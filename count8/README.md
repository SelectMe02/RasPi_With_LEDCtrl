# Mission B - 3 Bit LED Counter  
(with Raspberry Pi & Bash Script)

---

## 📘 과제 설명

3 Bit LED Counter를 구현하는 과제입니다.  
Bash 스크립트(`3_Bit_Counter.sh`)를 작성하여 3개의 LED를 통해 0부터 7까지 숫자를 이진수로 표현합니다.

---

## 🧠 프로젝트 소개

이 프로젝트는 **Raspberry Pi의 GPIO 핀**과 **bash 스크립트**를 이용하여  
숫자 0부터 7까지의 값을 3개의 LED로 이진수 형태로 출력하는 카운터 시스템입니다.

스크립트를 실행하면 3개의 LED가 현재 숫자를 이진수로 나타내며,  
1초마다 숫자가 1씩 증가하면서 LED 상태가 바뀝니다.

---

## ✨ 주요 기능 요약

- 🔢 숫자 카운팅 (0~7)
- 💡 이진수 LED 출력 (3개 LED로 표현)
- ⏱️ 1초 간격 자동 점등
- 🧰 Raspberry Pi GPIO 핀 제어
- 📜 간단한 Bash 스크립트 기반 실행

---

## 🔧 기술 구성

- **Raspberry Pi** – GPIO 핀 제어
- **bash script** – 제어용 스크립트 언어
- **pinctrl** – GPIO 핀의 상태 제어 명령어

---

## 📌 핀 구성 및 역할

| 핀 번호    | 역할             | 설명                            |
|------------|------------------|---------------------------------|
| GPIO 17    | LSB (1의 자리)   | 가장 작은 비트를 제어하는 LED |
| GPIO 22    | Middle (2의 자리)| 중간 비트를 제어하는 LED       |
| GPIO 27    | MSB (4의 자리)   | 가장 큰 비트를 제어하는 LED   |

---

## 🔌 회로 구성 설명

- 각 LED는 **330Ω 저항**을 거쳐 브레드보드의 **GND에 연결**
- Raspberry Pi의 GPIO 핀이 **HIGH(dh)** 상태가 되면 전류가 흐르며 LED가 점등됨
- pinctrl 명령어를 사용해 핀을 제어

---

## 💻 스크립트 코드

```bash
#!/usr/bin/env bash

# GPIO 핀 설정
gpio_bit0=17  # LSB (1의 자리)
gpio_bit1=22  # Middle bit (2의 자리)
gpio_bit2=27  # MSB (4의 자리)

# GPIO 핀 출력 모드 설정
for gpio in $gpio_bit0 $gpio_bit1 $gpio_bit2; do
    pinctrl set "$gpio" op
done

# 무한 루프 시작
while true; do
    for value in {0..7}; do
        # 비트 분해
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

