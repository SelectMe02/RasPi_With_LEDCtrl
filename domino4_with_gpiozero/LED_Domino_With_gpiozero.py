#!/usr/bin/python3

from gpiozero import LED
from time import sleep
import signal
import sys

# 사용할 GPIO 핀 번호를 순서대로 리스트에 저장
pins = [17, 27, 22, 5]
leds = [LED(pin) for pin in pins]

# 종료 시 모든 LED OFF 후 종료
def cleanup(sig, frame):
    print("\nLED OFF 후 종료합니다.")
    for led in leds:
        led.off()
    sys.exit(0)

# 종료 시그널 핸들링 등록 (Ctrl+C 등)
signal.signal(signal.SIGINT, cleanup)
signal.signal(signal.SIGTERM, cleanup)

# 메인 루프: LED 하나씩 도미노처럼 켜기
while True:
    for led in leds:
        for l in leds:
            l.off()       # 모든 LED OFF
        led.on()          # 현재 LED만 ON
        sleep(1)          # 1초 대기
