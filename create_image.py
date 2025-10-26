from PIL import Image, ImageDraw, ImageFont

def create_image(raw_message: str, author: str, posted_on: str):
    width, height = 800, 1000
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except IOError:
        font = ImageFont.load_default()

    sender = "De: " + author
    sender_position = (10, 10)

    posted_on_str = posted_on[:16]
    posted_on_str = posted_on_str.replace("T", " ")
    printed_on_position = (10, 60)

    separator = "================================="
    separator_position = (10, 110)

    # After 25 chars skip a line
    limit = 26

    if len(raw_message) > limit:
        message = list(raw_message)
        count = 0
        for i in range(len(message)):
            if count == limit:
                message[i] = "\n" + message[i]
                count = 0
            count += 1
        message = "".join(message)
    else:
        message = raw_message

    message_position = (10, 160)

    draw.text(sender_position, sender, fill="black", font=font)
    draw.text(printed_on_position, posted_on_str, fill="black", font=font)
    draw.text(separator_position, separator, fill="black", font=font)
    draw.text(message_position, message, fill="black", font=font)

    return img