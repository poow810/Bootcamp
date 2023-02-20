def find_index(ary, data):
    pos = -1
    for i in range(len(ary)):
        if ary[i] == data:
            pos = i
            break
    return pos


data_array = [188, 150, 168, 162, 105, 120, 177, 50]
find_data = int(input())
position = find_index(data_array, find_data)
if position == -1:
    print("찾는 data가 array에 없습니다.")
else:
    print(f"찾는 data가 {position}에 있습니다.")