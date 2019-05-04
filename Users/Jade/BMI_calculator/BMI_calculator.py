# BMI 계산기
# BMI = weight/height^2

# 리스트 생성
status = ["저체중", "정상", "과체중", "경도비만", "중증도 비만", "고도 비만"]

# 키, 몸무게 입력
height = (float)(input("본인의 키를 입력하세요.(m): "))
weight = (float)(input("본인의 몸무게를 입력하세요.(kg): "))

# BMI 수치 계산 (절댓값)
BMI = abs(weight / (height ** 2))

# 계산
if BMI < 18.5:  # BMI < 18.5
	status = status[0]
else:
	if BMI < 23:  # 18.5 < BMI < 23
		status = status[1]
	else:
		if BMI < 25:  # 23 < BMI < 25
			status = status[2]
		else:
			if BMI < 30:  # 25 < BMI < 30
				status = status[3]
			else:
				if BMI < 35:  # 30 < BMI < 35
					status = status[4]
				else:  # BMI >= 35
					status = status[5]
			
# 출력
print("%s" % status)

# 빨간줄이 그어지는 이유는, 인덴팅이 tap으로 되어있기 때문입니다.
# 구름IDE->기본설정->에디터(기본탭)->인덴팅에서 인덴트 단위를 스페이스로 해주시면 됩니다.
# if else구문을 if~ elif고 고치시는게 보기 좋습니다. 너무 if문이 깊게 들어가면 가독성이 떨어집니다.
# ex)
# if BMI < 18.5:  # BMI < 18.5
#     status = status[0]
# else:
#     if BMI < 23:  # 18.5 < BMI < 23
#        status = status[1]
# =>
# if BMI < 18.5:
#     status = status[0]
# elif BMI < 23:
#     status = status[1]
#
# 인라인 주석(구문 뒤에 주석이 들어가는 것)은 피하시는게 좋습니다.
# python에서 대문자로 된 변수는 상수로 하도록 코딩컨밴션이 되어 있기 때문에 변수명은 소문자로 하시는 것이 좋습니다.
# 수고하셨습니다.
# 주강사 김재형
