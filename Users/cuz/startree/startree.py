while True:
    input_startree = int(input("그리고 싶은 별 트리의 줄 수를 입력하세요.(1~79): "))
    if int(input_startree) < 0:
        break
    elif input_startree == 0 or input_startree >= 80:
        print("1에서 79까지만 입력가능합니다.")
        continue
    row = 1
    while row <= input_startree:
        print(" " * (input_startree - row), end="")
        print("*" * ((2 * row)-1))
        row += 1
print("프로그램을 종료합니다.")
