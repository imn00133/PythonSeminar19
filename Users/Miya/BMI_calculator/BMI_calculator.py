height = float(input("본인의 키를 입력하세요.(m): "))
weight = int(input("본인의 몸무게를 입력하세요.(kg): "))
calc = float("%.1f" % (weight / pow(height, 2)))
if calc < 18.5:
    print("저체중")
elif calc < 23:
    print("정상")
elif calc < 25:
    print("과체중")
elif calc < 30:
    print("경도비만")
elif calc < 35:
    print("중증도 비만")
elif calc >= 35:
    print("고도 비만")
else:
    print("안알랴줌")

# 마지막에 cal >=35와 else를 따로 넣은 이유가 궁금합니다?
# 그 이외에는 잘 해결했습니다. 수고하셨습니다.
# 주강사 김재형
