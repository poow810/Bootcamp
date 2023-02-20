def find_index(ary, data):
    pos = -1
    start = 0
    end = len(ary)-1
    while end >= start:
        mid = (start+end)//2
        if data == ary[mid]:
            return mid
        elif data > ary[mid]:
            start = mid + 1
        else:
            end = mid + 1



data_array = [188, 150, 168, 162, 105, 120, 177, 50]
find_data = int(input())
data_array = sorted(data_array)
position = find_index(data_array, find_data)
if position == -1:
    print("찾는 data가 data_array에 없음")
else:
    print(f"찾는 data가 {position}에 있음")