# 물품에 대한 모든 값
object_aLL = [['블랙커피', 100, 1], ['밀크커피', 150, 1], ['고급커피', 200, 1]]

# 제품명 외 자판기의 기능
controL = [['돈입력', '거스름돈'], ['물품추가', '물품변경', '물품삭제', '물품출력', '종료']] 

# 사용자가 볼 수있는 메뉴의 수
menu_size = [0, 1, 2]

# 사용자가 조작 할 수 있는 메뉴의 수
controL_money_size = [0, 1]

# 관리자가 조작하는 메뉴의 수
controL_object_size = [0, 1, 2, 3, 4]

# 사용자 메뉴에서 5번을 눌렀을때 작동하기 위한 값
receipt = 4

# 사용자가 돈을 추가로 넣을때 쓰는 값
pLuse_money = 3

# admin 계정을 입력시 메뉴를 계속해서 출력하기 위한 조건
controL_end = 1

# 사용자 메뉴값
object_name = 0
object_price = 1
object_count = 2
# 물건값의 최소값
min_price = 100

# 관리자 메뉴 값
admin_menu_1 = 1
admin_menu_2 = 2
admin_menu_3 = 3
admin_menu_4 = 4
admin_menu_end = 5

inputmoney = int(input("돈을 넣어주세요 : "))
print()

while True:
    # 사용자 메뉴명을 뽑는다
    for i in menu_size:
        print("%d. %s(%d원)" % (i+1, object_aLL[i][object_name], object_aLL[i][object_price]))
    for j in controL_money_size:
        print("%d. %s" % (j+4, controL[0][j]))
    print("현재까지 넣은 금액은 : %d" % inputmoney)

    seLect_object = input("뽑을 물건을 골라주세요 : ")
    print()

    if seLect_object == "admin":
        while controL_end == 1:
            print("관리자 메뉴")
            # 관리자 메뉴를 출력
            for i in controL_object_size:
                print("%d. %s" % (i+1, controL[1][i]))
            controL_menu = (int(input("원하는 작업을 선택해주세요 : ")))
            print()

            if controL_menu == admin_menu_1:
                # 물품을 추가
                pLuse_objcet = max(menu_size)+1
                menu_size.append(pLuse_objcet)
                name1 = input("추가할 물품을 입력하세요 : ")
                price1 = (int(input("추가할 가격을 입력하세요 : ")))
                count1 = (int(input("추가할 개수를 입력하세요 : ")))
                object_aLL.append([name1, price1, count1])
            elif controL_menu == admin_menu_2:
                # 물품을 변경
                for i in menu_size:
                    print("%d. %s(%d원) 개수: %d" % (i+1, object_aLL[i][object_name], object_aLL[i][object_price], object_aLL[i][object_count]))
                object_choice = (int(input("변경할 물품을 선택해주세요 : "))-1)
                name2 = input("물품 이름 변경(미입력시 변경하지 않음) : ")
                price2 = input("물품 가격 변경(미입력시 변경하지 않음) : ")
                count2 = input("물품 갯수 변경(미입력시 변경하지 않음) : ")
                # 입력을 안했는지 확인
                if name2 == '':
                    name2 = object_aLL[object_choice][object_name]
                if price2 == '':
                    price2 = object_aLL[object_choice][object_price]
                if count2 == '':
                    count2 = object_aLL[object_choice][object_count]
                # 미입력시 'str'로 저장되기 때문에 한번 'int'값으로 변경
                price2 = int(price2)
                count2 = int(count2)
                object_aLL[object_choice][object_name] = name2
                object_aLL[object_choice][object_price] = price2
                object_aLL[object_choice][object_count] = count2
                print()
            elif controL_menu == admin_menu_3:
                # 물품을 삭제
                print()
            elif controL_menu == admin_menu_4:
                # 물품을 출력
                for i in menu_size:
                    print("%d. %s(%d원) 개수: %d" % (i+1, object_aLL[i][object_name], object_aLL[i][object_price], object_aLL[i][object_count]))
                print()
            elif controL_menu == admin_menu_end:
                controL_end = 0
    else:
        seLect_object = (int(seLect_object)-1)

    if controL_end == 0:
        # 다시 어드민 메뉴를 불러올 경울 대비해 값을 초기화
        controL_end = 1
        continue
    elif seLect_object == pLuse_money:
        inputmoney += int(input("돈을 넣어주세요 : "))
        print()
    elif seLect_object == receipt:
        print("돈을 반환합니다 : %d \n" % inputmoney)
        break
    elif inputmoney < object_aLL[seLect_object][object_price]:
        print("돈이 부족합니다. 돈을 더 넣어주세요. \n")
    else:
        if object_aLL[seLect_object][object_count] > 0:
            # 입력한 돈의 값을 물건 값만큼 깍고 해당 물품의 재고를 수정
            inputmoney -= object_aLL[seLect_object][object_price]
            temp = object_aLL[seLect_object][object_count]
            temp -= 1
            object_aLL[seLect_object][object_count] = temp
        else:
            print("재고가 부족합니다. 관리자를 호출해주세요.")
            print()
            continue
        print("%s가 나왔습니다. \n" % object_aLL[seLect_object][object_name])
        print()

    if inputmoney < min_price:
        print("돈을 반환합니다 : %d \n" % inputmoney)
        inputmoney = 0
# 잘 해결하셨습니다.
# 주강사 김재형1
