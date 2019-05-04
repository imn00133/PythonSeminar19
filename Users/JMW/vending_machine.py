money = int(input("돈을 넣으세요: "))
print("1. 밀키스(100원)", "2. 알로에(150원)", "3. 트레비(200원)", "4. 거스름돈", sep='\n')
1 = 밀키스
2 = 알로에
3 = 트레비
4 = 거스름돈
print("넣은돈: (%d)" %money)
item = input("뽑을 물품을 골라주세요: ")
if item == 1:
	if money < 100:
		print("돈이 부족합니다.")
		print("돈을 반환합니다.: %d" %money)
	elif money >= 100:
		print("%s이/가 나왔습니다." %item)
        print("돈을 반환합니다.: %d" %(money-100))
if item ==2:
	if money < 150:
		print("돈이 부족합니다.")
		print("돈을 반환합니다.: %d" %money)
	elif money >= 150:
		print("%s이/가 나왔습니다." %item)
        print("돈을 반환합니다.: %d" %(money-150))
if item ==3:
	if money < 200:
		print("돈이 부족합니다.")
		print("돈을 반환합니다.: %d" %money)
	elif money >= 200:
		print("%s이/가 나왔습니다." %item)
        print("돈을 반환합니다.: %d" %(money-200))
	
elif item == 4:
	print("돈을 반환합니다.: %d" %money)


else:
    print("물품번호를 잘못 입력하셨습니다.")
	print("돈을 반환합니다.: %d" %money)

# 1. %연산자 앞 뒤에 띄어쓰기가 없습니다.
# 2. 3번 줄 끝에 띄어쓰기가 있기 때문입니다.
# -김재형
