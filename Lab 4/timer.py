# SPDX-FileCopyrightText: 2021 John Furcean
# SPDX-License-Identifier: MIT

"""I2C rotary encoder simple test example."""

import board
from adafruit_seesaw import seesaw, rotaryio, digitalio
import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# For use with the STEMMA connector on QT Py RP2040
# import busio
# i2c = busio.I2C(board.SCL1, board.SDA1)
# seesaw = seesaw.Seesaw(i2c, 0x36)

# code for encoder
seesaw = seesaw.Seesaw(board.I2C(), addr=0x36)

seesaw_product = (seesaw.get_version() >> 16) & 0xFFFF
print("Found product {}".format(seesaw_product))
if seesaw_product != 4991:
    print("Wrong firmware loaded?  Expected 4991")

seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
button = digitalio.DigitalIO(seesaw, 24)
button_held = False

encoder = rotaryio.IncrementalEncoder(seesaw)
last_position = None
    
# code for display
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

# code the actual timer
def startTimer(position):
    t = int(position)
    while t:
        mins, secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x,y),timer,font=font,fill="#FFFF00")
        
        print(timer,end="\r")
        time.sleep(1)
        t-=1
    print("Time up!!")
    
# controller
while True:

    # negate the position to make clockwise rotation positive
    position = -encoder.position

    if position != last_position:
        last_position = position
        print("Position: {}".format(position))

    if not button.value and not button_held:
        button_held = True
        startTimer(position)
        # print("Button pressed")

    if button.value and button_held:
        button_held = False
        # print("Button released")



