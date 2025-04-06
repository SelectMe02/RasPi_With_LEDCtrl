#!/usr/bin/env bash

# GPIO 핀 번호 설정
gpio_bit0=17  # LSB (1의 자리)
gpio_bit1=27  # Middle bit (2의 자리)
gpio_bit2=22  # MSB (4의 자리)

# GPIO 핀 출력 모드로 설정
initialize_pins() {
    for pin in $gpio_bit0 $gpio_bit1 $gpio_bit2; do
        pinctrl set "$pin" op || {
            echo "[ERROR] GPIO $pin 출력 모드 설정 실패"
            exit 1
        }
    done
}
# 종료 시 LED OFF 처리
stop_to_ctrlC() {
    echo "LED 끄는 중..."
    pinctrl set $gpio_bit0 dl
    pinctrl set $gpio_bit1 dl
    pinctrl set $gpio_bit2 dl
    exit 0
}

# 종료 신호 감지
trap stop_to_ctrlC SIGINT SIGTERM

# 핀 초기화
initialize_pins

# 무한 루프: 0부터 7까지 반복하며 3비트 LED 제어
while true; do
    for value in {0..7}; do
        # 비트 분해 (비트 시프트 & 비트 AND 연산 사용)
        bit0=$(( (value >> 0) & 1 ))
        bit1=$(( (value >> 1) & 1 ))
        bit2=$(( (value >> 2) & 1 ))

        # LED 제어
        pinctrl set $gpio_bit0 $( [ $bit0 -eq 1 ] && echo dh || echo dl )
        pinctrl set $gpio_bit1 $( [ $bit1 -eq 1 ] && echo dh || echo dl )
        pinctrl set $gpio_bit2 $( [ $bit2 -eq 1 ] && echo dh || echo dl )

        # 1초 대기
        sleep 1
    done
done

