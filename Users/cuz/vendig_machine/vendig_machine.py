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

# 오류가 나는 이유는 맨 마지막에 필요하지 않은 pass가 적혀있었기 때문입니다.
# 삭제하여서 정상실행이 가능합니다.

# 잘 만드셨으나, 문제점이 하나 있습니다.
# 4번 줄에 돈을 넣는 부분이 무한 루프 안에 있어 돈을 계속 넣고 있습니다.
# 따라서 이 부분이 무한루프(while True) 밖으로 간다면, 계속 돈을 넣지 않아도 됩니다.

# 생각해봐야 되는 부분은 다음과 같습니다.
# 이제 자판기를 제어해야 되는 상황이 있습니다. (4. 돈입력, 5. 거스름돈)
# 이를 item_list에 넣고 계산하려고 13번 째 줄에서 문제가 발생할 수 있습니다.
# (4나 5를 눌렀는데, 돈입력가 나왔습니다. 가 되면 문제가 발생)
# 따라서 목록을 두 개로 만드는 것이 좋을 것 같습니다.
# control_list = ["돈입력", "거스름돈"]
# 이렇게 list가 두 개가 되면 지금 사용하는 13번째 줄을 그냥 사용하셔도 됩니다.

# 이후에도 생각해봐야되는 부분이 있습니다.
# 하지만, 너무 많은 부분을 한 번에 설명드리면 어렵게 느끼실 것 같아서, 일단 이 정도만 생각해보시길 추천드립니다
# 다음 설명은 계속 해드리겠습니다.

# 여러번 접속했는데 바뀐 부분이 없는 걸 보니 바쁘신가 보군요.
# 수정해야 되는 부분은 상위 주석들입니다.
# 이해가 안되시면 연락주시거나 주석 남겨주세요!
# 주강사 김재형
