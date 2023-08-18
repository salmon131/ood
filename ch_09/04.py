class Equipment:

    def __init__(self, name: str, price: int, defence: int, magic_defence: int):
        if not name:
            raise ValueError("잘못된 이름입니다.")
        self._name = name
        self._price = price
        self._defence = defence
        self._magic_defence = magic_defence

    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    @property
    def defence(self):
        return self._defence
    
    @property
    def magic_defence(self):
        return self._magic_defence
    

Equipment.EMPTY = Equipment("장비 없음", 0, 0, 0)


class Member:
    def __init__(self, head: Equipment, body: Equipment, arm: Equipment, defence: int):
        self.head = head
        self.body = body
        self.arm = arm
        self.defence = defence

    def total_defence(self):
        total = self.defence
        total += self.head.defence
        total += self.body.defence
        total += self.arm.defence
        return total

    def take_off_all_equipments(self):
        self.head = Equipment.EMPTY
        self.body = Equipment.EMPTY
        self.arm = Equipment.EMPTY


if __name__ == "__main__":
    member = Member(Equipment("head", 10, 10, 10),
                    Equipment("body", 20, 20, 20),
                    Equipment("arm", 30, 30, 30),
                    100
                    )
    member.take_off_all_equipments()
    print(member.total_defence())