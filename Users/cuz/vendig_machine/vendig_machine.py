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
    # -->> 수정하였습니다. 하지만 돈 넣기와 거스름돈을 선택을 하면 자동으로 프로그램이 꺼지고맙니다.
    if 0 <= select_value < len(item_list) + len(control_list):
        if input_money >= item_list[select_value][1]:
            input_money = input_money - item_list[select_value][1]
            print("%s가 나왔습니다." % item_list[select_value][0])
        else:
            print("돈이 부족합니다")
    # 꺼지는 이유에 대해서 설명해드리겠습니다.
    # 현재, 이 부분에서 item_list와 control_list를 동시에 확인하고 있습니다.
    # 만일, 4를 입력했다고 하겠습니다.
    # 그렇다면, 다음과 같은 문제가 발생합니다. 4는 0 <= select_value < len~~에 포함됨으로
    # 이 수행문쪽으로 들어옵니다.
    # 그런데, item_list를 보면 index 4는 존재하지 않습니다.
    # 따라서 오류(out of index)가 나면서 오류가 발생하는 것입니다.
    # 이에 대한 해결이 43번째 주석입니다.
    # len(item_list)와 len(control_list)를 합쳐서 계산하는 것이 아닌,
    # len(item_list)를 조건으로 하는 if문 하나, control_list만 계산할 수 있는 elif하나를 만드셔야 합니다.
    else:
        print("물품번호를 잘못 입력하였습니다.")
    print("돈을 반환합니다.: %d" % input_money)
    elif select_value == 3:
        plus_money = int(input("돈을 더 넣어주세요: "))
        plus_money += input_money

# 지금 9번째 줄을 보시면, "4번에 돈 입력"이 있는 것을 볼 수 있습니다.
# 따라서 4를 입력했을 때(elif를 사용하여),
# input_money = int(input("돈을 넣어주세요: "))가 출력되도록 만들어주시면 됩니다.

# 15번째 줄 아래의 16~20번째 줄은 물품을 선택했을 때 출력하는 구간입니다.
# 따라서 15번째 줄과 21번을 if-else로 묶는 것 보다는
# if 물품을 선택하는 조건:
#    실행문
# elif 조작(돈입력, 거스름돈)을 선택하는 조건:
#    실행문
# else:
#    잘못 입력했을 때 물품번호를 잘못 입력했다를 알려주는 실행문
# 으로 구성해주시면 됩니다.
