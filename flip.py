import esp32
import urandom
import utime

from demo import Demo

np=None
BRIGHTNESS=16


class Flip(Demo):
    def __init__(self, np):
        super().__init__(np)

    def loop(self, ntimes):
        def x():
           return urandom.randint(0, BRIGHTNESS)
        np = self.np
        for nt in range(ntimes):
            for i in range(25):      
                np[i] = (x(),x(),x())
            np.write()
            utime.sleep(0.1)
