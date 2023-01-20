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
