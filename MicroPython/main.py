# Copyright (c) 2025 Isaac Ip All rights reserved
#
# Created by: Isaac Ip
# Created on: Oct 2025
# This program creates a traffic light with Neopixels.

from microbit import *
import neopixel

# variables
neopixelStrip = neopixel.NeoPixel(pin16, 4)

# cleanup
display.clear()
neopixelStrip[0] = (0, 0, 0)
neopixelStrip[1] = (0, 0, 0)
neopixelStrip[2] = (0, 0, 0)
neopixelStrip[3] = (0, 0, 0)
neopixelStrip.show()
display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        display.show(Image.ARROW_E)

        # Red
        neopixelStrip[2] = (255, 0, 0)  # Red
        neopixelStrip.show()
        sleep(1000)

        # Yellow
        neopixelStrip[2] = (0, 0, 0)
        neopixelStrip[1] = (255, 255, 0)  # Yellow
        neopixelStrip.show()
        sleep(1000)

        # Green
        neopixelStrip[1] = (0, 0, 0)
        neopixelStrip[0] = (0, 255, 0)  # Green
        neopixelStrip.show()
        sleep(1000)

        # Turn off all
        neopixelStrip[0] = (0, 0, 0)
        neopixelStrip.show()

        display.show(Image.YES)
