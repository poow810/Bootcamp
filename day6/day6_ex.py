# # 9-1
# def good():
#     return ['Harry', 'Ron', 'Hermione']
#
# print(good())

# 9-2
# 제네레이트 컴프리헨션
# def get_odds():
#     return list(i for i in range(10) if i%2!=0)
#
# print(get_odds()[2])

# 제네레이트
# def get_odds():
#     for i in range(10):
#         if i%2 :
#             yield i
#
# odds=get_odds()
# count=0
# for i in odds:
#     count+=1
#     if count==3:
#        print(i)

# 9-3
def test(func):
    def new_function():
        try:
            print("start")
            func()
        finally:
            print("end")
    return new_function()


@test
def start():
    print('함수 호출')