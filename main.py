import esp32
from machine import Pin
from neopixel import NeoPixel
from flip import Flip
from rainbow import Rainbow
from weather import Weather


esp32.RMT.bitstream_channel(0)
np = NeoPixel(Pin(8, Pin.OUT) , 26)

#demos = [Weather(np), Flip(np), Rainbow(np)]
demos = Weather(np)
print(' & '.join(demo.name() for demo in demos))

while True:
    for demo in demos:
        print(demo.name())
        demo.loop(50)
