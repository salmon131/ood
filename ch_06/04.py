from abc import ABC, abstractmethod


class Money:
    def __init__(self, amount: int):
        self.amount = amount

    def __add__(self, other: "Money") -> "Money":
        return self.amount + other.amount
    

class HotelRates(ABC):
    @abstractmethod
    def fee(self) -> Money:
        ...
    
    @abstractmethod
    def busy_season_fee(self) -> Money:
        ...


class RegularRates(HotelRates):
    def fee(self) -> Money:
        return Money(700000)
    
    def busy_season_fee(self) -> Money:
        return self.fee() + Money(30000)
    

class PremiumRates(HotelRates):
    def fee(self) -> Money:
        return Money(1200000)
    
    def busy_season_fee(self) -> Money:
        return self.fee() + Money(50000)
    

class Cash:
    def __init__(self, hotel_rate: HotelRates):
        self.hotel_rate = hotel_rate

    def billing(self, type) -> Money:
        if type == "busy":
            return self.hotel_rate.busy_season_fee()
        return self.hotel_rate.fee()
    

if __name__ == "__main__":
    regular_rates = RegularRates()
    premium_rates = PremiumRates()

    print(f"일반 객실 비수기 가격: {regular_rates.fee().amount}")
    print(f"일반 객실 성수기 가격: {regular_rates.busy_season_fee()}")

    print(f"프리미엄 객실 비수기 가격: {regular_rates.fee().amount}")
    print(f"프리미엄 객실 성수기 가격: {regular_rates.busy_season_fee()}")

    cash = Cash(regular_rates)
    print(cash.billing("busy"))