height = float(input("본인의 키를 입력하세요.(m): "))
weight = float(input("본인의 몸무게를 입력하세요.(Kg): "))
BMI = float(weight / (height * height))
status_list = ['저체중', '정상', '과체중', '경도비만', '중증도비만', '고도비만']
if BMI < 18.5:
    print(status_list[0])
if 18.5 <= BMI < 23:
    print(status_list[1])
if 23 <= BMI < 25:
    print(status_list[2])
if 25 <= BMI < 30:
    print(status_list[3])
if 30 <= BMI < 35:
    print(status_list[4])
if 35 < BMI:
    print(status_list[5])
    