item_list = [['블랙커피', 100], ['밀크커피', 150], ['고급커피', 200]]
control_list = ["돈입력", "거스름돈"]

input_money = int(input("돈을 넣어주세요: "))
plus_money = 0
while True:
    print("1. 블랙커피(100원)")
    print("2. 밀크커피(150원)")
    print("3. 고급커피(200원)")
    print("4. 돈입력")
    print("5. 거스름돈")
    print("넣은돈: %d원" % input_money)
    select_value = int(input("뽑을 물품을 골라주세요: "))-1
    
    if select_value == "admin":
        print("1. 물품목록과 개수출력")
        print("2. 물품개수 변경")
        print("3. 종료")
# select_value 값에 admin을 입력하여 모드로 들어가려고합니다.
# 혹시 벨류값에 문자를 사용하여 값을 지정해줄수 있을까요?
    
    if 0 <= select_value < len(item_list):
        if input_money >= item_list[select_value][1]:
            input_money = input_money - item_list[select_value][1]
            print("%s가 나왔습니다." % item_list[select_value][0])
        else:
            print("돈이 부족합니다.")
    elif select_value == 3:
        plus_money = int(input("돈을 더 넣어주세요: "))
        input_money += plus_money
    elif select_value == 4:
        print("돈을 반환합니다.:%d원" % input_money)
    
    elif select_value == "admin":
        print("1. 물품목록과 개수출력")
        print("2. 물품개수 변경")
        print("3. 종료")
    else:
        print("물품번호를 잘못 입력하셨습니다.")

    # 이에 대한 해결이 43번째 주석입니다.
    # len(item_list)와 len(control_list)를 합쳐서 계산하는 것이 아닌,
    # len(item_list)를 조건으로 하는 if문 하나, control_list만 계산할 수 있는 elif하나를 만드셔야 합니다.
  
