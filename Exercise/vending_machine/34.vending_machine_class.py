class Menu:
    def __init__(self):
        pass

    def create_list(self):
        pass

    def print_list(self):
        pass

    def return_item(self, item_num):
        pass


class Beverage:
    def __init__(self):
        pass

    def return_price(self):
        pass


class Cash:
    def __init__(self):
        pass

    def add_cash(self, money):
        pass

    def sub_cash(self, price):
        pass

    def print_cash(self):
        pass

    def return_cash(self):
        pass


class VendingMachine:
    def __init__(self):
        self.cash_bucket = Cash(0)

    def control_cash(self, string, money=0):
        if string == "add":
            self.cash_bucket.add_cash(money)
        elif string == "print":
            self.cash_bucket.print_cash()
        elif string == "return":
            self.cash_bucket.return_cash()
        else:
            print("잘못된 입력입니다.")

    def print_itemlist(self, Menu):
        Menu.print_list()

    def return_item(self, Menu, item_num):
        item = Menu.retun_item(item_num)
        item_value = item.return_price()
        if self.cash_bucket.sub_cash(item_value):
            print("%s가 나왔습니다." % item.name)
        else:
            print("금액이 부족합니다.")


def main():
    pass


if __name__ == "__main__":
    main()
