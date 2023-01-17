# list comprehension
a_list = [i for i in range(1,11) if i % 2==1]    # 리스트 comprehension
print(a_list)

b_list = (i for i in range(1,11) if i % 2==1)   # generator 객체 (튜플이 아님)
print(b_list)

odd_list = []
for i in range(1,11):
    if i % 2 == 1:
        odd_list.append(i)      # 원래 방식의 리스트 추가
print(odd_list)
# range 함수
