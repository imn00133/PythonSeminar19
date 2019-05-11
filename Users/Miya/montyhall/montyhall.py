import random

door = int(input("총 문의 개수를 입력하세요: "))
opdoor = int(input("사회자가 여는 문의 개수를 입력하세요: "))
rt = int(input("반복 횟수를 입력하세요: "))
moderator = []
mysel = 0
modsel = 0
cwin = 0
ncwin = 0
state = 0
tmp = 0
for change in range(2):
    for i in range(rt):
        car = random.randint(1, door)
        mysel = random.randint(1, door)
        while True:
            if len(moderator) == opdoor:
                break

            modsel = random.randint(1, door)

            if len(moderator) == 0:
                if modsel != mysel and modsel != car:
                    moderator.append(modsel)
                    continue

            for modcar in moderator:
                if modcar == modsel:
                    state = 1
                    break
            if state == 0:
                if modsel != mysel and modsel != car:
                    moderator.append(modsel)
            state = 0

        if change == 0:
            tmp = mysel
            while True:
                mysel = random.randint(1, door)
                for modsel in moderator:
                    if modsel == mysel:
                        state = 1
                        break
                if state == 0:
                    if mysel != tmp:
                        break
                state = 0
            if mysel == car:
                cwin += 1
        else:
            if mysel == car:
                ncwin += 1
        state = 0
        moderator = []


print("총 횟수: %d" % rt)
print("바꾸지 않았을 때 이긴 횟수: %d" % ncwin)
print("바꿨을 때 이긴 횟수: %d" % cwin)
print("바꾸지 않았을 때 이길 이론적 확률: %.4f" % (1/door))
print("바꾸지 않았을 때 이긴 시뮬레이션 확률: %.4f" % (ncwin/rt))
print("바꿨을 때 이길 이론적 확률: %.4f" % ((door-1)/(door*(door-opdoor-1))))
print("바꿨을 때 이긴 시뮬레이션 확률: %.4f" % (cwin/rt))

# 중간 중간 주석을 달아주는 것이 나중에 코드를 이해하기 좋습니다.
# 또한 변수명이 무엇을 뜻하는지 시간이 걸려, 조금 더 이해하기 쉽게 만드는 것이 좋을 것 같습니다.

# for과 if가 너무 깊게 들어가는 것은 좋지 않습니다.
# for로 moderator의 값을 전부 가져와 mysel을 비교하는 방법도 좋으나,
# if mysel in moderator을 통해서 for을 break로 빠져나가지 앟고, 바로 검색하는 방법도 있습니다.

# change부분은 이 시뮬레이션에서 꼭 필요한 부분이 아닙니다.
# 이로 인해 전체를 해석하기 더 어려워질 수 있습니다.

# 리스트에 선택한 문의 값을 넣어 비교하는 방법은 좋았습니다.
# 수고하셨습니다.
# 주강사 김재형
