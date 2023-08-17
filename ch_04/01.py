from typing import Final

class AttackPower:
    MIN = 0
    def __init__(self, value: int):
        if value < AttackPower.MIN:
            raise ValueError()
        
        self._value = value

    @property
    def value(self):
        return self._value
    
    def reinforce(self, increment: "AttackPower"):
        _increment: Final["AttackPower"] = increment
        return AttackPower(self.value + _increment.value)
    
    def disable(self):
        return AttackPower(AttackPower.MIN)


class Weapon:
    def __init__(self, attack_power: AttackPower):
        self._attack_power = attack_power

    @property
    def attack_power(self):
        return self._attack_power
    
    def reinforce(self, increment: "AttackPower"):
        reinforced: Final["AttackPower"] = self.attack_power.reinforce(increment)
        return Weapon(reinforced)
    

if __name__ == "__main__":
    attack_power_a = AttackPower(20)
    attack_power_b = AttackPower(20)
    weapon_a = Weapon(attack_power_a)
    weapon_b = Weapon(attack_power_b)
    
    print(weapon_a.attack_power.value)
    print(weapon_b.attack_power.value)

    increment = AttackPower(5)
    reinforced_weapon_a = weapon_a.reinforce(increment)

    print(reinforced_weapon_a.attack_power.value)
    print(weapon_b.attack_power.value)
