item_list = [['블랙커피', 100], ['밀크커피', 150], ['고급커피', 200]]
control_list = ["돈입력", "거스름돈"]

input_money = int(input("돈을 넣어주세요: "))
plus_money = 0
while True:
    # 이번에는 이 부분을 수정하도록 하겠습니다.
    # 현재, item_list에 값이 추가된다 하더라도, 값이 자동으로 추가되지 않습니다.
    # 이는 프로그램의 유연성이 부족하기 때문입니다.
    # 따라서 자동으로 추가되게 하기 위해서 for과 enumerate()를 사용하여,
    # item_list에 값이 추가되면 자동으로 추가되도록 만들것입니다.
    # 19번 ppt를 참고하시면 좋겠습니다.
    # for 변수명1, 변수명2 in enumerate(item_list):
    #    print(변수명1, 변수명2)
    # 이를 해보시면 0 ['블랙커피', 100], 1 ['밀크커피', 150] ...
    # 가 나타나는 것을 볼 수 있습니다.
    # 이는 enumerate가 인덱스, 요소를 반환하기 때문입니다.
    # 따라서 인덱스가 1로 수정되게 만들고, 요소로 반환된 리스트 각각을 참조하면
    # print("1. 블랙커피(100원)")과 같게 만들 수 있습니다.
    # 이에 대해서 한 번 생각해보시고, 해결해보시기 바랍니다.
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

# 현재, select_value에 문자열을 받으면 오류가 발생합니다.
# 그 이유는 select_value에서 int()를 통해서 바로 정수로 변환하기 때문입니다.
# 따라서 int로 바로 변환하지 않고, select_value로 문자열을 받은 이후, select_value가 admin인지 확인합니다.
# admin이 아니라면, 현재는 정수만 받도록 되어 있기 때문에 정수로 변환해 줍니다.
# 이때, 한 번 admin이 들어왔다면 admin에서 빠져나갈 때, select_value를 초기화해줍니다.
# 남은 값("admin")으로 인해 오류가 발생하기 때문입니다.
# 이러한 점을 해결하기 위해 함수를 사용합니다만, 이는 나중에 천천히 지도해드리겠습니다.

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

# 대청소의 날 등 이것저것 있어서 좀 늦게 접속했습니다. 죄송합니다.
# 너무 피곤해서 좀 쉴 필요가 있었네요 ;;
# 주강사 김재형
