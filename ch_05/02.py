class GiftPoint(object):

    __create_key = object()

    MIN_POINT = 0
    STANDARD_MEMBERSHIP_POINT = 3000
    PREMIUM_MEMBERSHIP_POINT = 10000

    def __init__(self, create_key, point: int):
        assert(create_key == GiftPoint.__create_key), \
            "OnlyCreatable objects must be created using OnlyCreatable.create"
        
        if point < self.MIN_POINT:
            raise Exception("포인트는 0 이상이어야 합니다.")
        self.value = point

    @staticmethod
    def for_standard_membership():
        return GiftPoint(GiftPoint.__create_key, GiftPoint.STANDARD_MEMBERSHIP_POINT)
    
    @staticmethod
    def for_premium_membership():
        return GiftPoint(GiftPoint.__create_key, GiftPoint.PREMIUM_MEMBERSHIP_POINT)


if __name__=="__main__":
    standard_point = GiftPoint.for_standard_membership()
    print(standard_point.value)

    premium_point = GiftPoint.for_premium_membership()
    print(premium_point.value)

    point = GiftPoint(point=100)
    print(point.value)