import esp32
import urandom
import utime

class Demo(object):
    def __init__(self, np):
        self.np = np

    def loop(self, ntimes):
        raise Exception("implement loop in Demo subclass")

    def name(self):
        return type(self).__name__
