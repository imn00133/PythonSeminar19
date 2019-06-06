import random

com = []
cnt = 0
state = 0
usr = ""
strike = 0
ball = 0
out = 0
play = 0

while play == 0:
    while len(com) < 4:
        if len(com) == 0:
            com.append(random.randint(0, 9))
        else:
            tmp = random.randint(0, 9)
            for i in range(len(com)):
                if com[i] == tmp:
                    break
                else:
                    if i == len(com)-1:
                        com.append(tmp)

    while True:
        while True:
            usr = input("중복되지 않은 4자리 수를 입력해주세요(0000~9999): ")
            usr = list(usr)
            if len(usr) != 4:
                print("4자리 숫자를 입력해주세요.")
                continue
            for i in range(3):
                for j in range(i + 1, 4):
                    if usr[i] == usr[j]:
                        state = 1
                        break
                if state == 1:
                    print("각 자리 숫자가 중복되지 않게 입력해주세요.")
                    break
            if state == 0:
                break
            else:
                state = 0
        cnt += 1
        for i in range(4):
            for j in range(4):
                if int(com[i]) == int(usr[j]):
                    if i == j:
                        strike += 1
                    else:
                        ball += 1
                    state = 1
                    break
            if state == 0:
                out += 1
            state = 0

        print("strike: %d, ball: %d, out: %d" % (strike, ball, out))
        if strike == 4:
            break
        else:
            strike = 0
            ball = 0
            out = 0

    print("축하합니다. %d번만큼 질문하여 맞추셨습니다." % cnt)
    cnt = 0
    while True:
        usr = input("다시 하시겠습니까?(yes/no) ")
        if usr == "yes" or usr == "y":
            com = []
            strike = 0
            ball = 0
            out = 0
            break
        elif usr == "no" or usr == "n":
            play = 1
            break

# 플래그를 사용하는 것도 좋습니다. 하지만 현재 구문들의 깊이가 깊어, 함수 처리를 해주는 것이 좋습니다.
# 변수의 초기화를 맨 처음이 아닌, 사용하기 직전에 초기화 해주는 것이 좋습니다.
# 특히, 지금처럼 재사용시 맨 마지막에 초기화를 해주어야 한다면, 사용하기 전에 해주면 따로 초기화할 필요가 없습니다.
# 45번째 줄에서 for 중첩으로 비교하고 있습니다. 이렇게 해주어도 좋지만, 파이썬에서는 in을 사용할 수 있습니다.
# 16-23번째 줄은 좀 더 간단하게 수정할 수 있습니다. in과 not in을 사용하시면 편합니다.
# 25, 26처럼 while True가 반복된다면, 함수로 처리하는 것이 가독성면에서 좋습니다.
# 수고하셨습니다.
# 주강사 김재형
