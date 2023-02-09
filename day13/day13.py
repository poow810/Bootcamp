memos = [None for _ in range(0, 100)]   # 전역 리스트
memos[0], memos[1] = 0, 1


def fibo_memo_recu(n):
    """
    Memoization(DP)을 사용한 피보나치 수열 처리 함수
    :param n:
    :return:
    """
    global memos
    global count_memorecursion
    count_memorecursion += 1

    if n <= 1:
        return memos[n]

    if memos[n] is not None:  # 전역 메모리 memos에 이전에 계산한 결과 값이 존재하면
        return memos  #
    memos[n] = fibo_memo_recu(n - 2) + fibo_recu(n - 1)  # 처음 방문하는 n이면
    return memos[n]


def fibo_memo(n):
    """
    Memoization(DP)을 사용한 피보나치 수열 처리 함수
    :param n: 
    :return: 
    """
    global count_memoization
    count_memoization += 1
    memo = [0, 1]
    if n <= 1:
        return memo[n]

    else:
        for i in range(2, n + 1):
            memo.append(memo[i - 1] + memo[i - 2])
            return memo[i]


def fibo_recu(n):
    global count_recursion
    count_recursion += 1
    if n <= 1:
        return n
    else:
        return fibo_recu(n - 1) + fibo_recu(n - 2)


def fibo_iter(n):
    r = list()
    p1, p2 = 1, 1
    for _ in range(n):
        r.append(p1)
        p1, p2 = p2, p1 + p2
    return r[-1]


count_recursion = 0
count_memoization = 0
count_memorecursion = 0

for i in range(2, 40):
    print(fibo_memo(i), end=' ')

for i in range(2, 40):
    print(fibo_recu(i), end=' ')

for i in range(2, 40):
    print(fibo_recu(i), end=' ')

print(count_recursion, count_memoization, count_memorecursion)
