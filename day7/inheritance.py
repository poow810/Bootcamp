# # inheritance
# class Car():
#     def exclaim(self):
#         print("I'm a Car!")
#
# class Yugo(Car):
#     def exclaim(self):
#         print("I'm a Yugo! Much like a Car, but moore Yugo-ish")
#
#
#
# class Person():
#     def __init__(self, name):
#         self.name = name
#
#
# class MDPerson(Person):
#     def __init__(self, name):
#         self.name = "Doctor " + name
#
#
# class JDPerson(Person):
#     def __init__(self, name):
#         self.name = name + ", Esquire"
#
#
# person = Person("Fudd")
# doctor = MDPerson("Fudd")
# lawyer = JDPerson("Fudd")
# print(person.name)
# print(doctor.name)
# print(lawyer.name)
import math


# add method
# class Car():
#     def exclaim(self):
#         print("I'm a Car!")
#
#
# class Yugo(Car):
#     def exclaim(self):
#         print("I'm a Yugo! Much like a Car, but moore Yugo-ish")
#     def need_a_push(self):
#         print("A little help here?")
#
#
# give_me_a_car = Car()
# give_me_a_yugo = Yugo()
#
# give_me_a_yugo.need_a_push()
#
# class Pokemon:
#     def __init__(self, owner, skills):     # 객체 생성 시 동작
#         self.owner = owner
#         self.skills = skills.split('/')
#         print(f"포켓몬 생성됨", end=" : ")
#
#     def info(self):
#         print(f"{self.owner}의 포켓몬이 사용 가능한 스킬입니다.")
#         for skill in self.skills:
#             print(skill)
#
#
#     def attack(self, idx):
#         print(f'{self.skills[idx]} 공격 시전')
#
# class Pikachu(Pokemon):
#     def __init__(self, owner, skills):
#         super().__init__(owner, skills)
#         self.name = "피카츄"
#         print(f"{self.name}")
#
#         def attack(self, idx):      # override
#             print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전')
#
#
# class Ggoboogi(Pokemon):
#     def __init__(self, owner, skills):
#         super().__init__(owner, skills)
#         self.name = "꼬부기"
#         print(f"{self.name}")
#
#     def attack(self, idx):      # override
#         print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전')
#
#     def swim(self):
#         print(f'{self.name}가 수영을 합니다.')
#
#
# p0 = Pokemon("아이리스", "어떤 공격")
# pk1 = Pikachu('한지우', '번개')
# ggo1 = Ggoboogi('오바람', '고속 스핀/거품/몸통박치기')
# ggo1.attack(2)
# ggo1.swim()        #부모 class는 사용할 수 없음

class Animal:
    def says(self):
        return 'I speak!'


class Horse(Animal):
    def says(self):
        return 'Neight!'


class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'


class Mule(Donkey, Horse):
    pass


class Minny(Horse, Donkey):
    pass

m1 = Mule()
print(m1.says())


class PrettyMixin:
    def time_print(self):
        import datetime
        print(datetime.date.today())
    def dump(self):
        import pprint
        pprint.pprint(vars(self))
class Thing(PrettyMixin):
    pass


t = Thing()
t.time_print()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"
t.dump()

# 좀이따 다시 해보기
# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#
    @classmethod
    def test():
        pass


    @staticmethod
    def ace():
        pass


#     @property
#     def get_name(self):
#         print('inside the getter')
#         return self.hidden_name
#
#     @name.setter
#     def set_name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name

don = Duck('Donald')
print(don.name)         # 클래스.name은 쓸 수 없음
# don = Duck('Donald')
# don.get_name()

# don = Duck('Donald')
# print(don.color, Duck.color)
# don.color = 'blue'
# print(don.color, Duck.color)
# Duck.color = 'green'
# print(don.color, Duck.color)
# d2 = Duck('Induk')



class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_area(self):
        print("도형의 면적을 출력합니다")


class Circle(Shape):
    def __init__(self, x, y, radius, height):
        super().__init__(x, y, radius)
        self.radius = height


    def get_area(self):
        return math.pi * self.radius * self.radius * self.height


class Rectangle(Shape):
    def __init__(self, x, y, width, length):
        super().__init__(x, y)
        self.width = width
        self.length = length

    def get_area(self):
        return super().get_area() * self.height


c1 = Circle(100, 100, 10.0)
c2 = Circle(50, 50, 2.0)
r1 = Rectangle(100, 2)

print(f'사각형의 좌표는 x : {r1.x}, y = {r1.y}이고 넓이는 {r1.get_area()}입니다')



