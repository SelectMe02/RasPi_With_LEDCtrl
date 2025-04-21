#!/usr/bin/python3

from gpiozero import LED, Button
from time import sleep

button = Button(25)
leds = [LED(pin) for pin in [7, 8, 16, 20]]

state = False
prev = 1

while True:
    curr = button.is_pressed
    if curr and not prev:
        state = not state
        for led in leds:
            if state:
                led.on()
            else:
                led.off()
    prev = curr
    sleep(0.05)

