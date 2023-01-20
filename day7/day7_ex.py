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
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


    def dump(self):
        print(self.name, self.symbol, self.number)


hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.dump()
