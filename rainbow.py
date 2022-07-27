#!/usr/bin/env python
# https://github.com/pimoroni/rgbmatrix5x5-python/blob/master/examples/rainbow.py
# https://stackoverflow.com/questions/24852345/hsv-to-rgb-color-conversion

import utime, math
import esp32
from demo import Demo


class Rainbow(Demo):
    def __init__(self, np):
        super().__init__(np)
        self.spacing = 360.0 / 5.0
        self.BRIGHTNESS=8
        self.hue = 0

    def loop(self, ntimes):
        def hsv_to_rgb2(h, s, v):
            if s == 0.0: return (v, v, v)
            i = int(h*6.) # XXX assume int() truncates!
            f = (h*6.)-i; p,q,t = v*(1.-s), v*(1.-s*f), v*(1.-s*(1.-f)); i%=6
            if i == 0: return (v, t, p)
            if i == 1: return (q, v, p)
            if i == 2: return (p, v, t)
            if i == 3: return (p, q, v)
            if i == 4: return (t, p, v)
            if i == 5: return (v, p, q)
    
        np = self.np
        spacing = self.spacing
        brightness = self.BRIGHTNESS
        for nt in range(ntimes * 20):
            self.hue = (self.hue + 1) % 360
            for x in range(5):
                for y in range(5):
                    offset = (x * y) / 25.0 * spacing
                    h = ((self.hue + offset) % 360) / 360.0
                    rgb = [int(c*brightness) for c in hsv_to_rgb2(h, 1.0, 1.0)]
                    np[x + y * 5] = rgb
            np.write()
 
