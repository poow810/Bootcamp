# function
import random

# 리스트로 표현
def calculate_fee(args)->list:
    """
    놀이공원 요금 계산 프로그램
    :param args: age in list
    :return: 전체 인원수, 어른 수, 아이수, 총 금액
    """
    total = 0
    adult = 0
    kids = 0
    for age in args:
        if 19 <= age:
            total = total + 10000
            adult = adult + 1
        else:
            total = total + 3000
            kids = kids + 1
    return [len(args), adult, kids, total]
n = int(input())
ages = []
for i in range(n):
    ages.append(random.randint(1,50))

results = calculate_fee(ages)
print(f'{results[0]}명 방문 하셨고 어른 {results[1]}명, 아이 {results[2]}명, 총 요금은 {results[-1]}입니다.')

# 딕셔너리로 표현
def calculate_fee(args):
    """
    놀이공원 요금 계산 프로그램
    :param args: age in list
    :return: {'no_of_people': 전체 인원수, 'no_of_adult':어른 수, 'no_of_kid' : 아이수, 'total_fee': 총 금액}
    """
    total = 0
    adult = 0
    kids = 0
    for age in ages:
        if 19 <= age:
            total = total + 10000
            adult = adult + 1
        else:
            total = total + 3000
            kids = kids + 1
    return {'no_of_people': len(args), 'no_of_adult': adult, 'no_of_kid' : kids, 'total_fee': total}
n = int(input())
ages = []
for i in range(n):
    ages.append(random.randint(1,50))
results = calculate_fee(ages)
print(f"{results['no_of_people']}명 방문하셨고 어른 {results['no_of_adult']}명 아이 {results['no_of_kid']}명으로 총 {results['total_fee']}원 입니다.")
# def do_nothing():
#     pass
#
# mamamoo = {'화사', '솔라', '휘인', '문별'}
# print(mamamoo.pop())        # 삭제할 값 리턴 후 삭제
# print(mamamoo.remove('문별'))     #
#
#
# print(mamamoo)
