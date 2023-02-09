# 응용 예제 2 - 2차원 배열의 중앙값 찾기
def sort_array(ary):
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


array = [[53, 33, 250, 44],
         [88, 1, 67, 23],
         [199, 222, 38, 47],
         [155, 145, 20, 99]]
new_array = []
for i in range(len(array)):
    for j in range(len(array[i])):
        new_array.append(array[i][j])
print('1차원 변경 후, 정렬 전 -->', end= ' ')
print(new_array)
print('1차원 변경 후, 정렬 후 -->', end= ' ')
print(sort_array(new_array))
print(f"중앙값 --> {new_array[len(new_array)//2]}")