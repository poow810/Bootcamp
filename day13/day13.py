import random
# 재귀 함수를 통한 숫자 합계 내기
def add_number(num):
    if num <= 1:
        return 1
    return num+add_number(num-1)

# 팩토리얼을 재귀 함수로 구현
def factorial(num):
    if num <= 1:
        return 1
    return num*factorial(num-1)


# 배열의 합 계산하기
def array_sum(arr, n):
    if n <= 0:
        return arr[0]
    return arr[n]+array_sum(arr, n-1)


array = [random.randint(0, 255) for _ in range(10)]
print(array)
print(array_sum(array, len(array)-1))

