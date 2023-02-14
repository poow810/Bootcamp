# pokemon game v0.4
# getter setter -> property -> decorator
# class field
class Pokemon:
    count = 0
    def __init__(self, owner, skills):  # 객체 생성 시 동작
        self.__hidden_owner = owner     # like private
        self.skills = skills.split('/')
        print(f"포켓몬 생성됨", end=" : ")
        Pokemon.count+=1

    @property
    def owner(self):
        return self.__hidden_owner

    @owner.setter
    def owner(self, owner):
        self.__hidden_owner = owner

    #owner = property(get_owner, set_owner)

    def info(self):
        print(f"{self.owner}의 포켓몬이 사용 가능한 스킬입니다.")
        for i in range(len(self.skills)):
            print(f'{i + 1} : {self.skills[i]}')

        # for skill in self.skills:
        #     print(f'{skill}')

    def attack(self, idx):
        print(f'{self.skills[idx]} 공격 시전')


class Pikachu(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "피카츄"
        print(f"{self.name}")

        def attack(self, idx):  # override
            print(f'[삐까삐까] {self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전')




class Ggoboogi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self, idx):  # override
        print(f'[꼬북꼬북] {self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전')

    def swim(self):
        print(f'{self.name}가 수영을 합니다.')


class Pairi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "파이리"
        print(f"{self.name}")

    def attack(self, idx):  # override
        print(f'[파이파이] {self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전')


while True:
    print(f'총 {Pokemon.count}마리의 포켓몬이 생성되었습니다')
    menu = input('1) 포켓몬 생성 2) 프로그램 종료 : ')
    if menu == '2':
        print('프로그램을 종료합니다')
        break
    elif menu == '1':
        pokemon = input('1) 피카츄 2) 꼬부기 3) 파이리 : ')
        n = input('플레이어 이름 입력 : ')
        s = input('사용 가능한 기술 입력(/로 구분하여 입력) : ')
        if pokemon == '1':
            p = Pikachu(n, s)
        elif pokemon == '2':
            p = Ggoboogi(n, s)
        elif pokemon == '3':
            p = Pairi(n, s)
        else:
            print('메뉴에서 골라 주세요')
        info_attack = input('1) 정보 조회 2) 공격 : ')
        if info_attack == '1':
            p.info()

        elif info_attack == '2':
            p.info()
            attack_menu = input('공격 번호 선택 : ')
            p.attack(int(attack_menu) - 1)
        else:
            print('메뉴에서 골라 주세요')

    else:
        print('메뉴에서 골라 주세요')
