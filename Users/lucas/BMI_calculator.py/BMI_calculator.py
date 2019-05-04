hei = float(input("키를 입력하세오(m)"))
wei = float(input("몸무게를 입력하시오(kg)"))
bmi = wei/hei*hei
if 18.5 > bmi:
    print("저체중")
elif 23 >= bmi:
    print("정상")
elif 25 >= bmi:
    print("과체중")
elif 30 >= bmi:
    print("경도비만")
elif 35 >= bmi:
    print("중증도 비만")
else:
    print("고도 비만")

# 잘 해결하셨습니다.
# 주강사 김재형
