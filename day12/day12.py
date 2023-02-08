# 개선된 무방향 그래프
class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


G1 = None
name = ['문별', '솔라', '휘인', '쯔위', '선미', '화사']


def print_graph(g):
    print(' ', end=' ')
    for i in range(g.size):
        print(name[i], end=' ')
    print()
    for row in range(g.size):
        print(name[row], end=' ')
        for col in range(g.size):
            print(name[row][col], end=' ')
        print()
    print()
