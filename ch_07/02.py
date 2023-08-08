from enum import Enum
from typing import List


class StateType(Enum):
    poison = 1
    dead = 2

class Member:
    def __init__(self, hit_point: int, states: List[StateType]):
        self.hit_point = hit_point
        self.states = states
    
    def contains_state(self, state_type: StateType):
        if state_type in self.states:
            return True
        return False
    
    def add_state(self, state_type: StateType):
        self.states.append(state_type)

    def remove_state(self, state_type: StateType):
        self.states.remove(state_type)

    def has_team_attack_succeeded(self):
        return True
    
    def attack(self):
        return 30
    

def poison_damage(members: List[Member]):
    for member in members:
        if member.hit_point == 0: continue
            
        if not member.contains_state(StateType.poison): continue

        member.hit_point -= 10

        if member.hit_point: continue

        member.hit_point = 0
        member.add_state(StateType.dead)
        member.remove_state(StateType.poison)

    return members


def team_attack(members: List[Member]):
    total_damage = 0

    for member in members:
        if not member.has_team_attack_succeeded(): break

        damage = member.attack() * 1.1

        if damage < 30: break

        total_damage += damage

    return total_damage


if __name__ == "__main__":
    member = Member(hit_point=10, states=[StateType.poison])

    print(member.states, member.hit_point)
    members = poison_damage([member])
    print(members[0].states, member.hit_point)


    print(team_attack([member]))