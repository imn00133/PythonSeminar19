s1 = 1
s2 = 1
x = 0
y = -1
cnt = 0
inp = int(input("입력하세요: "))
n = inp
arr = []
for i in range(0, inp):
    arr.append([])

for i in range(0, inp):
    for j in range(0, inp):
        arr[i].append(0)

for i in range(inp * inp-1):
    for j in range(n):
        if s1 == 1:
            y = y + 1
        elif s1 == 2:
            x = x + 1
        elif s1 == 3:
            y = y - 1
        elif s1 == 4:
            x = x - 1
        cnt = cnt + 1
        arr[x][y] = cnt
    s2 = s2 + 1
    s1 = (s1 % 4) + 1
    if s2 == 2:
        s2 = 0
        n = n - 1

for i in range(inp):
    for j in range(inp):
        print("%d " % arr[i][j], end='')
    print("")

# 잘 만들었으나, 과제가 정사각만 확인하지 않습니다..?
# 수고하셨습니다.
# 주강사 김재형
