#!/usr/bin/python3

from gpiozero import LED, Button
from time import sleep

button = Button(25)
leds = [LED(pin) for pin in [7, 8, 16, 20]]

while True:
    if button.is_pressed:
        for led in leds:
            led.on()
    else:
        for led in leds:
            led.off()
    sleep(0.05)


