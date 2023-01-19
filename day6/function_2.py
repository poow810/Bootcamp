# namespace
g = 1       # 전역 변수
def print_global():
    # g = 1     # 지역 변수
    print(g)


def change_print_global():
    global g        # 전역 변수 선언
    print(g)
    g = 2
    print(g)


change_print_global()
print_global()
print(g)
print(globals())
print(__name__)