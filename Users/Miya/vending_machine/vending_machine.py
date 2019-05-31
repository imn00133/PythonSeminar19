items = [{"블랙커피": 100}, {"밀크커피": 150}, {"고급커피": 200}]
quantity = [0, 2, 0]
menu = ["돈 입력", "거스름돈", "종료"]
admenu = ["물품출력", "개수추가", "종료"]
mode = 0
money = 0

while True:
    if mode == 0:
        for i in items:
            for coffee in i:
                print("%d. %s(%s원)" % (items.index(i) + 1, coffee, i[coffee]))

        for m in menu:
            print("%d. %s" % (len(items) + menu.index(m) + 1, m))

        print("현재까지 넣은 돈은 %d원입니다." % money)
        sel = input("뽑을 물품을 골라주세요: ")

        if sel == "admin":
            mode = 1
            continue
        else:
            sel = int(sel)

        if sel in range(1, len(items)+1):
            if quantity[sel-1] > 0:
                if money >= items[sel-1][list(items[sel-1]).pop()]:
                    money = money - items[sel-1][list(items[sel-1]).pop()]
                    print("%s이/가 나왔습니다." % list(items[sel-1]).pop())
                else:
                    print("돈이 부족합니다. 돈을 더 넣어주세요.")
            else:
                print("물품 개수가 부족합니다. 관리자를 불러주세요.")
        elif sel == len(items)+1:
            money = money + int(input("돈을 넣으세요: "))
        elif sel == len(items)+2 or sel == len(items)+3:
            print("돈을 반환합니다: %d원" % money)
            money = 0
            if sel == len(items)+3:
                break
        print("")
    else:
        print("")
        for adm in admenu:
            print("%d. %s" % (admenu.index(adm)+1, adm))

        sel = int(input("원하는 작업을 선택해주세요: "))

        if sel == 3:
            print("자판기 모드로 돌아갑니다.")
            mode = 0
            continue
        elif sel == 1 or sel == 2:
            print("")
            for i in items:
                for coffee in i:
                    print("%d. %s(%s원) 개수: %d" % (items.index(i) + 1, coffee, i[coffee], quantity[items.index(i)]))

        if sel == 2:
            sel = int(input("개수를 추가할 물품을 선택하세요: "))
            quantity[sel-1] += int(input("추가할 개수를 입력해주세요: "))
print("프로그램을 종료합니다.")
# 시간이 없어 주석을 달지 못했습니다. ㅇwㅇ (귀찮았던 것은 아닙니다 ㅎ..ㅎ)

# 잘 해결하였으나, 현재 들여쓰기가 많이 되는 것을 볼 수 있습니다.
# 이럴 경우에는 main부분과 admin부분을 나눠 함수로 작성하는 것이 좀 더 깔끔할 수 있습니다.
# 들여쓰기가 많이 될수록 전체적인 흐름을 이해하기 어려울 수 있습니다.
# 주강사 김재형
