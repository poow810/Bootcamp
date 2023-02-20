def find_index(ary, data):
    pos = -1
    position = [x for x in range(len(ary)) if ary[x] == data]
    return position


data_array = [188, 50, 150, 168, 50, 162, 105, 120, 177, 50]
find_data = 50

print(find_index(data_array, find_data))