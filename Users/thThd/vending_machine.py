money = int(input("돈을 넣으세요 : "))
print("1. 블랙커피(100원)")
print("2. 밀크커피(150원)")
print("3. 고급커피(200원)")
print("4. 거스름돈")
print("넣은 돈: (%d)" % money)
coffee = int(input("뽑을 물건을 골라주세요: "))
if coffee > 3:
    print("물품번호를 잘못 입력하셨습니다.")
    print("돈을 반환합니다. : %d원" % money)
elif coffee == 1:
    if money < 100:
        print("돈이 부족합니다.\n돈을 반환합니다. : %d원" % (money))
    else:
        print("블랙커피가 나왔습니다. \n돈을 반환합니다. : %d원" % (money-100))
elif coffee == 2:
    if money < 150:
        print("돈이 부족합니다. \n돈을 반환합니다. : %d원" % (money))
    else:
        print("밀크커피가 나왔습니다. \n돈을 반환합니다. : %d원" % (money-150))
elif coffee == 3:
    if money < 200:
        print("돈이 부족합니다. \n돈을 반환합니다. : %d원" % (money))
    else:
        print("고급커피가 나왔습니다. \n돈을 반환합니다. : %d원" % (money-200))
elif coffee == 4:
    print("\n돈을 반환합니다. : %d원" % (money))
    