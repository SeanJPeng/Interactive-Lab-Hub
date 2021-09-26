import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 

    # block to show the hours
    hours = int(time.strftime("%I"))
    hourBlock = ""
    for _ in range(hours):
        hourBlock += "H"
    for _ in range(12-hours):
        hourBlock += "X"
    y = top
    draw.text((x,y),hourBlock,font=font,fill="#FFFF00")
    
    #block to show the minutes
    minutes = time.strftime("%M")
    min1 = int(minutes[0])
    min2 = int(minutes[1])
    min1Block = ""
    min2Block = ""
    for _ in range(min1):
        min1Block += "M"
    for _ in range(6-min1):
        min1Block += "X"
    for _ in range(min2):
        min2Block += "m"
    for _ in range(9-min2):
        min2Block += "X"
    # min1Block = "".join(["M" for _ in range(min1)])
    # min2Block = "".join(["M" for _ in range(min2)])
    y += font.getsize(hourBlock)[1]
    draw.text((x,y),min1Block,font=font,fill="#0000FF")
    y += font.getsize(min1Block)[1]
    draw.text((x,y),min2Block,font=font,fill="#0000FF")

    # block to show the seconds
    seconds = time.strftime("%S")
    sec1 = int(seconds[0])
    sec2 = int(seconds[1])
    sec1Block = "".join(["S" for _ in range(sec1)])
    sec2Block = "".join(["s" for _ in range(sec2)])
    y += font.getsize(min2Block)[1]
    draw.text((x,y),sec1Block,font=font, fill="#FF00FF")
    y += font.getsize(sec1Block)[1]
    draw.text((x,y),sec2Block,font=font, fill="#FF00FF")

    
    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
