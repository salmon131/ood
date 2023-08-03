import typing as t


class Product:
    def __init__(self, id: int, name: str, price: int):
        self.id = id
        self.name = name
        self.price = price


class ProductDiscount:
    def __init__(self, id: int, can_discount: bool):
        self.id = id
        self.can_discount = can_discount


class DiscountManager:
    discount_products: t.List[Product] = []
    total_price = 0

    def add(self, product: Product, product_discount: ProductDiscount):
        if product.id < 0:
            raise Exception("Invalid product id")
        if product.name  == "":
            raise Exception("Invalid product name")
        if product.price < 0:
            raise Exception("Invalid product price")
        if product.id != product_discount.id:
            raise Exception("Invalid product id")
        discount_price = self.get_discount_price(product.price)
        
        tmp = 0
        if product_discount.can_discount:
            tmp = DiscountManager.total_price + discount_price
        else:
            tmp = DiscountManager.total_price + product.price

        if tmp <= 200000:
            self.total_price = tmp
            DiscountManager.discount_products.append(product)
            return True
        else:
            return False
        
    def get_discount_price(self, price: int):
        discount_price = price - 3000
        if discount_price < 0:
            discount_price = 0
        return discount_price
    

class SummerDiscountManager:
    discount_manager = DiscountManager()

    def add(self, product: Product):
        if product.id < 0:
            raise Exception("Invalid product id")
        if product.name  == "":
            raise Exception("Invalid product name")
        
        if product.can_discount:
            tmp = SummerDiscountManager.discount_manager.total_price + SummerDiscountManager.discount_manager.get_discount_price(product.price)
        else:
            tmp = SummerDiscountManager.discount_manager.total_price + product.price

        if tmp <= 300000:
            self.total_price = tmp
            SummerDiscountManager.discount_manager.discount_products.append(product)
            return True
        else:
            return False


if __name__ == "__main__":
    product1 = Product(1, "test1", 10000)
    product2 = Product(2, "test2", 20000)
    product3 = Product(3, "test3", 30000)

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

    print("총 상품 여름 할인가격: ", summer_discount_manager.total_price) # 버그 발생