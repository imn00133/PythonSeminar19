inp = int(input("돈을 넣으세요:"))
menu = {'블랙커피': 100, '밀크커피': 150, '고급커피': 200}
cnt = 0
for i in menu:
    cnt += 1
    print("{0}. {1}({2}원)".format(cnt, i, menu[i]))
print("4. 거스름돈\n넣은 돈: %d원" % inp)
