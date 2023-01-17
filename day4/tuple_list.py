# tuple
a = 'harry',
b = ('harry',)
c = ()      # empty tuple
d = 'harry', 'ron'  # packing
e = ('hermione')  # string
f = ('harry', 'ron')  # packing
g = ('hermione',)  # string
print(id(g))    #id값이 다름
print(f[1])
x, y = f    # unpacking
g = f+g     # 덮어쓰기
print(id(g))    #id값이 다름
print(g)


# tuple 비교하기 - 원소 개수 비교
a = (7, 2)
b = (7, 2, 9)
print(a == b)