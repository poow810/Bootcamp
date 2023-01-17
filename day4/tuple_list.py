# list
# shallow copy
a = [1, 2, [5, 6]]
b = a.copy()
c = list(a)
d = a[:]
a[1] = -77          # immutable한 원소가 변경되면 복사본은 변경 x
a[2][1] = '7'       # 리스트 자체의 원소가 변경되면 복사본들도 변경 = 얕은 복사
print(a, b, c, d)       # 나머지 복사본들은 바뀌지 않음

# deep copy
import copy
a = [1, 2, [5, 6]]
b = copy.deepcopy(a)
a[2][1] = 7
print(a, b)         # 복사본은 바뀌지 않음

primes = [2, 19, 3, 5, 7, 11]
primes_cp = primes
print(primes)
print(primes_cp)
primes[-1] = 'lunch time'
print(primes)
print(primes_cp)

# mixed = [6, 4, 5, 'A+', 7, '트와이스', '8', 'b', '마마무'] # type error
# mixed = ['6', '4', '5', 'A+', '7', '트와이스', '8', 'b', '마마무']
# mixed.sort()
# mixed.sort(reverse=True)
# print(mixed)
