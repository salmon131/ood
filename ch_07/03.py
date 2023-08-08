from typing import List
import copy

class Member:
    def __init__(self, id: int):
        self.id = id

    def is_alive(self):
        return True

# 안티 패턴
class FieldManager:
    MAX_MEMBER_COUNT = 4

    def __init__(self):
        ...

    def add_member(self, members: List[Member], new_member: Member):
        if any([member.id == new_member.id for member in members]):
            raise Exception("이미 존재하는 멤버입니다.")
        
        if len(members) == FieldManager.MAX_MEMBER_COUNT:
            raise Exception("이 이상 멤버를 추가할 수 없습니다.")
        
        members.append(new_member)

    def party_is_alive(self, members: List[Member]):
        return any([member.is_alive() for member in members])
    

class SpecialEventManager:
    def __init__(self):
        ...

    def add_member(self, members: List[Member], new_member: Member):
        if any([member.id == new_member.id for member in members]):
            raise Exception("이미 존재하는 멤버입니다.")
        
        if len(members) == FieldManager.MAX_MEMBER_COUNT:
            raise Exception("이 이상 멤버를 추가할 수 없습니다.")
        
        members.append(new_member)


class BattleManager:
    def __init__(self):
        ...

    def members_are_alibe(self, members: List[Member]):
        result = False
        for each in members:
            if each.is_alive():
                result = True
                break

        return result
    

class Party:
    MAX_MEMBER_COUNT = 4

    def __init__(self, members: List[Member]):
        self._members = members

    @property
    def members(self):
        return tuple(self._members)

    def add(self, new_member: Member):
        if self.exists(new_member):
            raise Exception("이미 존재하는 멤버입니다.")
        if self.is_full():
            raise Exception("이 이상 멤버를 추가할 수 없습니다.")

        adding = copy.deepcopy(self._members)
        adding.append(new_member)
        return Party(adding)
    
    def is_alive(self):
        return any([member.is_alive() for member in self.members])

    def exists(self, member: Member):
        return any([each.id == member.id for each in self.members])
    
    def is_full(self):
        return len(self.members) == Party.MAX_MEMBER_COUNT
    

if __name__ == "__main__":
    members = [Member(1), Member(2), Member(3)]
    party = Party(members)

    party = party.add(Member(4))
    print([member.id for member in party.members])

    # exception
    party = party.add(Member(5))
    print([member.id for member in party.members])

