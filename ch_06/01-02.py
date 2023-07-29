from enum import Enum

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

class HealthCondition(Enum):
    dead = 1
    danger = 2
    caution = 3
    fine = 4

def bad_case():
    member = Member(hit_point = 5, magic_point = 10, max_hit_point=20)

    hit_point_rate = member.hit_point / member.max_hit_point

    current_health_condition = HealthCondition.fine

    if hit_point_rate == 0:
        current_health_condition = HealthCondition.dead
    elif hit_point_rate < 0.3:
        current_health_condition = HealthCondition.danger
    elif hit_point_rate < 0.5:
        current_health_condition = HealthCondition.caution
    else:
        current_health_condition = HealthCondition.fine

    return current_health_condition

def good_case():
    member = Member(hit_point = 5, magic_point = 10, max_hit_point=20)

    hit_point_rate = member.hit_point / member.max_hit_point

    if hit_point_rate == 0: return HealthCondition.dead
    if hit_point_rate < 0.3: return HealthCondition.danger
    if hit_point_rate < 0.5: return HealthCondition.caution
    
    return HealthCondition.fine


if __name__=="__main__":
    print(good_case())