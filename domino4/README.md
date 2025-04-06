## 💡 Mission A - LED 도미노 과제

본 스크립트는 Raspberry Pi의 GPIO 핀을 제어하여 LED를 도미노처럼 순차적으로 점등하는 과제입니다.  
사용된 언어는 Bash이며, pinctrl 명령어를 사용해 GPIO 핀의 출력 상태를 조절합니다.

---

### 📋 주요 기능 요약

- ✅ LED는 1초 간격으로 하나씩 순차적으로 켜집니다.
- ✅ 한 번에 **오직 하나의 LED만 ON**, 나머지는 OFF 상태입니다.
- ✅ Ctrl + C로 스크립트를 종료하면 LED가 모두 꺼지고 안전하게 종료됩니다.
- ✅ `GPIO 17`, `27`, `22`, `5`번 핀을 사용하여 총 4개의 LED를 제어합니다.

---

### 🔧 사용된 GPIO 핀 설정

| 핀 번호  | 설명                 |
|----------|----------------------|
| GPIO 17  | LED 1                |
| GPIO 27  | LED 2                |
| GPIO 22  | LED 3                |
| GPIO 5   | LED 4                |

---

### 🧾 코드 전체 설명

```bash
#!/usr/bin/bash  # Bash 인터프리터 사용 명시

# GPIO 핀 설정 (LED 순서대로 지정)
gpio0=17
gpio1=27
gpio2=22
gpio3=5

# 배열로 핀 묶기 (반복문 처리 용이)
gpios=($gpio0 $gpio1 $gpio2 $gpio3)

# 모든 핀 출력 모드로 초기화
initialize_pins() {
    for pin in "${gpios[@]}"; do
        pinctrl set "$pin" op || {
            echo "[ERROR] GPIO $pin 출력 모드 설정 실패"
            exit 1
        }
    done
}

# 종료 시 모든 핀 OFF 처리
turn_off_all() {
    for pin in "${gpios[@]}"; do
        pinctrl set "$pin" dl  # LOW로 설정
    done
    echo "LED OFF 후 종료합니다."
    exit 0
}

# 루프 내에서 사용하는 LED OFF 함수 (종료는 아님)
turn_off_leds() {
    for pin in "${gpios[@]}"; do
        pinctrl set "$pin" dl
    done
}

# Ctrl+C 또는 SIGTERM 시 종료 핸들러 등록
trap turn_off_all SIGINT SIGTERM

# 핀 초기화
initialize_pins

# 도미노처럼 LED를 순차적으로 켜는 무한 루프
while true; do
    for i in "${!gpios[@]}"; do
        turn_off_leds                      # 현재 모든 LED OFF
        pinctrl set "${gpios[$i]}" dh     # 해당 핀만 ON
        sleep 1                            # 1초 대기
    done
done
```

---

### 🛠 실행 방법

1. 터미널에서 스크립트에 실행 권한을 부여합니다:

```bash
chmod +x LED_Domino.sh
```

2. 스크립트를 실행합니다:

```bash
./LED_Domino.sh
```

3. Ctrl + C로 종료하면 모든 LED가 꺼집니다.

---

### 📌 실행 결과 예시 (도미노 순차 점등)

```
🟥 ⬛ ⬛ ⬛   ← LED1 ON
⬛ 🟥 ⬛ ⬛   ← LED2 ON
⬛ ⬛ 🟥 ⬛   ← LED3 ON
⬛ ⬛ ⬛ 🟥   ← LED4 ON
(다시 반복)
```

