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

# 프로그램이 돌아가지 않습니다.
# 이 프로그램에는 다음과 같은 문제가 있습니다.
# 1. 3-6번째 줄은 사용하실 수 없는 문장입니다. 변수명을 짓는 규칙은 다음과 같습니다.
#    1) 영문자(대, 소문자 구분), 숫자, 언더바(_)를 사용할 수 있다.
#    2) 첫 자리에는 숫자를 사용할 수 없다.
#    3) 파이썬 키워드는 변수 명으로 사용할 수 없다.
# 따라서 3-6번째 줄을 어떤 번호에 뭐가 있었는지 확인하려고 하셨다면, 주석처리를 하셔야 됩니다.
# 2. 텝과 공백4칸이 혼합되어 있습니다. 구름IDE에서 탭을 눌렀을 때, 공백4칸이 되지 않는다면
# 구름IDE->기본설정->에디터(기본탭)->인덴팅에서 인덴트 단위를 스페이스로 해주시면 됩니다.
# 제가 이 부분은 수정해드렸습니다.
#
# 빨간줄이 쳐지는 이유는 % 뒤에 공백이 없어서입니다.
# 예를 들어 7번째줄 print("넣은돈: (%d)" %money)부분은
# print("넣은돈: (%d)" % money)로 (%뒤에 공백을 넣음)으로 고쳐주시면 됩니다.
#
# 물품이 추가/제거되거나, 가격이 변경될 경우에 코드를 전부 뜯어고쳐야 됩니다.
# 이런 것을 최대한 유연하게 하기 위한 프로그래밍을 하시는 것이 좋을 수 있습니다.
# 이에 대해서는 수업시간에 설명해드리도록 하겠습니다.
# 그 외에 알고리즘에는 문제점이 없습니다. 수고하셨습니다.
# - 주강사 김재형
