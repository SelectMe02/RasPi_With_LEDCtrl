







```
#!/usr/bin/python3
# → 이 스크립트를 Python3 인터프리터로 실행하라는 의미 (Shebang)
# → 터미널에서 './파일명.py'로 실행할 수 있게 함

from gpiozero import LED
# → gpiozero는 라즈베리파이에서 GPIO 제어를 쉽게 해주는 라이브러리
# → 여기서 'LED' 클래스는 GPIO 핀을 LED처럼 제어할 수 있게 해줌

from time import sleep
# → sleep() 함수는 코드 실행을 지정한 시간(초) 동안 멈춤
# → 여기선 LED 전환 주기를 1초로 설정하기 위해 사용

from signal import pause
# → signal.pause()는 프로그램을 무한 대기 상태로 유지할 때 사용
# → 이 코드에선 사용하지 않았지만, 백그라운드에서 이벤트 대기를 할 때 유용

import signal
# → 운영체제에서 발생하는 신호(예: Ctrl+C = SIGINT)를 감지해서 처리할 수 있게 해줌
# → 사용자 정의 종료 동작(cleanup 함수)을 등록할 때 사용됨

import sys
# → sys.exit() 함수를 통해 프로그램을 강제 종료할 때 필요
# → 또한 시스템 관련 정보 및 제어 기능 제공


# 각 비트에 해당하는 GPIO 핀 설정
leds = [
    LED(17),  # bit 0 (LSB) → 1의 자리
    LED(27),  # bit 1        → 2의 자리
    LED(22)   # bit 2 (MSB) → 4의 자리
]
# → 3개의 GPIO 핀을 각각 하나의 LED로 설정하고 리스트에 저장
# → 이 리스트를 통해 반복문으로 LED를 제어 가능


# Ctrl+C 종료 처리용 함수 정의
def cleanup(signal_num, frame):
    print("\nLED 끄는 중...")  # 종료 메시지 출력
    for led in leds:          # 모든 LED 반복하면서
        led.off()             # 꺼줌 (안 끄면 프로그램 종료 후에도 켜진 상태일 수 있음)
    sys.exit(0)               # 프로그램 종료 (정상 종료 코드 0 반환)

# 종료 시그널(SIGINT = Ctrl+C, SIGTERM = kill 명령 등)을 감지하면
# 위에서 정의한 cleanup() 함수를 실행하도록 등록
signal.signal(signal.SIGINT, cleanup)   # Ctrl+C 시
signal.signal(signal.SIGTERM, cleanup)  # 시스템 종료 요청 시

# 무한 루프: 0부터 7까지 숫자를 이진수로 표현하여 LED로 출력
while True:
    for value in range(8):  # value = 0부터 7까지 총 8번 반복
        for i in range(3):  # i = 0, 1, 2 → 각 비트를 하나씩 검사
            # (value >> i) & 1:
            # value를 i만큼 오른쪽으로 쉬프트 → i번째 비트를 LSB로 이동
            # & 1 → 마지막 비트만 추출 (1이면 켜고, 0이면 끔)
            if (value >> i) & 1:
                leds[i].on()   # i번째 LED 켜기
            else:
                leds[i].off()  # i번째 LED 끄기
        sleep(1)  # 1초 대기 후 다음 숫자로 넘어감
```
