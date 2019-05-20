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

# 잘 해결하셨으나, 과제가 3번째 과제입니다.
# 현재 8줄 if부터 24줄까지 보면, 똑같은 내용이 반복하고 있는 것을 볼 수 있습니다.
# coffee를 1일때, 2일때, 3일때, 4일때를 전부 비교하고 있기 때문입니다.
# 리스트나 튜플, 딕셔너리를 사용하면 1-3을 전부 모아서 하나의 elif문으로 사용할 수 있습니다.
# 8번째 줄의 coffee > 3으로 인해 26번줄이 실행되지 않습니다.
# 따라서 if의 맨 앞보다는 마지막에 else를 사용해서 알려진 값이 아니면 전부 잘못 입력했다는 값을 표현할 수 있습니다.
# 수고하셨습니다. 주강사 김재형
