# 정렬
# 배열에서 최솟값 위치를 찾는 함수
def find_index(array):
    pindex = 0
    for i in range(len(array)):
        if array[pindex] > array[i]:
            pindex = i
    return pindex

test = [10, 20, 30, 40, 50]
min = find_index(test)
print(test[min])