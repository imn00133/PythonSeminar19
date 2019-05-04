input_money = int(input("돈을 넣어주세요: "))
print("1. 블랙커피(100원)")
print("2. 밀크커피(150원)")
print("3. 고급커피(200원)")
print("4. 거스름돈")
print("넣은돈: %d원" % input_money)

item_list = [['블랙커피', 100], ['밀크커피', 150], ['고급커피', 200], ['거스름돈', None]]

select_value = int(input("뽑을 물품을 골라주세요: "))-1
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

# 그런데 select_value = int(input("뽑을 물품을 골라주세요: "))-1 에서 -1이 왜 붙는지 잘 모르겠습니다.
# 리스트의 맨뒤의것을 말하는건가요?
# => list는 0부터 시작합니다. 그런데 입력받은 값은 1부터 시작하네요!
# => 따라서 이를 맞추기 위해 -1을 한 것입니다.
#     => 맞추기 위해서는 +1이 되야 0에서 시작이 아니라 1에서 시작이 가능한게 아닌가요??
#         => 사람이 블랙커피를 뽑고싶어서 입력한 값은 1입니다. 그런데 item_list의 블랙커피는 어떤 인덱스를 가지고 있나요?
# 아하 이해했습니다. 그렇다면 select_value = int(input("뽑을 물품을 골라주세요: "))-1 이 맞는 표현이군요
# 예 그렇습니다.

# 혹시 if 0 <= select_value <len(item_list): 에 :의 의미나 이유를 알수있을까요?
# 모든 if 문의 끝에 들어가는것 같습니다.
# 그리고  if select_value != len(item_list)-1: 이 문장을 잘 이해하지 못하고있습니다.ㅠ

# :은 if문이 시작된다는 것을 알려주는 문법입니다. 항상 사용한다 보시면 됩니다
# if 0<= select_value < len(item_list)와 같은지 확인하였습니다.
# 따라서 이 부분에는 거스름돈이 포함되어 들어갑니다.
# (len(item_list)가 반환하는 값은 리스트 내 요소 개수임으로, index보다 1이 큽니다.)
# (지금 리스트를 보면 list내의 요소의 개수는 3, 마지막 요소의 인덱스는 2입니다.)
# if select_value != len(item_list)-1은 len(itme_list)-1이 거스름돈임으로,
# 거스름돈이 아닌 것을 선택하면 물품의 가격을 계산하도록 짜여져 있습니다.
# 사실 이렇게 꾸민 이유는 프로그램을 종료하기 전에 항상 돈을 반환하도록 작성하고,
# 반환하는 문장을 반복하지 않으려고 if문이 중첩되어 있습니다.
# if ~ elif ~ else 문을 사용하는 것이 보기 더 좋을 수 있습니다.
