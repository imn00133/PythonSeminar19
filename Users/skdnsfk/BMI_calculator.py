height = float(input("본인의 키를 입력하세요(m) : "))
weight = float(input("본인의 몸무게를 입력하세요(kg) : "))
BMI = (weight/height)**2
if BMI < 18.5:
    print("저체중")
elif BMI <= 23:
    print("정상")
elif BMI <= 25:
    print("과체중")
elif BMI <= 30:
    print("경도비만")
elif BMI <= 35:
    print("중증도 비만")
else:
    print("고도비만")

# BMI 계산식에 문제가 있습니다. 몸무게/(키)^2입니다.
# 변수명은 보통 소문자로 사용합니다. PEP8에서는 상수를 대문자로 사용하도록 되어있습니다.
# 따라서 다른 사람이 읽었을 때, 단어가 대문자일 경우 상수로 오인될 가능성이 있습니다.
# 그 외에 나머지는 잘 하셨습니다. 수고하셨습니다.
# 주강사 김재형
