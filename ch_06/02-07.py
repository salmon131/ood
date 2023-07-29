from enum import Enum

class MagicType(Enum):
    fire = 0
    lightning = 1
    hellfire = 2

class Member:
    def __init__(self, level, agility=0):
        self.level = level
        self.agility = agility
    
class MagicManager:
    def __init__(self):
        pass
    
    def getName(self, magic_type : MagicType):
        name = ""
        match magic_type:
            case MagicType.fire:
                name = "파이어"
            case MagicType.lightning:
                name = "라이트닝"
            case MagicType.hellfire:
                name = "헬파이어"
        return name
    
    def cost_magic_point(self, magic_type : MagicType, member : Member):
        magic_point = 0
        match magic_type:
            case MagicType.fire:
                magic_point = 2
            case MagicType.lightning:
                magic_point = 5 + member.level*0.2
            case MagicType.hellfire:
                magic_point = 16
        return magic_point

    def attack_power(self, magic_type: MagicType, member:Member):
        attack_power = 0
        match magic_type:            
            case MagicType.fire:
                attack_power = 20 + member.level*0.5
            case MagicType.lightning:
                attack_power = 50 + member.agility*1.5
        return attack_power
    
    def cost_technical_point(self, magic_type: MagicType, member:Member):
        technical_point = 0
        match magic_type:            
            case MagicType.fire:
                technical_point = 0
            case MagicType.lightning:
                technical_point = 5
        return technical_point
    
if __name__ == "__main__":
    magic_manager = MagicManager()
    print(magic_manager.getName(MagicType.fire))
    print(magic_manager.cost_magic_point(MagicType.lightning, Member(10)))
    print(magic_manager.attack_power(MagicType.lightning, Member(10, 20)))