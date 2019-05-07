treeplz = 0  # 트리 개수 받는 변수
while treeplz >= 0:  # 입력 값이 음수가 나오기 전까지 반복
    treeplz = int(input("그리고 싶은 별 트리의 개수를 입력하세요 (1~79): "))

    if treeplz > 0 and treeplz < 80:
        for i in range(1, treeplz+1):  # 트리 출력을 위한 반복문
            print("{0}{1}".format(" "*(treeplz-i), "*"*(i+(i-1))))
    elif treeplz == 0 or treeplz > 79:
        print("1에서 79까지의 범위만 입력할 수 있습니다.")

print("종료합니다.")

# 인라인 주석은 웬만하면 하지 않는 것이 좋습니다.
# 5번 라인에서 0 < treeplz < 80으로 고칠 수 있습니다.(python 특성)
# 괄호가 반복되는 경우가 많습니다. 7번 줄에서 (i+(i-1))은 (2i-1)로 고칠 수 있습니다.
# range의 범위를 바꾸면 더 보기 좋을 수도 있으나, 크게 문제는 없습니다.
# 잘 해결하셨습니다.
# 주강사 김재형
