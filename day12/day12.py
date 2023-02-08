# 자전거 도로 건설을 위한 간선 제거, 정리하는 함수
from operator import itemgetter


class Graph():
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g):
    print(' ', end=' ')
    for i in range(g.size):
        print(name[i], end=' ')
    print()
    for row in range(g.size):
        print(name[row], end=' ')
        for col in range(g.size):
            print(g.graph[row][col], end=' ')
        print()


# 얘는 code 갖고옴
def find_vertex(g, findVtx):
    stack = []
    visitedAry = []  # 방문한 노드

    current = 0  # 시작 정점
    stack.append(current)
    visitedAry.append(current)

    while len(stack) != 0:
        next = None
        for vertex in range(gSize):
            if g.graph[current][vertex] != 0:
                if vertex in visitedAry:  # 방문한 적이 있는 정점이면 탈락
                    pass
                else:  # 방문한 적이 없으면 다음 정점으로 지정
                    next = vertex
                    break

        if next != None:  # 다음에 방문할 정점이 있는 경우
            current = next
            stack.append(current)
            visitedAry.append(current)
        else:  # 다음에 방문할 정점이 없는 경우
            current = stack.pop()

    if findVtx in visitedAry:
        return True
    else:
        return False


G1 = None
name = ['춘천', '서울', '속초', '대전', '광주', '부산']
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5
gSize = 6
G1 = Graph(gSize)

G1.graph[춘천][서울] = 10
G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10
G1.graph[서울][속초] = 40
G1.graph[서울][대전] = 11
G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15
G1.graph[속초][서울] = 40
G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11
G1.graph[대전][속초] = 12
G1.graph[대전][광주] = 20
G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50
G1.graph[광주][대전] = 20
G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30
G1.graph[부산][광주] = 25

# 간선 정리 시작
edge_array = []
for i in range(gSize):
    for j in range(gSize):
        if G1.graph[i][j] != 0:
            edge_array.append([G1.graph[i][j], i, j])
edge_array = sorted(edge_array, key=itemgetter(0), reverse=True)

# 중복 간선 제거하기
new_array = []
for i in range(0, len(edge_array), 2):
    new_array.append(edge_array[i])

# 가중치가 높은 간선부터 제거
index = 0
while len(new_array) > gSize-1:  # 사이클이 되면 안되므로 간선 개수는 정점 개수-1이여야 함
	start = new_array[index][1]
	end = new_array[index][2]
	save = new_array[index][0]

	G1.graph[start][end] = 0
	G1.graph[end][start] = 0	# 양 방향 제거

	startname = find_vertex(G1, start)
	endname = find_vertex(G1, end)
	if startname and endname:
		del(new_array[index])
	else:
		G1.graph[start][end] = save
		G1.graph[end][start] = save
		index += 1

print_graph(G1)