# 응용 예제 2 - 효율적인 케이블망 구성하기
from operator import itemgetter


class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range (size)]


def print_graph(g):
    print(' ', end=' ')
    for i in range(g.size):
        print(city[i], end = ' ')
    print()
    for j in range(g.size):
        print(city[j], end = ' ')
        for k in range(g.size):
            print("%2d"%g.graph[j][k], end = ' ')
        print()


def find_vertex(g, findvtx):
    stack = []
    visit_array = []
    current = 0
    stack.append(current)
    visit_array.append(current)

    while len(stack) != 0:
        next = None
        for i in range(g.size):
            if g.graph[current][i] != 0:
                if i in visit_array:
                    pass
                else:
                    next = i
                    break
        if next != None:
            current = next
            stack.append(current)
            visit_array.append(current)
        else:
            current = stack.pop()
    if findvtx in visit_array:
        return True
    else:
        return False


G1 = None
city = ['서울', '뉴욕', '북경', '방콕', '런던', '파리']
서울, 뉴욕, 북경, 방콕, 런던, 파리 = 0, 1, 2, 3, 4, 5

gsize = 6
G1 = Graph(gsize)
G1.graph[0][1] = 80; G1.graph[0][2] = 10
G1.graph[1][0] = 80; G1.graph[1][3] = 70; G1.graph[1][2] = 40
G1.graph[2][0] = 10; G1.graph[2][1] = 40; G1.graph[2][3] = 50
G1.graph[3][1] = 70; G1.graph[3][2] = 50; G1.graph[3][4] = 30; G1.graph[3][5] = 20
G1.graph[4][3] = 30; G1.graph[4][5] = 60
G1.graph[5][3] = 20; G1.graph[5][4] = 60
print_graph(G1)

edge_array = []
for i in range(gsize):
    for j in range(gsize):
        if G1.graph[i][j] != 0:
            edge_array.append([G1.graph[i][j], i, j])

edge_array = sorted(edge_array, key = itemgetter(0), reverse = False)
new = []
for i in range(0, len(edge_array), 2):
    new.append(edge_array[i])

index = 0
while len(new) > 5:
    start = new[index][1]
    end = new[index][2]
    save = new[index][0]

    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    point_start = find_vertex(G1, start)
    point_end = find_vertex(G1, end)

    if point_start and point_end:
        del(new[index])
    else:
        G1.graph[start][end] = save
        G1.graph[end][start] = save
        index += 1


print_graph(G1)