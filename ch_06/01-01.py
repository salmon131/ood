class Magic:
    def __init__(self, cost_magic_point: int):
        self.cost_magic_point = cost_magic_point

class Member:
    def __init__(
            self,
            hit_point: int,
            magic_point: int
        ):
        self.hit_point = hit_point
        self.magic_point = magic_point
    
    def can_act(self):
        return True
    
    def consume_magic_point(self, cost_magic_point: int):
        print("consume!")

    def chant(self, magic):
        print("발동!")


def bad_case():
    member = Member(hit_point = 10, magic_point = 10)
    magic = Magic(cost_magic_point= 5)

    if 0 < member.hit_point:
        if member.can_act():
            if magic.cost_magic_point <= member.magic_point:
                member.consume_magic_point(magic.cost_magic_point)
                member.chant(magic)
                
    member.consume_magic_point(magic.cost_magic_point)
    member.chant(magic)

def good_case():
    member = Member(hit_point = 10, magic_point = 10)
    magic = Magic(cost_magic_point= 5)

    if member.hit_point <= 0: return
    if not member.can_act(): return
    if member.magic_point < magic.cost_magic_point: return

    member.consume_magic_point(magic.cost_magic_point)
    member.chant(magic)

    
if __name__=="__main__":
    good_case()







