from enum import Enum
from abc import ABC, abstractmethod

class Member:
    def __init__(
            self,
            hit_point: int,
            magic_point: int,
            max_hit_point: int
        ):
        self.hit_point = hit_point
        self.magic_point = magic_point
        self.max_hit_point = max_hit_point
    
    def can_act(self):
        return True
    
    def consume_magic_point(self, cost_magic_point: int):
        print("consume!")

    def chant(self, magic):
        print("발동!")
    
    def add_state(self, state: "HealthCondition"):
        ...

class HealthCondition(Enum):
    dead = 1
    danger = 2
    caution = 3
    fine = 4


class DamageType(Enum):
    hit_point = 1
    magic_point = 2


class Damage(ABC):
    @abstractmethod
    def execute(self, damage_amount: int) -> Member:
        ...

class HitPointDamage(Damage):
    def execute(self, member: Member, damage_amount: int) -> Member:
        member.hit_point -= damage_amount
        if 0 < member.hit_point: 
            return member

        member.hit_point = 0
        member.add_state(HealthCondition.dead)

        return member


class MagicPointDamage(Damage):
    def execute(self, member: Member, damage_amount: int) -> Member:
        member.magic_point -= damage_amount
        if 0 < member.magic_point: 
            return member

        member.magic_point = 0

        return member

damages = {
    DamageType.hit_point: HitPointDamage(), 
    DamageType.magic_point: MagicPointDamage()
}

def apply_damage(member: Member, damage_type: DamageType, damage_amount: int):
    damage = damages.get(damage_type)
    return damage.execute(member, damage_amount)


if __name__ == "__main__":
    member = Member(
        hit_point=50,
        magic_point=60,
        max_hit_point=100
    )
    member = apply_damage(member, DamageType.hit_point, 30)
    print(member.hit_point)

    member = apply_damage(member, DamageType.hit_point, 50)
    print(member.hit_point)

    member = apply_damage(member, DamageType.magic_point, 50)
    print(member.magic_point)

    member = apply_damage(member, DamageType.magic_point, 50)
    print(member.magic_point)
