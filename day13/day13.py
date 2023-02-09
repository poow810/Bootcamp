# 퀵 정렬의 일반적인 구현
def quick_sort(ary, start, end):
    if end <= start:
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
            low, high = low +1, high -1

    mid = low
    quick_sort(ary, start, mid-1)
    quick_sort(ary, mid, end)
    return ary


array = [188, 150, 168, 162, 105, 120, 177, 50]
print(quick_sort(array, 0, len(array)-1))