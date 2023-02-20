import random

import numpy as np


def find_index(ary, data):
    global count
    pos = -1
    start = 0
    end = len(ary)-1
    while end >= start:
        count = count + 1
        mid = (start+end)//2
        if data == ary[mid]:
            return mid
        elif data > ary[mid]:
            start = mid + 1
        else:
            end = mid + 1
    return pos


data_array = np.random.randint(0, 100000, 100000)
data_array.sort()
find_data = np.random.randint(100000)
count = 0

position = find_index(data_array, find_data)
if position == -1:
    print("찾는 data가 data_array에 없음")
    print(f"{count}회 검색함")
else:
    print(f"찾는 data가 {position}에 있음")
    print(f"{count}회 검색함")
