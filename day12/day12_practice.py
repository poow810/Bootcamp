# 응용 예제 1 - 허니버터칩이 가장 많이 남은 편의점 찾기
class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


# graph 출력함수
def print_graph(g):
    print(' ', end=' ')
    for i in range(gsize):
        print("%7s"%store_array[i][0], end='')
    print()
    for j in range(gsize):
        print("%9s"%store_array[j][0], end=' ')
        for k in range(gsize):
            print("%3d"%g.graph[j][k], end=' ')
        print()




# 전역 변수 설정
G1 = None
store_array = [["Gs25", 30], ["CU", 60], ["Seven", 10], ["Mini", 90], ["Emart", 40]]
Gs25, CU, Seven, Mini, Emart = 0, 1, 2, 3, 4
stack = []
visit_array = []

gsize = 5
G1 = Graph(gsize)
G1.graph[0][1] = 1; G1.graph[0][2] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1; G1.graph[1][3] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][1] = 1; G1.graph[3][2] = 1; G1.graph[3][4] = 1
G1.graph[4][3] = 1
# 방문
current = 0
max_snack = current     # 편의점 번호를 0으로 지정해놓고 서로 다른 편의점 방문할 때마다 크기 비교
max_count = store_array[current][1]
stack.append(current)
visit_array.append(current)

while len(stack) != None:
    next = None
    for i in range(gsize):
        if G1.graph[current][i] == 1:
            if i in visit_array:
                pass
            else:
                next = i
                break

    if next != None:
        current = next
        stack.append(current)
        visit_array.append(current)
        if store_array[current][1] > max_count:
            max_count = store_array[current][1]
            max_snack = current
    else:
        current = stack.pop()
        break        # stack에서 아예 추출할 data가 없을 때까지 pop()을 해서 오류 발생 break 사용


print("## 편의점 그래프 ##")
print_graph(G1)
print(f"허니 버터칩 최대 보유 편의점 --> {store_array[max_snack][0],store_array[max_snack][1]}")