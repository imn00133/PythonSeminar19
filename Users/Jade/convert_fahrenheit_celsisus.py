global fah, cel

fah = input("변환할 화씨온도(℉)를 입력하십시오: ")
cel = (float(fah) - 32) * 5/9
print("%0.2f℉는 %0.2f℃입니다." %(float(fah), float(cel)))
