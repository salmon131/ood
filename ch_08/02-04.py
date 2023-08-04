from typing import List

class Product:
    def __init__(self) -> None:
        pass


class OrderService:
    def _calc_discount_price(self, price: int) -> int:
        ...
    
    def _get_product_browsing_history(self, user_id: int) -> List[Product]:
        ...


    
