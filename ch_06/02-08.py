from abc import ABC, abstractmethod
from enum import Enum
class MagicType(Enum):
    fire = 0
    lightning = 1
    hellfire = 2
    water = 3
    
class Magic(ABC):
    @abstractmethod
    def name(self) -> str:
        ...
    @abstractmethod
    def cost_magic_point(self) -> int:
        ...
    @abstractmethod
    def attack_power(self, member) -> int:
        ...
    @abstractmethod
    def cost_technical_point(self)-> int:
        ...

class Member:
    def __init__(self, level, agility=0, magic_attack = 0):
        self.level = level
        self.agility = agility
        self.magic_attack = magic_attack
        
class Fire(Magic):
    _member : Member
    
    def __init__(self, member: Member):
        self._member = member
    
    def name(self) -> str:
        return "파이어"
    
    def cost_magic_point(self) -> int:
        return 2
    
    def attack_power(self) -> int:
        return 20 + self._member.level*0.5
    
    def cost_technical_point(self) -> int:
        return 0

class Lighting(Magic):
    _member : Member
    
    def __init__(self, member: Member):
        self._member = member
    
    def name(self) -> str:
        return "라이트닝"
    
    def cost_magic_point(self) -> int:
        return 5 + self._member.level*0.2
    
    def attack_power(self) -> int:
        return 50 + self._member.agility*1.5
    
    def cost_technical_point(self) -> int:
        return 5
    
class HellFire(Magic):
    _member : Member
    
    def __init__(self, member: Member):
        self._member = member
    
    def name(self) -> str:
        return "헬파이어"
    
    def cost_magic_point(self) -> int:
        return 16
    
    # def attack_power(self) -> int:
    #     return 200 + self._member.magic_attack*0.5 + self._member.agility*2
    
    def cost_technical_point(self) -> int:
        return 20 + self._member*0.4
 
   
if __name__ == "__main__":
    magic_map = {MagicType.fire : Fire(Member(10)), 
                 MagicType.lightning : Lighting(Member(10)),
                 MagicType.hellfire : HellFire(Member(10))}
    def magic_attact(magic_type : MagicType):
        magic = magic_map[magic_type]
        return magic.attack_power()
        
    print(magic_attact(MagicType.hellfire)) # hellfire 구현 안한 경우