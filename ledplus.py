from rpi_ws281x import *
import neopixel
import os

os.popen('sudo python3 ledplus.py')

nbled = 12
pin = 18
hz = 800000
dma = 10
lum = 255
invert = False
channel = 0

strip = Adafruit_NeoPixel(nbled, pin, hz, dma, invert, lum, channel)

strip.begin()

for x in range(0, nbled):
    strip.setPixelColor(x , Color(255,255,255))

strip.show()
