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
