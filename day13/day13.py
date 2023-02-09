# 개선된 선택 정렬
def selection_sort(ary):
    n = len(ary)
    for i in range(0, n - 1):
        findex = i
        for j in range(i + 1, n):
            if ary[findex] > ary[j]:
                findex = j
        temp = ary[i]
        ary[i] = ary[findex]
        ary[findex] = temp
    return ary


array = [1, 12, 33, 4, 51, 6, 100, 25]
after_array = selection_sort(array)
print(after_array)
