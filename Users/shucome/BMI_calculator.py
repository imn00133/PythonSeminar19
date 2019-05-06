BMi_type = ['저체중', '정상', '과체중', '경도비만', '중증도비만', '고도비만']

weight = float(input("본인의 몸무게를 입력하세요(KG) : "))
height = float(input("본인의 키를 입력하세요(M) : "))
BMi_value = weight/(height**2)
if BMi_value < 18.5:
    print("%s" % BMi_type[0])
elif BMi_value < 23:
    print("%s" % BMi_type[1])
elif BMi_value < 25:
    print("%s" % BMi_type[2])
elif BMi_value < 30:
    print("%s" % BMi_type[3])
elif BMi_value < 35:
    print("%s" % BMi_type[4])
elif BMi_value >= 35:
    print("%s" % BMi_type[5])
