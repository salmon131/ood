class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shift(self, shift_x: int, shift_y: int):
        x = self.x + shift_x
        y = self.y + shift_y
        return Location(x, y)
    
    
class ActorManager:
    def __init__(self):
        ...

    def shift(self, location: Location, shift_x: int, shift_y: int):
        return location.shift(shift_x, shift_y)


if __name__ == "__main__":
    loc = Location(1, 2)
    print(loc.x, loc.y)
    loc2 = ActorManager().shift(loc, 1, 1)
    print(loc.x, loc.y)
    print(loc2.x, loc2.y)