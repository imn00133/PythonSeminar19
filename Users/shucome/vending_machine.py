object_price = [100, 150, 200]
object_name = ['블랙커피', '밀크커피', '고급커피']

inputmoney = int(input("돈을 넣어주세요 : "))
print("1. 블랙커피(100원)")
print("2. 밀크커피(150원)")
print("3. 고급커피(200원)")
print("4. 거스름돈 ")
print("넣은 돈 : %d" % inputmoney)

# 리스트는 0부터 시작하기때문에 입력값의 -1을 해줘야한다.
seLect_object = (int(input("뽑을 물건을 골라주세요 : "))-1)
if seLect_object > 3:
    print("물품번호를 잘못 입력하였습니다.")
    print("돈을 반환합니다 : %d" % inputmoney)
elif seLect_object == 3:
    print("돈을 반환합니다 : %d" % inputmoney)
elif inputmoney < object_price[seLect_object]:
    print("돈이 부족합니다.")
    print("돈을 반환합니다 : %d" % inputmoney)
else:
    inputmoney = inputmoney - object_price[seLect_object]
    print("%s가 나왔습니다." % object_name[seLect_object])
    print("돈을 반환합니다 : %d" % inputmoney)


# 잘 해결하셨습니다.
# 주강사 김재형
