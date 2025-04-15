#!/usr/bin/python3

from gpiozero import LED
from time import sleep
from signal import pause
import signal
import sys

# 각 비트에 해당하는 GPIO 핀 설정
leds = [
    LED(17),  # bit 0 (LSB)
    LED(27),  # bit 1
    LED(22)   # bit 2 (MSB)
]

# Ctrl+C 종료 처리
def cleanup(signal_num, frame):
    print("\nLED 끄는 중...")
    for led in leds:
        led.off()
    sys.exit(0)

signal.signal(signal.SIGINT, cleanup)
signal.signal(signal.SIGTERM, cleanup)

# 메인 루프
while True:
    for value in range(8):  # 0 ~ 7
        for i in range(3):
            if (value >> i) & 1:
                leds[i].on()
            else:
                leds[i].off()
        sleep(1)

