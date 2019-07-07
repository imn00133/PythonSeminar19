class VendingMachine:
    # 자판기 초기화 과정
    # 데이터를 불러옵니다. (없으면 빈 자판기를 만듭니다.)
    def __init__(self, datafile=null):
        if datafile is null:
            # 데이터 없는 경우
            clear
        else:
            try:
                load(datafile)
            except FileNotFoundError:
                clear

    # 품목 관련 함수
    # 초기화(clear), 파일 로드(load)
    def clear:
        # 대충 음료수 아무 것도 없는 진열대 만드는 부분
        pass

    def load(filename):
        # 대충 파일에서 정보 뜯어오는 부분
        with open(filename) as f:
            pass


'''
음료수를 마셔야 합니다.
음료수 클래스는 가독성은 좋겠으나 메모리의 낭비와 쓸데없는 연산의 수행이 걱정됩니다.
'''


class Drink:
    def __init__(self, name):
        pass
