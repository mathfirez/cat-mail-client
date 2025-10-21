package main

import (
	"cat-mail-client/src/scheduler"
	"log"
	"os"
	"strconv"
)

func main() {
	// Gets Scheduler interval.
	interval, err := strconv.Atoi(os.Getenv("INTERVAL"))

	if err != nil {
		log.Fatal(err)
	}

	// Starts main loop.
	scheduler.Scheduler(interval)
}
