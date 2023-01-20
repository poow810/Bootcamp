# # 10.1
# class Thing():
#     pass
#
#
# print(Thing)
# example = Thing()
# print(example)  # 출력값이 다름
#
# # 10.2
# class Thing2():
#     letters = 'abc'
#
# print(Thing2.letters)
#
# # 10.3
# class Thing3():
#     pass
#
# a = Thing3()
# a.letters = 'abc'
# print(a.letters)
#
# # 10.4
# class Element():
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#
#
#
#
# element = Element('Hydrogen', 'H', 1)
# print(element.name, element.symbol, element.number)
#
# # 10.5
# el_dict = {'name':'Hydrogen', 'symbol':'H', 'number':1}
# hydrogen = el_dict.keys()

# 10.6
# class Element():
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#
#
#     def __str__(self):
#         return f'{self.name} {self.symbol} {self.number}'
#
#
# # hydrogen = Element('Hydrogen', 'H', 1)
# # hydrogen.dump()
#
# # 10.7
# hydrogen = Element('Hydrogen', 'H', 1)
# print(hydrogen)


# # 10.8
# class Element():
#     def __init__(self, name, symbol, number):
#         self.__name = name
#         self.__symbol = symbol
#         self.__number = number
#     @property
#     def dump(self):
#         return self.__name, self.__symbol, self.__number
#
#
# hydrogen = Element('Hydrogen', 'H', 1)
# print(hydrogen.dump)

# 10.9
class Bear():
    def __init__(self, name):
        self.name = name

    def eats(self):
        return f"'{self.name}'(Bear)"



class Rabbit(Bear):
    def eats(self):
        return f"'{self.name}'(Rabbit)"



class Octothorpe(Bear):
    def eats(self):
        return f"'{self.name}'(Octothorpe)"


bear = Bear('berries')
rabbit = Rabbit('clover')
octothorpe = Octothorpe('campers')
print(bear.eats())
print(rabbit.eats())
print(octothorpe.eats())


# 10.10
class Robot():
    def __init__(self, name, laser, claw, smartphone):
        self.name = name
        self.laser = laser.does()
        self.claw = claw.does()
        self.smartphone = smartphone.does()


    def does(self):
        print(f'{self.laser} {self.claw} {self.smartphone}')


class Laser(Robot):
    def does(self):
        return f"'{self.name}'(Laser)"



class Claw(Robot):
    def does(self):
        return f"'{self.name}'(Claw)"


class SmartPhone(Robot):
    def does(self):
        return f"'{self.name}'(Smart Phone)"

laser = Laser('disintegrate')
claw = Claw('crush')
smartphone = SmartPhone('ring')