height = float(input("본인의 키를 입력하세요.(m): "))
weight = float(input("본인의 몸무게를 입력하세요.(kg): "))
bmi = float(weight / height**2)
if bmi < 18.5:
    print("저체중")
elif bmi < 23:
    print("정상")
elif bmi < 25:
    print("과체중")
elif bmi < 30:
    print("경도비만")
elif bmi < 35:
    print("중증도 비만")
else:
    print("고도 비만")
