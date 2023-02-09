# 중복 값을 고려한 퀵 정렬
def quick_sort(ary):
    n = len(ary)
    if n <= 1:
        return ary

    pivot = ary[n//2]
    left_array, right_array, mid_array = [], [], []

    for num in ary:
        if num > pivot:
            right_array.append(num)
        elif num < pivot:
            left_array.append(num)
        else:
            mid_array.append(num)

    return quick_sort(left_array)+mid_array+quick_sort(right_array)
# mid_array는 함수로 반환하지 않는 이유?
# num = pivot 값으로 기준 값이기 때문에 기준이 변하면 안됨


array = [161, 2, 66, 90, 105, 144, 66, 161, 90]
print(quick_sort(array))