from typing import List


class MagicPoint:
    def __init__(self, current_amount: int, original_max_amount: int, max_increments: List[int]):
        self.current_amount = current_amount
        self.original_max_amount = original_max_amount
        self.max_increments = max_increments

    def current(self):
        return self.current_amount
    
    def max(self):
        amount = self.original_max_amount
        for i in self.max_increments:
            amount += i
        return amount
    
    def recover(self, recovery_amount: int):
        self.current_amount = min(self.current_amount + recovery_amount, self.max())

    def consume(self, consume_amount: int):
        ...


if __name__ == "__main__":
    mp = MagicPoint(
        current_amount=50,
        original_max_amount=100,
        max_increments=[10, 20, 30]
    )
    print(f"현재 매직 포인트 잔량: {mp.current()}")
    print(f"매직 포인트 최댓값: {mp.max()}")
    
    mp.recover(80)
    print(f"매직 포인트 회복량: {mp.current()}")

    mp.recover(40)
    print(f"매직 포인트 회복량: {mp.current()}")