# 간선 생성 후 정렬
from operator import itemgetter

edge_array = []
for i in range(size):
    for j in range(size):
        if G1.graph[i][k] != 0:
            edge_array.append(G1.graph[i][k], i, k)
edge_array = sorted(edge_array, key = itemgetter(0), reverse = True)

# 중복 간선 제거
new_array = []
for i in range(0, len(edge_array), 2):
    new_array.append(edge_array[i])

# 가중치가 높은 간선부터 제거
index = 0
start = new_array[index][1]
end = new_array[index][2]
G1.graph[start][end] = 0
G1.graph[end][start] = 0
del(new_array[index])