def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def fibo_iter(n):
    r = list()
    p1, p2 = 1, 1
    for _ in range(n):
        r.append(p1)
        p1, p2 = p2, p1+p2
    return r[-1]


print('피보나치 수 --> 0 1 ', end='')
for i in range(2, 40):
    print(fibo_iter(i), end=' ')
