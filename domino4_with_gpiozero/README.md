






```

#!/usr/bin/python3
# 🟡 이 스크립트를 Python3 인터프리터로 실행하라는 지시
# 🟡 이 줄 덕분에 터미널에서 `./파일명.py`처럼 직접 실행 가능하게 됨

from gpiozero import LED
# ✅ gpiozero: 라즈베리파이의 GPIO 핀을 제어하기 위한 고수준(high-level) 라이브러리
# ✅ LED 클래스는 특정 GPIO 핀을 LED처럼 제어할 수 있게 해줌
#    ex) led.on(), led.off(), led.value = 1 (켜짐), 0 (꺼짐) 등

from time import sleep
# ✅ sleep(): 코드 실행을 잠시 멈추는 함수 (단위: 초)
# ✅ 여기선 LED 간의 점등 간격을 1초로 두기 위해 사용

import signal
# ✅ signal: 시스템 종료 시그널을 처리하기 위한 모듈
# ✅ 예: SIGINT (Ctrl+C), SIGTERM (kill 명령 등)
# ✅ 시그널을 감지해서 특정 함수를 실행시킬 수 있음 (여기선 cleanup)

import sys
# ✅ sys: 시스템 관련 기능을 제공하는 모듈
# ✅ 여기선 `sys.exit(0)`을 통해 프로그램을 명시적으로 종료하기 위해 사용


# 사용할 GPIO 핀 번호를 순서대로 리스트에 저장
pins = [17, 27, 22, 5]
# ✅ Raspberry Pi의 GPIO 핀 번호 (BCM 번호 기준)
# ✅ 4개의 핀을 사용하여 4개의 LED 제어

leds = [LED(pin) for pin in pins]
# ✅ 각 핀 번호에 대해 LED 객체를 생성하고 리스트로 저장
# ✅ 이렇게 하면 `leds[0]`은 GPIO 17에 연결된 LED 객체가 됨
# ✅ 반복문을 사용할 수 있어 코드가 간결하고 확장성 있음


# 종료 시 모든 LED OFF 후 프로그램 종료하는 함수 정의
def cleanup(sig, frame):
    print("\nLED OFF 후 종료합니다.")  # 종료 메시지 출력
    for led in leds:      # 모든 LED를 반복하며
        led.off()         # 각각의 LED를 끔
    sys.exit(0)           # 정상 종료 (exit code 0)

# 종료 시그널 핸들링 등록
signal.signal(signal.SIGINT, cleanup)
# ✅ SIGINT: Ctrl+C를 눌렀을 때 발생하는 인터럽트 시그널
# ✅ 이 시그널이 오면 위에서 정의한 cleanup() 함수가 실행됨

signal.signal(signal.SIGTERM, cleanup)
# ✅ SIGTERM: kill 명령 등으로 프로세스 종료 요청 시 발생하는 시그널
# ✅ 이 시그널도 cleanup() 함수로 처리되게 설정


# 무한 루프: LED를 도미노처럼 하나씩 켰다가 끄기
while True:
    for led in leds:           # LED 리스트를 순서대로 반복하면서
        for l in leds:
            l.off()            # 모든 LED를 먼저 꺼줌
        led.on()               # 현재 선택된 LED만 켬
        sleep(1)               # 1초 대기 후 다음 LED로 넘어감

```
