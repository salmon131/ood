class Equipment:

    def __init__(self, name: str, price: int, defence: int, magic_defence: int):
        self.name = name
        self.price = price
        self.defence = defence
        self.magic_defence = magic_defence


Equipment.EMPTY = Equipment("장비 없음", 0, 0, 0)

class Equipments:
    def __init__(self, can_change: bool, head: Equipment, armor: Equipment, arm: Equipment):
        self.can_change = can_change
        self.head = head
        self.armor = armor
        self.arm = arm

    def equip_amor(self, new_armor: Equipment):
        if self.can_change:
            self.armor = new_armor

    def deactivae_all(self):
        self.head = Equipment.EMPTY
        self.armor = Equipment.EMPTY
        self.arm = Equipment.EMPTY


if __name__ == "__main__":
    head = Equipment("투구", 1000, 30, 30)
    armor = Equipment("갑옷", 300, 20, 20)
    arm = Equipment("무기", 200, 10, 10)

    equipments = Equipments(True, head, armor, arm)

    new_armor = Equipment("새 갑옷", 400, 30, 30)
    equipments.equip_amor(new_armor)
    print(equipments.armor.name)

    equipments.deactivae_all()
    print(equipments.head.name)