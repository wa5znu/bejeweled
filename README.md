# Bejeweled

Experiment space for 01space ESP32 sbc with 5x5 LED pixel display.

# Development
- Downloads esp32c3-usb nightly after july something
- esptool.py --chip esp32c3 --port /dev/ttyACM0 erase_flash
- esptool.py --chip esp32c3 --port /dev/ttyACM0 --baud 460800 write_flash -z 0x0 esp32c3-usb-20220725-unstable-v1.19.1-209-g0c45a28d2.bin
- use thonny or try ampy with emacs

# References

## Products
- https://www.banggood.com/ESP32-C3-Development-Board-RISC-V-WiFi-Bluetooth-IoT-Development-Board-Compatible-with-Python-p-1914005.html
- https://www.banggood.com/ESP32-PICO-D4-Development-Board-WiFi-bluetooth-Internet-of-Things-IoT-Compatible-with-Python-p-1914004.html
- https://github.com/01Space/ESP32-C3FH4-RGB
- https://github.com/01Space/ESP32-PICO-D4-RGB

# Reviews
- https://www.cnx-software.com/2022/01/07/board-with-25-rgb-leds-is-offered-with-esp32-c3-or-esp32-pico-d4/

## Development
- https://micropython.org/download/esp32c3-usb/ # esp32c3-usb-20220725-unstable-v1.19.1-209-g0c45a28d2.bin
- https://bigl.es/tooling-tuesday-a-m-p-y/ # not yet tried

## Examples
- https://github.com/andypiper/fivebyfive/blob/main/notes.md
- https://github.com/pimoroni/rgbmatrix5x5-python/blob/master/examples/rainbow.py
- https://bigl.es/friday-fun-micro-weather-station/

## Utilities
- https://stackoverflow.com/questions/24852345/hsv-to-rgb-color-conversion
- https://thonny.org/
