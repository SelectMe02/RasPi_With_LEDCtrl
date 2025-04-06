#!/usr/bin/bash

# GPIO 핀 설정
gpio0=17
gpio1=27
gpio2=22
gpio3=5

# 배열로 핀 묶기
gpios=($gpio0 $gpio1 $gpio2 $gpio3)

# 핀 출력 모드로 설정
initialize_pins() {
    for pin in "${gpios[@]}"; do
        pinctrl set "$pin" op || {
            echo "[ERROR] GPIO $pin 출력 모드 설정 실패"
            exit 1
        }
    done
}

# 모든 핀 OFF (종료 시)
turn_off_all() {
    for pin in "${gpios[@]}"; do
        pinctrl set "$pin" dl
    done
    echo "LED OFF 후 종료합니다."
    exit 0
}

# 루프 내부에서 쓸 LED OFF 함수 (종료 안 함)
turn_off_leds() {
    for pin in "${gpios[@]}"; do
        pinctrl set "$pin" dl
    done
}

# 종료 시 LED OFF
trap turn_off_all SIGINT SIGTERM

# 핀 초기화
initialize_pins

# 무한 루프: 도미노처럼 LED 하나씩 켜기
while true; do
    for i in "${!gpios[@]}"; do
        turn_off_leds                      # 현재 반복에서 모든 LED 끄고
        pinctrl set "${gpios[$i]}" dh      # 해당 LED만 켜기
        sleep 1
    done
done
