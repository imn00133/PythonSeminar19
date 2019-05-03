money = int(input("돈을 넣으세요 : "))
print("1. 블랙커피(100원)")
print("2. 밀크커피(150원)")
print("3. 고급커피(200원)")
print("4. 거스름돈")
print("넣은 돈: %d원" % (money))
buy = int(input("뽑을 물품을 골라주세요 : "))
if buy == 1:
    if money < 100:
        print("돈이 부족합니다.\n돈을 반환합니다. : %d원" % (money))
    else:
        print("블랙커피가 나왔습니다.\n돈을 반환합니다. : %d원" % (money-100))
elif buy == 2:
    if money < 150:
        print("돈이 부족합니다.\n돈을 반환합니다. : %d원" % (money))
    else:
        print("밀크커피가 나왔습니다.\n돈을 반환합니다. : %d원" % (money-150))
elif buy == 3:
    if money < 200:
        print("돈이 부족합니다.\n돈을 반환합니다. : %d원" % (money))
    else:
        print("고급커피가 나왔습니다.\n돈을 반환합니다. : %d원" % (money-200))
elif buy == 4:
    print("돈을 반환합니다. : %d원" % (money))
else:
    print("물품 번호를 잘못 입력하셨습니다.\n돈을 반환합니다. : %d원" % (money))
# 맨 마지막 줄의 빨간줄은 맨 마지막 괄호에 띄어쓰기가 있기 때문입니다
# -김재형
