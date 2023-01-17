# # dictionary
#
# students = {'name' : 'Kim inha', 'age' : '23', 'eyes' : [0.9, 1.1]}
# for k in students.keys():       # key 값만
#     print(k)
# for v in students.values():     # value 값만
#     print(v)
# for k, v in students.items():
#     print(f'{k} : {v}')
# print(f"이름은 {students['name']}")
# print(f"나이는 {students['age']}")
# print(f"시력은 좌: {students['eyes'][0]}, 우 :{students['eyes'][1]}")

# dictionary2
import random
alcohol_foods = {
    '맥주' : '치킨',
    '소주' : '골뱅이소면',
    '와인' : '치즈',
    '고량주' : '짬뽕'
}
alcohol_list = list(alcohol_foods)      # extract keys
food_list = [food for food in alcohol_foods.values()]
# print(alcohol_list, food_list)
while True:
    alcohol = input(f'술을 선택하세요 1) {alcohol_list[0]} 2) {alcohol_list[1]} 3) {alcohol_list[2]} 4) {alcohol_list[3]} 5) 계산 : ')
    if alcohol == '5':
        print('다음에 또 오세요')
        break
    elif alcohol == '1':
        print(f'{random.choice(alcohol_list)}에 어울리는 안주는 {random.choice(food_list)}입니다')      # 리스트에선 키값 딕셔너리에서는 키값에 대한 값 반환
    elif alcohol == '2':
        print(f'{alcohol_list[1]}에 어울리는 안주는 {alcohol_foods[alcohol_list[1]]}입니다')
    elif alcohol == '3':
        print(f'{alcohol_list[2]}에 어울리는 안주는 {alcohol_foods[alcohol_list[2]]}입니다')
    elif alcohol == '4':
        print(f'{alcohol_list[3]}에 어울리는 안주는 {alcohol_foods[alcohol_list[3]]}입니다')
    else:
        print('메뉴에서 골라주세요')