global items
items = [{"블랙커피": 100}, {"밀크커피": 150}, {"고급커피": 200}]
global quantity
quantity = [0, 2, 0]
menu = ["돈 입력", "거스름돈", "종료"]
admenu = ["물품추가", "물품변경", "물품삭제", "물품출력", "개수추가", "종료"]
mode = 0
money = 0

def FileWrite():
    try:
        file = open('items_list.txt', 'w', encoding='utf-8')
        apitems = []
        for i in range(len(items)):
            apitems.append(("%s|%d|%d\n" % (list(items[i].keys()).pop(), items[i][list(items[i]).pop()], quantity[i])))
        file.writelines(apitems)
        file.close()
    except:
        print("읽는 도중 문제가 발생하였습니다.")

def FileRead():
    global items
    items = []
    global quantity
    quantity = []
    try:
        file = open('items_list.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        for line in lines:
            line = line.split('|')
            if len(line) == 3:
                items.append({line[0]: int(line[1])})
                quantity.append(int(line[2][:-1]))
    except:
        print("관리자에게 연락하십시오.")


FileRead()
while True:
    try:
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
                        quantity[sel-1] -= 1
                        print("%s이/가 나왔습니다." % list(items[sel-1]).pop())
                        FileWrite()
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

            if sel == 1:
                items.append({input("추가할 물품을/를 입력하세요: "): int(input("추가할 가격을/를 입력하세요: "))})
                try:
                    quantity.append(int(input("추가할 개수을/를 입력하세요: ")))
                except:
                    print("잘못된 개수를 입력하여 0개로 입력되었습니다.")
                    quantity.append(0)
            elif sel == 6:
                print("자판기 모드로 돌아갑니다.")
                mode = 0
                continue
            elif sel in (2, 3, 4, 5):
                print("")
                for i in items:
                    for coffee in i:
                        print("%d. %s(%s원) 개수: %d" % (items.index(i) + 1, coffee, i[coffee], quantity[items.index(i)]))

            if sel == 5:
                sel = int(input("개수를 추가할 물품을 선택하세요: "))
                quantity[sel-1] += int(input("추가할 개수를 입력해주세요: "))
            elif sel == 2:
                sel = int(input("변경할 물품을 선택해주세요: "))
                if sel in range(1, len(items)+1):
                    print("%s을/를 선택하셨습니다." % list(items[sel-1]).pop())
                    name = input("물품 이름 변경 (값 미입력시, 변경하지 않음): ")
                    prc = input("물품 가격 변경 (값 미입력시, 변경하지 않음): ")
                    if name != "":
                        items[sel-1] = {name: items[sel-1][list(items[sel-1]).pop()]}
                    if prc != "":
                        items[sel-1][list(items[sel-1]).pop()] = int(prc)
            elif sel == 3:
                sel = int(input("삭제할 물품을 선택해주세요: "))
                if sel in range(1, len(items)+1):
                    print("%s이/가 삭제되었습니다." % list(items[sel-1]).pop())
                    del items[sel-1]
                    del quantity[sel-1]
            FileWrite()
    except:
        print("올바른 값을 입력해주세요.")
        continue
print("프로그램을 종료합니다.")
