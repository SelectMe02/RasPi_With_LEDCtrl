
#!/usr/bin/python3

from gpiozero import LED, Button
from time import sleep

button = Button(25)
leds = [LED(pin) for pin in [7, 8, 16, 20]]  # LSB부터

prev = 1
count = 0

def update_leds(val):
    for i in range(4):
        bit = (val >> i) & 1
        if bit:
            leds[i].on()
        else:
            leds[i].off()

while True:
    curr = button.is_pressed
    if curr and not prev:
        count = (count + 1) % 16
        print(f"Count: {count}")
        update_leds(count)
    prev = curr
    sleep(0.05)
