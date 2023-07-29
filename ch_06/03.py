from typing import Set
from abc import ABC, abstractmethod


class PurchaseHistory:
    def __init__(
            self, 
            total_amount: int, 
            purchase_frequency_per_month: int,
            return_rate: float
        ):
        self.total_amount = total_amount
        self.purchase_frequency_per_month = purchase_frequency_per_month
        self.return_rate = return_rate


class ExcellentCustomerRule(ABC):

    @abstractmethod
    def ok(self, history: PurchaseHistory) -> bool:
        ...


class GoldCustomerPurchaseAmountRule(ExcellentCustomerRule):
    def ok(self, history: PurchaseHistory) -> bool:
        return 1000000 <= history.total_amount


class PurchaseFrequencyRule(ExcellentCustomerRule):
    def ok(self, history: PurchaseHistory) -> bool:
        return 10 <= history.purchase_frequency_per_month


class ReturnRateRule(ExcellentCustomerRule):
    def ok(self, history: PurchaseHistory) -> bool:
        return history.return_rate <= 0.001


class ExcellentCustomerPolicy:
    def __init__(self):
        self.rules: Set[ExcellentCustomerRule] = set()

    def add(self, rule: ExcellentCustomerRule):
        self.rules.add(rule)

    def comply_with_all(self, history: PurchaseHistory) -> bool:
        for rule in self.rules:
            if not rule.ok(history): return False
        return True


class GoldCustomerPolicy:
    def __init__(self):
        self.policy = ExcellentCustomerPolicy()
        self.policy.add(GoldCustomerPurchaseAmountRule())
        self.policy.add(PurchaseFrequencyRule())
        self.policy.add(ReturnRateRule())

    def comply_with_all(self, history: PurchaseHistory) -> bool:
        return self.policy.comply_with_all(history)
    

class SilverCustomerPolicy:
    def __init__(self):
        self.policy = ExcellentCustomerPolicy()
        self.policy.add(PurchaseFrequencyRule())
        self.policy.add(ReturnRateRule())

    def comply_with_all(self, history: PurchaseHistory) -> bool:
        return self.policy.comply_with_all(history)


if __name__=="__main__":
    history = PurchaseHistory(
        total_amount=100,
        purchase_frequency_per_month=100,
        return_rate=0.001
    )

    gold_policy = GoldCustomerPolicy()
    silver_policy = SilverCustomerPolicy()

    print(f"골드회원인가?: {gold_policy.comply_with_all(history)}")
    print(f"실버회원인가?: {silver_policy.comply_with_all(history)}")