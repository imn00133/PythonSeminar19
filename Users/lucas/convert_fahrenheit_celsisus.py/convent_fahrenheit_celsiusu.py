F=float(input("변화할 화씨온도를 입력하시오"))

C=(F-32)*5/9

print("%0.2f℉는 %0.2f℃입니다"%(F,C))

# 위의 코드에서 빨간줄이 그어지는 이유는 다음과 같습니다.
# 1. '='(할당 연산자) 앞 뒤에는 띄어쓰기를 해주시는 것이 좋습니다.
# 2. ',' 뒤에는 띄어쓰기를 해주시는 것이 좋습니다.
# 3. 파일에서 코드가 끝날 때는 마지막 줄이 비어있도록 엔터를 넣어주는 것이 좋습니다.
# 각 줄마다 엔터를 치셨는데, 흐름이 연결되는 코드일 경우 엔터를 치지 않으시는 것이 코드를 읽기 쉽습니다.
# 이번 과제는 간단하여 F나 C같은 변수를 사용하셨습니다.
# 하지만, 과제의 내용이 길어지는 것을 대비해서 변수명을 좀 더 알기 쉽게 해주시는 것이 좋습니다.
# - 김재형
