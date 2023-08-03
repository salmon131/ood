import typing as t


class Product:
    def __init__(self, id: int, name: str, price: "RegularPrice"):
        if id < 0:
            raise Exception("Invalid product id")
        if name  == "":
            raise Exception("Invalid product name")
        
        self.id = id
        self.name = name
        self.price = price


class ProductDiscount:
    def __init__(self, id: int, can_discount: bool):
        self.id = id
        self.can_discount = can_discount


class RegularPrice:
    MIN_AMOUNT = 0

    def __init__(self, amount: int):
        if amount < RegularPrice.MIN_AMOUNT:
            raise Exception("Invalid amount")
        self.amount = amount


class RegularDiscountedPrice:
    MIN_AMOUNT = 0
    DISCOUNT_AMOUNT = 4000

    def __init__(self, price: RegularPrice):
        discount_amount = price.amount - RegularDiscountedPrice.DISCOUNT_AMOUNT
        if discount_amount < RegularDiscountedPrice.MIN_AMOUNT:
            discount_amount = RegularDiscountedPrice.MIN_AMOUNT

        self.amount = discount_amount


class SummerDiscountedPrice:
    MIN_AMOUNT = 0
    DISCOUNT_AMOUNT = 3000

    def __init__(self, price: RegularPrice):
        discount_amount = price.amount - SummerDiscountedPrice.DISCOUNT_AMOUNT
        if discount_amount < SummerDiscountedPrice.MIN_AMOUNT:
            discount_amount = SummerDiscountedPrice.MIN_AMOUNT

        self.amount = discount_amount


class DiscountManager:

    discount_products: t.List[Product] = []
    total_price = 0

    def add(self, product: Product, product_discount: ProductDiscount):
        if product.id != product_discount.id:
            raise Exception("Invalid product id")
        discount_price = RegularDiscountedPrice(product.price).amount
        
        tmp = 0
        if product_discount.can_discount:
            tmp = DiscountManager.total_price + discount_price
        else:
            tmp = DiscountManager.total_price + product.price

        if tmp <= 200000:
            DiscountManager.total_price = tmp
            DiscountManager.discount_products.append(product)
            return True
        else:
            return False
        

class SummerDiscountManager:
    
    discount_products: t.List[Product] = []
    total_price = 0

    def add(self, product: Product, product_discount: ProductDiscount):
        if product.id < 0:
            raise Exception("Invalid product id")
        if product.name  == "":
            raise Exception("Invalid product name")
        discount_price = SummerDiscountedPrice(product.price).amount

        if product_discount.can_discount:
            tmp = SummerDiscountManager.total_price + discount_price
        else:
            tmp = SummerDiscountManager.total_price + product.price

        if tmp <= 300000:
            SummerDiscountManager.total_price = tmp
            SummerDiscountManager.discount_products.append(product)
            return True
        else:
            return False


if __name__ == "__main__":
    product1 = Product(1, "test1", RegularPrice(10000))
    product2 = Product(2, "test2", RegularPrice(20000))
    product3 = Product(3, "test3", RegularPrice(30000))

    product_discount1 = ProductDiscount(1, True)
    product_discount2 = ProductDiscount(2, True)
    product_discount3 = ProductDiscount(3, True)

    discount_manager = DiscountManager()
    summer_discount_manager = SummerDiscountManager()

    print("test1", discount_manager.add(product1, product_discount1))
    print("test2", discount_manager.add(product2, product_discount2))
    print("test3", discount_manager.add(product3, product_discount3))
    
    print("총 상품 할인가격: ", discount_manager.total_price)

    print("test1", summer_discount_manager.add(product1, product_discount1))
    print("test2", summer_discount_manager.add(product2, product_discount2))
    print("test3", summer_discount_manager.add(product3, product_discount3))

    print("총 상품 여름 할인가격: ", summer_discount_manager.total_price)