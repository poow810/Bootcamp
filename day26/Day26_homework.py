import random


def sequence_find(ary, data):
    global count
    pos = -1
    for i in range(len(ary)):
        count += 1
        if ary[i] == data:
            pos = i
            break
    return pos


def bin_find(ary, data):
    global count
    start = 0
    end = len(ary)-1
    while start <= end:
        count += 1
        mid = (start+end)//2
        if ary[mid] == data:
            return mid
        elif ary[mid] >= data:
            end = mid - 1
        else:
            start = mid + 1
    return -1


count = 0
data_list = [random.randint(0, 1000000) for i in range(1000000)]
data_sort = sorted(data_list)
find_data = 50

sequence = sequence_find(data_list, find_data)
if sequence != -1:
    print(f"순차 검색 --> {count}회")

count = 0
bin = bin_find(data_sort, find_data)
if bin != -1:
    print(f"이진 검색 --> {count}회")