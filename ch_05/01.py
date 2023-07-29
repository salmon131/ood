class Money:
    def __init__(self, amount: int):
        self.amount = amount

    def __add__(self, other: "Money") -> "Money":
        return Money(self.amount + other.amount)


if __name__ == "__main__":
    money1 = Money(100)
    money2 = Money(200)
    money3 = money1 + money2

    print(money3.amount)