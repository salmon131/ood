class PhysicalAttack:
    def __init__(self) -> None:
        ...

    def single_attack_damage(self):
        return 10

    def double_attack_damage(self):
        return self.single_attack_damage() * 2
    

class FighterPhysicalAttack(PhysicalAttack):
    def __init__(self) -> None:
        super().__init__()

    def single_attack_damage(self):
        return super().single_attack_damage() + 20
    
    def double_attack_damage(self):
        return super().double_attack_damage() + 10
    

class FighterPhysicalAttackV2:
    def __init__(self) -> None:
        self.physical_attack = PhysicalAttack()

    def single_attack_damage(self):
        return self.physical_attack.single_attack_damage() + 20
    
    def double_attack_damage(self):
        return self.physical_attack.double_attack_damage() + 10
    

if __name__ == "__main__":
    attack = FighterPhysicalAttack()
    attack2 = FighterPhysicalAttackV2()

    print(attack.single_attack_damage())
    print(attack.double_attack_damage())

    print(attack2.single_attack_damage())
    print(attack2.double_attack_damage())