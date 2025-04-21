#!/usr/bin/python3

from gpiozero import LED, Button
from time import sleep

button = Button(25)
leds = [LED(pin) for pin in [7, 8, 16, 20]]

prev = 1

while True:
    curr = button.is_pressed
    if curr and not prev:
        print("Button pressed, executing domino sequence...")
        n = 0
        for _ in range(len(leds)):
            leds[n].on()
            sleep(1)
            leds[n].off()
            sleep(1)
            n = (n + 1) % len(leds)
    prev = curr
    sleep(0.1)

