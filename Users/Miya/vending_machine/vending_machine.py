money = 0
menu = ['블랙커피', '밀크커피', '고급커피', '돈 입력', '거스름돈']
price = [100, 150, 200]
sel = 0

while sel >= 0:  # -1 값 입력전까지 반복
    for i in range(5):  # 메뉴 띄워주깅
        if i < 3:
            print("%d. %s(%d원)" % (i+1, menu[i], price[i]))
        else:
            print("%d. %s" % (i+1, menu[i]))

    print("현재까지 넣은 돈은 %d원입니다." % money)
    sel = int(input("뽑을 물품을 골라주세요: "))

    if sel in (1, 2, 3):  # 고른대로 기능 실행하깅
        if money >= price[sel-1]:
            money = money - price[sel-1]
            print("%s이/가 나왔습니다." % menu[sel-1])
            if money < price[0]:
                print("돈을 반환합니다: %d원" % money)
                money = 0
                break
        else:
            print("돈이 부족합니다. 돈을 더 넣어주세요.")
    elif sel == 4:
        money = int(input("돈을 넣으세요: "))
    elif sel == 5 or sel < 0:
        print("돈을 반환합니다: %d원" % money)
        money = 0
        break
    else:
        print("번호를 잘못 입력 하셨습니다.")
    print("\n")

print("프로그램을 종료합니다.")

# 빨간 줄은 다음과 같은 사유로 생성됩니다.
# 공백 대신에 탭이 사용되었습니다.
# 이는 구름IDE문제로 인해 인덴팅이 바뀐 것입니다.
# 구름IDE-기본설정-인덴팅에서 탭을 스페이스로 바꿔주시면 됩니다. => 감사합니다. 빨간줄 때문에 힘들었습니다. -_-
# 그 외 문법 오류입니다.
# 1. 11번째 줄에 괄호가 완료되지 않아 오류가 발생합니다. => ?!
# 2. 21, 23번줄에서 비교가 아닌 할당이 되고 있습니다. => 최근 한셀 스크립트 코딩만 하다보니 한셀과 착각했습니다. ㅠㅠ
# 주강사 김재형
