money = int(input("돈을 넣어주세요"))
print("1. 블랙 커피 100원")
print("2. 밀크 커피 150원")
print("3. 고급 커피 200원")
print("4. 거스름돈")
print("넣은 돈: %d원" % money)
but = int(input("뽑을 물품을 골라주세요"))

if but == 1:
    price = money-100
	print("선택한 물품이 나왔습니다.")
    print("잔돈을 반환합니다: %d원" % price)
elif but == 2:
	price = money-150
    print("선택한 물품이 나왔습니다")
    print("잔돈을 반환합니다: %d원" % price)
elif but == 3:
	price = money-200
    print("물품번호를 잘못입력하셨습니다")
    print("돈을 반환합니다: %d원" % price)
elif but = 4:
    print("돈을 반환합니다: %d원" % money)
else:
    print("물품번호를 잘못입력하셨습니다")
    print("돈을 반환합니다: %d원" % money)
	
