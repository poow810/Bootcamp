# 삽입 정렬 효율적 구현
def insertion(ary):
    n = len(ary)
    for i in range(0,n):
        for j in range(i, 0, -1):
            if ary[j-1] < ary[j]:
                ary[j-1], ary[j] = ary[j], ary[j-1]
    return ary

array = [15, 14, 17, 20, 66, 99]

new_array = insertion(array)
print(new_array)
