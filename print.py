#!/usr/bin/env python
import argparse
import asyncio
from datetime import datetime, timedelta
import logging
import sys
from typing import cast

from catprinter import logger
from catprinter.cmds import PRINT_WIDTH, cmds_print_img
from catprinter.ble import run_ble
from catprinter.img import read_img
from catprinter.server import get_last_message
from create_image import create_image


def parse_args():
    args = argparse.ArgumentParser(
        description='prints an image on your cat thermal printer')
    args.add_argument('data', default= "aaaaaa", type=str)
    args.add_argument('-l', '--log-level', type=str,
                      choices=['debug', 'info', 'warn', 'error'], default='info')
    args.add_argument('-d', '--device', type=str, default='',
                      help=(
                          'The printer\'s Bluetooth Low Energy (BLE) address '
                          '(MAC address on Linux; UUID on macOS) '
                          'or advertisement name (e.g.: "GT01", "GB02", "GB03"). '
                          'If omitted, the the script will try to auto discover '
                          'the printer based on its advertised BLE services.'
                      ))
    args.add_argument('-e', '--energy', type=lambda h: int(h.removeprefix("0x"), 16),
                      help="Thermal energy. Between 0x0000 (light) and 0xffff (darker, default).",
                      default="0xffff")
    return args.parse_args()


def configure_logger(log_level):
    logger.setLevel(log_level)
    h = logging.StreamHandler(sys.stdout)
    h.setLevel(log_level)
    logger.addHandler(h)


def main(data):
    # args = parse_args()

    log_level = getattr(logging, cast(str, "debug").upper())
    configure_logger(log_level)

    # raw_data = cast(str, data).encode("utf-8")
    try:
        bin_img = read_img(
            data,
            PRINT_WIDTH,
            "floyd-steinberg",
        )
    except RuntimeError as e:
        logger.error(f'🛑 {e}')
        return
    
    data = cmds_print_img(bin_img, energy=int("0xffff".removeprefix("0x"), 16))
    logger.info(f'✅ Generated BLE commands: {len(data)} bytes')

    # Try to autodiscover a printer if --device is not specified.
    asyncio.run(run_ble(data, device=""))

try:
    if __name__ == '__main__':
        last_message = ""
        delta = timedelta(
            minutes=2,
        )
        last_request_time = datetime.now()
        while 1:
            if datetime.now() - delta < last_request_time:
                msg = get_last_message()
                if last_message != msg:
                    print(f"Found a new message: {msg}")
                    last_message = msg
                    main(create_image(msg))
except Exception as error:
    input(error)