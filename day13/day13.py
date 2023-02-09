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
        ary = ary[1:-2]
    return ary


array = [1, 36, 30, 70, 90, 1000, 4000]
print(mid_num(array))