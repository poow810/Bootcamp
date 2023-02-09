import tkinter as tk

memos = [None for _ in range(0, 100)]   # 전역 리스트
memos[0], memos[1] = 0, 1


def fibo_memo_recu(n):
    """
    Memoization(DP)을 사용한 피보나치 수열 처리 함수
    :param n:
    :return:
    """
    global memos

    if n <= 1:
        return memos[n]

    if memos[n] is not None:  # 전역 메모리 memos에 이전에 계산한 결과 값이 존재하면
        return memos[n]  #
    memos[n] = fibo_memo_recu(n - 2) + fibo_memo_recu(n - 1)  # 처음 방문하는 n이면
    return memos[n]


def fact_recursion(n):
    if n == 1:
        return 1
    else:
        return n*fact_recursion(n-1)


def factorial_input():
    lbl_results.config(text=f"팩토리얼 출력 결과 : {fact_recursion(int(en_num_input.get()))}")

def fibonacci_input():
    lbl_results.config(text=f"피보나치 출력 결과 : {fibo_memo_recu(int(en_num_input.get()))}")



win = tk.Tk()
win.title("Calculator")  # 피보나치, 팩토리얼 계산기
win.geometry("250x150")
en_num_input = tk.Entry()
lbl_results = tk.Label(text="계산기 출력 결과 :")  # 레이블, 계산 결과 출력용
btn_fact = tk.Button(text="팩토리얼", command = factorial_input)   # 팩토리얼 버튼, 이벤트 발생
btn_fibo = tk.Button(text="피보나치", command = fibonacci_input) # 피보나치 버튼, 이벤트 발생

en_num_input.pack()
lbl_results.pack()
btn_fact.pack(fill='x')
btn_fibo.pack(fill='x')
win.mainloop()





def fibo_memo(n):
    """
    Memoization(DP)을 사용한 피보나치 수열 처리 함수
    :param n: 
    :return: 
    """
    memo = [0, 1]
    if n <= 1:
        return memo[n]

    else:
        for i in range(2, n + 1):
            memo.append(memo[i - 1] + memo[i - 2])
        return memo[n]


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

for i in range(2, 30):
    print(fibo_memo(i), end=' ')

for i in range(2, 40):
    print(fibo_recu(i), end=' ')

for i in range(2, 30):
    print(fibo_recu(i), end=' ')

print(count_recursion, count_memoization, count_memorecursion)
