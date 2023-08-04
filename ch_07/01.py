if __name__ == "__main__":
    keys = ['감옥 열쇠', '빨간열쇠', '파란열쇠']

    # java에서 anyMatch는 python에서 any와 같다
    print(any([key == '감옥 열쇠' for key in keys]))