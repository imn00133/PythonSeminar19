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
