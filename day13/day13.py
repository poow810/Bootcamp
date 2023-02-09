# 배열에서 자신이 삽입될 위치를 찾는 함수
def find_index(ary, data):
    findidx = -1
    for i in range(0, len(ary)):
        if ary[i] > data:
            findidx = i
            break
    if findidx == -1:       # 아무것도 못찾았을 경우에 맨 마지막 위치
        return [findidx]
    else:
        return [findidx]

test = [33, 40, 70]
print(find_index(test, 50))
