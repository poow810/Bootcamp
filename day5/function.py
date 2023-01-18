# Closures
def calculate():
    x = 1
    y = 2
    temp = 0
    def add_sub(n):
        nonlocal temp       # temp가 변경된 값을 계속 기억 != local variable
        # x = 11      # local variable
        temp = temp + x + n - y
        return temp
    return add_sub

c1 = calculate()
for i in range(5):
    print(c1(i))
print(type(c1))