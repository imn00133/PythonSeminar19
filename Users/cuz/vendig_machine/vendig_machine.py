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

# 4번 줄에 돈을 넣는 부분이 무한 루프 안에 있어 돈을 계속 넣고 있습니다. =>
# 이 부분에서 다시 처음 돈을 넣어주세요로 어떻게 전환할지 잘 모르겠네요 ㅠㅠ =>

# 지금 9번째 줄을 보시면, "4번에 돈 입력"이 있는 것을 볼 수 있습니다.
# 따라서 4를 입력했을 때(elif를 사용하여),
# input_money = int(input("돈을 넣어주세요: "))가 출력되도록 만들어주시면 됩니다.

# -->> 리스트를 만들었습니다. 그리고 돈입력과 거스름돈을 위해 select_value 값을 지정하려고 하였습니다.
# -->> 하지만 15번 줄부터 바로 select_value 값의 조건이 되지않아 오류가 뜨고맙니다.
# -->> 그래서 길이를 늘려주었습니다. 그 다음엔 16번 줄의 물건출력 및 돈감소가 오류가 뜹니다.
# -->> 다른 좋은 방법을 생각하기엔 시간이 너무 부족하네요. ㅠㅠ 다음에 다른 방법을 찾아야겠습니다.

# 현재 오류는 15번째 줄에 ":"이 빠져서 그렇습니다. select_value의 값의 오류와는 상관없는 문법 오류입니다.
# 실행시켰을 때, syntax error라고 뜨면, 이는 :이나 ", 들여쓰기등이 잘못되어서 생기는 오류가 생각하시면 됩니다.

# 15번째 줄 아래의 16~20번째 줄은 물품을 선택했을 때 출력하는 구간입니다.
# 따라서 15번째 줄과 21번을 if-else로 묶는 것 보다는
# if 물품을 선택하는 조건:
#    실행문
# elif 조작(돈입력, 거스름돈)을 선택하는 조건:
#    실행문
# else:
#    잘못 입력했을 때 물품번호를 잘못 입력했다를 알려주는 실행문
# 으로 구성해주시면 됩니다.
