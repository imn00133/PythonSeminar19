#fahrenheit = 화씨
#ceLsius = 썹씨
fahrenheit = float(input("변환할 화씨온도(℉)릴 입력해주세요 : "))
ceLsius = (fahrenheit - 32.0) * 5.0 / 9.0
print("%0.2f℉는 %0.2f℃입니다." % (fahrenheit, ceLsius))

# PEP 8에 따르면, 주석(#)을 달 때는 # 다음에 한칸을 띄도록 되어있습니다.
# 또한, 마지막 줄에는 한 줄을 띄도록 되어있습니다.
# -김재형
