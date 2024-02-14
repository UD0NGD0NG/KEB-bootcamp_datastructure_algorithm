import random
ans = random.randint(1, 128)

chance = 7
try_cnt = 0
success = False

while chance > 0:
    try_cnt += 1
    my_ans = int(input("생각한 수를 입력해주세요(1 ~ 128): "))
    if my_ans == ans:
        print(f"정답입니다. 시도 횟수: {try_cnt}")
        success = True
        break
    elif my_ans < ans:
        print(f"{my_ans}가 정답보다 작습니다.")
    else:
        print(f"{my_ans}가 정답보다 큽니다.")
    chance -= 1
    print(f"{chance}번 남았습니다.")

if not success:
    print("실패")