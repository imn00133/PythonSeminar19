# 리스트 생성
coffee = ["아메리카노", "라떼", "프라푸치노"]
price = [100, 150, 200]

# 돈 입력
money = int(input("돈을 넣으세요: "))

# 비용(cost)을 입력한 돈의 값(money)으로 초기화
cost = money

print("1. %s(%d원)" % (coffee[0], price[0]))
print("2. %s(%d원)" % (coffee[1], price[1]))
print("3. %s(%d원)" % (coffee[2], price[2]))
print("4. 거스름돈")

# 넣은 돈 출력
print("넣은 돈: %d원" % money)

# 뽑기
choice = int(input("뽑을 물품을 골라주세요: "))
if choice == 1:  # 1번을 선택할 경우
	if money < price[0]:  # 돈이 부족할 경우
		print("돈이 부족합니다.")
	else:
		print("%s이/가 나왔습니다." % coffee[0])
		cost = money - price[0]
elif choice == 2:  # 2번을 선택할 경우
	if money < price[1]:  # 돈이 부족할 경우
		print("돈이 부족합니다.")
	else:
		print("%s이/가 나왔습니다." % coffee[1])
		cost = money - price[1]
elif choice == 3:  # 3번을 선택할 경우
	if money < price[2]:  # 돈이 부족할 경우
		print("돈이 부족합니다.")
	else:
		print("%s이/가 나왔습니다." % coffee[2]) 
		cost = money - price[2]
elif choice == 4:  # 돈을 반환할 경우
		cost = money - 0
else:  # 물품 번호를 잘못 입력할 경우
	    print("물품번호를 잘못 입력하셨습니다.")
	
print("돈을 반환합니다.: %d원" % cost)

