# 퀵 정렬의 간단한 구현
def quick_sort(ary):
    n = len(ary)
    if n <= 1:
        return ary

    pivot = ary[n // 2]     # 중간값을 기준으로 지정
    left_array, right_array = [], []

    for num in ary:
        if num < pivot:
            left_array.append(num)
        elif num > pivot:
            right_array.append(num)
    return quick_sort(left_array) + [pivot] + quick_sort(right_array)


array = [188, 150, 168, 162, 105, 120, 177, 50]

print(quick_sort(array))