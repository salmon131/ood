from typing import Final


class Currency:
    def __init__(self, value: str = None):
        if value not in ["원", "$"]:
            raise ValueError("통화 단위는 '원' 혹은 '$'여야 합니다.")
        self.value = value


class Money:
    def __init__(self, amount: int, currency: Currency):
        if amount < 0:
            raise ValueError("금액은 0 이상의 값을 지정해주세요.")
        if currency == None:
            raise ValueError("통화 단위를 지정해 주세요.")
        
        self._amount = amount
        self._currency = currency

    @property
    def amount(self):
        return self._amount
    
    @property
    def currency(self):
        return self._currency
    
    def add(self, other: "Money"):
        _other: Final["Money"] = other
        
        if self.currency != _other.currency:
            raise ValueError("통화 단위가 다릅니다.")
        
        added = self.amount + _other.amount
        return Money(added, self.currency)
    

if __name__ == "__main__":
    curr = Currency(value="원")
    money = Money(10000, curr)
    money2 = Money(3000, curr)
    new = money.add(money2)
    print(new.amount)
        