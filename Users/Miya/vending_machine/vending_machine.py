inp = int(input("돈을 넣으세요:"))
menu = ['블랙커피', '밀크커피', '고급커피']
price = [100, 150, 200]
cnt = 0
tmp = 0
for i in menu:
    cnt += 1
    print("{0}. {1}({2}원)".format(cnt, i, price[cnt-1]))
print("4. 거스름돈\n넣은 돈: %d원" % inp)
sel = int(input("뽑을 물품을 골라주세요:"))
if sel in (1, 2, 3):
    if inp >= price[sel-1]:
        print("%s이/가 나왔습니다." % menu[sel-1])
        tmp = price[sel-1]
    else:
        print("돈이 부족합니다.")
elif sel != 4:
    print("물품번호를 잘못 입력하셨습니다.")
print("돈을 반환합니다.: %d원" % (inp-tmp))
