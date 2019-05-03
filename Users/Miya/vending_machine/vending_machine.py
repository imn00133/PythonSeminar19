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

# 중간중간 엔터를 쳐서 흐름별로 나눠주는 것이 읽기에 편할 수 있습니다.
# 프로그램이 커진다면, 주석을 다는 것도 좋습니다.
# tmp변수를 사용하는 이유가 궁금합니다.
# in (1, 2, 3)을 사용한 것이 참신합니다. 다만, 프로그램의 유연성부분을 고려하는 것도 중요합니다.
# 주강사 김재형
