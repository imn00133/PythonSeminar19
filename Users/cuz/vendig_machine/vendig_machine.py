item_list = [['블랙커피', 100], ['밀크커피', 150], ['고급커피', 200], ['거스름돈', None]]

while True:
    input_money = int(input("돈을 넣어주세요: "))
    print("1. 블랙커피(100원)")
    print("2. 밀크커피(150원)")
    print("3. 고급커피(200원)")
    print("4. 거스름돈")
    print("넣은돈: %d원" % input_money)
    select_value = int(input("뽑을 물품을 골라주세요: "))-1
    if select_value < 0:
        break
    if 0 <= select_value < len(item_list):
        if select_value != len(item_list)-1:
            if input_money >= item_list[select_value][1]:
                input_money = input_money - item_list[select_value][1]
                print("%s가 나왔습니다." % item_list[select_value][0])
            else:
                print("돈이 부족합니다")
    else:
        print("물품번호를 잘못 입력하였습니다.")
    print("돈을 반환합니다.: %d" % input_money)
