def find_index(ary, data):
    pos = -1
    for i in range(len(ary)):
        if ary[i] == data:
            pos = i
            break
        elif ary[i] > data:
            break
    return pos


data_array = [188, 150, 168, 162, 105, 120, 177, 50]
find_data = int(input())
data_array = sorted(data_array)

print(find_index(data_array, find_data))
