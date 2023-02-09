# 10장 응용 예제 1번 - 진수 변환하기
def change(num ,n):
    if n < num:
        print(numbers[n], end=' ')
    else:
        change(num, n//num)
        print(numbers[n%num], end=' ')


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', 'A', 'B', 'C', 'D', 'F']
number = int(input())
change(2, number)