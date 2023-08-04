class SellingPrice:
    SELLING_COMMISSION_RATE = 0.05
    DELIVERY_FREE_MIN = 20000
    SHOPPING_POINT_RATE = 0.01

    def __init__(self, amount: int):
        if amount < 0:
            raise Exception("가격은 0 이상이어야 합니다.")
        self.amount = amount

    def calc_selling_commission(self):
        return int(self.amount * SellingPrice.SELLING_COMMISSION_RATE)
    
    def calc_delivery_charge(self):
        return 0 if SellingPrice.DELIVERY_FREE_MIN <= self.amount else 5000
    
    def calc_shopping_point(self):
        return int(self.amount * SellingPrice.SHOPPING_POINT_RATE)


class SellingPriceV2:

    def __init__(self, amount: int):
        if amount < 0:
            raise Exception("가격은 0 이상이어야 합니다.")
        self.amount = amount


class SellingCommission:
    SELLING_COMMISSION_RATE = 0.05

    def __init__(self, selling_price: SellingPriceV2):
        self.amount = int(selling_price.amount * SellingCommission.SELLING_COMMISSION_RATE)
    

class DeliveryCharge:
    DELIVERY_FREE_MIN = 20000

    def __init__(self, selling_price: SellingPriceV2):
        self.amount = 0 if DeliveryCharge.DELIVERY_FREE_MIN <= selling_price.amount else 5000
    

class ShoppingPoint:
    SHOPPING_POINT_RATE = 0.01

    def __init__(self, selling_price: SellingPriceV2):
        self.amount =  int(selling_price.amount * ShoppingPoint.SHOPPING_POINT_RATE)


if __name__ == "__main__":
    selling_price = SellingPrice(5000)
    print("판매 수수료", SellingCommission(selling_price).amount)
    print("베송비", DeliveryCharge(selling_price).amount)
    print("쇼핑 포인트", ShoppingPoint(selling_price).amount)
