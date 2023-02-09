# 응용 예제 2 - 이미 정렬된 줄에 끼어들기
# 이미 데이터가 정렬되어 있다면 버블 정렬이 효과적
import random
import time


def bubble(ary):
    n = len(ary)
    for i in range(n-1, 0, -1):
        changeYN = False
        for j in range(0, i):
            if ary[j] > ary[j+1]:
                ary[j], ary[j+1] = ary[j+1], ary[j]
                changeYN = True
        if not changeYN:
            break
    return ary


array = [random.randint(0,10000) for _ in range(100000)]
array.sort()

ranidx = random.randint(0, len(array)-1)
array.insert(ranidx, array[-1])
start = time.time()
bubble(array)
end = time.time()
print(f"버블 정렬이 걸린 시간 : {end-start}")
