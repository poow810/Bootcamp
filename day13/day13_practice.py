# 응용 예제 1 - 성적별로 조 편성하기
def find_index(ary):
    n = len(ary)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if ary[j-1][1] > ary[j][1]:
                ary[j-1], ary[j] = ary[j], ary[j-1]
    return ary


array = [['선미', 88], ['초아', 99], ['화사', 71],
         ['영탁', 78], ['영웅', 67], ['민호', 92]]
print("정렬 전 --> ", end=' ')
print(array)
print("정렬 후 --> ", end=' ')
print(find_index(array))
print("## 성적별 조 편성표 ##")
for i in range(0, len(array)//2):
    print(f"{array[i][0]} : {array[len(array)-i-1][0]}")
