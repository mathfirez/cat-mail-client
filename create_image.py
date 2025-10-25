from PIL import Image, ImageDraw, ImageFont

def create_image(raw_message: str):
    width, height = 800, 1000
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except IOError:
        font = ImageFont.load_default()

    sender = "De: Miçanga"
    sender_position = (10, 10)

    separator = "================================="
    separator_position = (10, 60)

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

    message_position = (10, 100)

    draw.text(sender_position, sender, fill="black", font=font)
    draw.text(separator_position, separator, fill="black", font=font)
    draw.text(message_position, message, fill="black", font=font)

    return img