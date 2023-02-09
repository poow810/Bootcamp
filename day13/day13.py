# 중앙값 계산
def mid_num(ary):
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


array = [1, 3, 10, 70, 90, 1000, 4000]
print(array[len(mid_num(array))//2])
