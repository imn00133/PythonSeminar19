a = float(input("변환할 화씨온도(℉)를 입력하십시오: "))
b = (a-32)*(5/9)
print("%.2f℉는 %.2f℃입니다."%(a, b))

# 마지막 줄에 빨간 줄이 그어지는 이유는
# 1. %연산자 앞 뒤에 띄어쓰기가 없습니다.
# 2. 코드가 끝나는 마지막 줄 다음에 하나의 엔터가 있어야 합니다.
# 이번에는 코드가 짧아서 변수명을 고려하지 않아도 좋지만, 코드가 길어질 경우 a, b로 변수명을 놓는 것은 좋지 않습니다.
# -김재형
