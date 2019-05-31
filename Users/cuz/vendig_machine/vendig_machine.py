item_list = [['블랙커피', 100], ['밀크커피', 150], ['고급커피', 200]]
control_list = ["돈입력", "거스름돈"]

input_money = int(input("돈을 넣어주세요: "))
while True:
    print("1. 블랙커피(100원)")
    print("2. 밀크커피(150원)")
    print("3. 고급커피(200원)")
    print("4. 돈입력")
    print("5. 거스름돈")
    print("넣은돈: %d원" % input_money)
    select_value = int(input("뽑을 물품을 골라주세요: "))-1
    if select_value < 0:
        break
    if 0 <= select_value < len(item_list)+len(control_list)
        if input_money >= item_list[select_value][1]:
            input_money = input_money - item_list[select_value][1]
            print("%s가 나왔습니다." % item_list[select_value][0])
        else:
            print("돈이 부족합니다")
    else:
        print("물품번호를 잘못 입력하였습니다.")
    print("돈을 반환합니다.: %d" % input_money)
    if select_value == 3:
        plus_money = int(input("돈을 더 넣어주세요: "))
    

# 잘 만드셨으나, 문제점이 하나 있습니다.
# 4번 줄에 돈을 넣는 부분이 무한 루프 안에 있어 돈을 계속 넣고 있습니다.
# 따라서 이 부분이 무한루프(while True) 밖으로 간다면, 계속 돈을 넣지 않아도 됩니다. -->
# 이 부분에서 다시 처음 돈을 넣어주세요로 어떻게 전환할지 잘 모르겠네요 ㅠㅠ

# 생각해봐야 되는 부분은 다음과 같습니다.
# 이제 자판기를 제어해야 되는 상황이 있습니다. (4. 돈입력, 5. 거스름돈)
# 이를 item_list에 넣고 계산하려고 13번 째 줄에서 문제가 발생할 수 있습니다.
# (4나 5를 눌렀는데, 돈입력가 나왔습니다. 가 되면 문제가 발생)
# 따라서 목록을 두 개로 만드는 것이 좋을 것 같습니다.
# control_list = ["돈입력", "거스름돈"]
# 이렇게 list가 두 개가 되면 지금 사용하는 13번째 줄을 그냥 사용하셔도 됩니다.
# -->> 리스트를 만들었습니다. 그리고 돈입력과 거스름돈을 위해 select_value 값을 지정하려고 하였습니다.
# -->> 하지만 15번 줄부터 바로 select_value 값의 조건이 되지않아 오류가 뜨고맙니다.
# -->> 그래서 길이를 늘려주었습니다. 그 다음엔 16번 줄의 물건출력 및 돈감소가 오류가 뜹니다.
# -->> 다른 좋은 방법을 생각하기엔 시간이 너무 부족하네요. ㅠㅠ 다음에 다른 방법을 찾아야겠습니다.