# 응용 예제 1 - 선택 정렬과 퀵 정렬의 성능 비교하기
import random
import time


def selection(ary):
    n = len(ary)
    for i in range(0, n-1):
        idx = i
        for j in range(i+1, n):
            if ary[idx] > ary[j]:
                idx = j
        temp = ary[i]
        ary[i] = ary[idx]
        ary[idx] = temp
    return ary


def quick_sort(ary, start, end):
    if start >= end:
        return
    low = start
    high = end

    pivot = ary[(low+high)//2]
    while low <= high:
        while ary[low] < pivot:
            low += 1
        while ary[high] > pivot:
            high -= 1
        if low <= high:
            ary[low], ary[high] = ary[high], ary[low]
            low, high = low+1, high - 1

    mid = low
    quick_sort(ary, start, mid-1)
    quick_sort(ary, mid, end)


count_array = [1000, 10000, 12000, 15000]
for i in count_array:
    temp = [random.randint(1,15000) for _ in range(i)]
    select = temp[:]
    quick = temp[:]

    print(f"## 데이터 수 --> {i}")
    start = time.time()
    selection(count_array)
    end = time.time()
    print(f"선택 정렬 --> {end-start:.3f}")
    start = time.time()
    quick_sort(count_array, 0, len(count_array)-1)
    end = time.time()
    print(f"퀵 정렬 --> {end-start:.3f}")

    i *= 5

