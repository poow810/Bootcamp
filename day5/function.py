# function

def isprime(n):
    """
    n이 소수인지의 여부 판단
    :param n: integer number
    :return: True or False
    """
    if n <= 1:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    else:
        return True

help(isprime)
start = int(input("start number : "))
end = int(input("end number : "))
if end < start:
    start, end = end, start
for i in range(start, end + 1):
    if isprime(i):
        print(i, end=', ')
