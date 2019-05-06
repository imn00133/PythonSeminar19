money = 0
menu = ['블랙커피', '밀크커피', '고급커피', '돈 입력', '거스름돈']
price = [100, 150, 200]
inp = 0

while inp >= 0:
	for i in range(4):
		if i < 3:
			print("%d. %s(%d원)" % (i+1, menu[i], price[i]))
		else:
			print("%d. %s" % (i+1, menu[i])
	print("현재까지 넣은 돈은 %d원입니다." % money)
	
	sel = int(input("뽑을 물품을 골라주세요: "))
	
	if sel in (1, 2, 3):
		if money >= price[inp-1]:
			print("%s이/가 나왔습니다." % menu[inp-1])
		else:
			print("돈이 부족합니다. 돈을 더 넣어주세요.")
	elif sel = 4:
		money = int(input("돈을 넣으세요: "))
	elif sel = 5:
		pass
	else:
		print("잘못 입력 하셨습니다.")
