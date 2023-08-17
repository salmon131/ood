from enum import Enum
from typing import List


class StateType(Enum):
    poison = 1
    dead = 2


class HitPoint:
    MIN = 0
    def __init__(self, amount: int):
        if amount < HitPoint.MIN:
            raise Exception()
        self.amount = amount

    def damage(self, damage_amount: int):
        next_amount = self.amount - damage_amount
        self.amount = max(HitPoint.MIN, next_amount)

    def is_zero(self):
        return self.amount == HitPoint.MIN

class Member:
    def __init__(self, hit_point: HitPoint, states: List[StateType]):
        self.hit_point = hit_point
        self.states = states

    def damage(self, damage_amount: int):
        self.hit_point.damage(damage_amount)
        if self.hit_point.is_zero():
            self.states.append(StateType.dead)


if __name__ == "__main__":
    member = Member(HitPoint(100), states=[])
    member.damage(80)
    print(member.states)
    member.damage(40)
    print(member.states)