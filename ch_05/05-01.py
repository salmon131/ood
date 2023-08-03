class Common:
    def discount_price(self, regular_price: int, discount_rate: float):
        if regular_price < 0:
            raise Exception("정상 가격은 0보다 작을 수 없습니다.")
        
        if discount_rate < 0.0:
            raise Exception("할인율은 0과 1 사이여야 합니다.")

class RegularPrice:
    def __init__(self, amount: int):
        if amount < 0:
            raise Exception("정상 가격은 0보다 작을 수 없습니다.")
        
        self.amount = amount


class DiscountRate:
    def __init__(self, rate: float):
        if rate < 0.0:
            raise Exception("할인율은 0과 1 사이여야 합니다.")
        
        self.rate = rate


class DiscountedPrice:
    def __init__(self, regular_price: RegularPrice, discount_rate: DiscountRate):
        self.amount = regular_price.amount * discount_rate.rate


if __name__ == "__main__":
    regular_price = RegularPrice(10000)
    discount_rate = DiscountRate(0.3)

    print(DiscountedPrice(regular_price, discount_rate).amount)

        
