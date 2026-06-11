#0에서 100까지의 숫자 중 하나를 랜덤하게 선정함
#플레이어에게 숫자를 입력받으면 입력된 숫자와 선정된 숫자를 비교해 '업'혹은 '다운'을 출력함
#두 숫자가 일치하면 게임 종료
import random

target = random.randint(1, 100)

print("1부터 100까지의 숫자에서 랜덤한 수자를 선정합니다.")

while True:
    num = int(input("숫자를 입력하세요>> "))

    if num < target:
        print("업")
    elif num > target:
        print("다운")
    else:
        print("정답")
        break