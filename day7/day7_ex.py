# 10.1
class Thing():
    pass


print(Thing)
example = Thing()
print(example)  # 출력값이 다름

# 10.2
class Thing2():
    letters = 'abc'

print(Thing2.letters)

# 10.3
class Thing3():
    pass

a = Thing3()
a.letters = 'abc'
print(a.letters)