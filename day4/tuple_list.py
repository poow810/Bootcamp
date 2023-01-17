# tuple
a = 'harry',
b = ('harry',)
c = ()      # empty tuple
d = 'harry', 'ron'  # packing
e = ('hermione')  # string
f = ('harry', 'ron')  # packing
g = ('hermione',)  # string
print(id(g))    #id값이 다름
print(f[1])
x, y = f    # unpacking
g = f+g     # 덮어쓰기
print(id(g))    #id값이 다름
print(g)


# tuple 비교하기 - 원소 개수 비교
a = (7, 2)
b = (7, 2, 9)
print(a == b)

# list
scores = ('B+', 'A+', 'C+')
print(scores[1], scores[2])
temp = list(scores)
temp[1]='C+'
temp[2]='A+'
scores = tuple(temp)
print(scores[1], scores[2])     # tuple값을 list로 변환, 수정 후 다시 tuple로

# list
big_bang = ['GD', '태양', '탑', '대성', '승리']
# big_bang.append('인하')         # append는 맨 뒤에 넣음

big_bang.insert(1, '인하')        # insert는 특정 위치에 넣음
# print(big_bang)
exo = ['백현', '첸']
# exo.extend(big_bang)       # 서로 다른 리스트를 병합
# print(exo)
exo.append(big_bang)         # 리스트안에 리스트가 들어오도록 추가
print(exo)
print(exo[2][2])             # 첫 리스트 1번에 있는 리스트 2번을 호출
print(exo[-1][-4])
exo[-2] = '시우민'
# 삭제하기
# print(exo.pop())         # 빅뱅 다 날라감 #pop은 맨 뒤 삭제 후 return
print(exo[2].pop())
print(exo)
print(exo[2].pop(-2))
print(exo)
del exo[2][-1]      # 대성 delate
print(exo)

exo[2].remove('인하')
print(exo)
exo.clear()
print(exo)