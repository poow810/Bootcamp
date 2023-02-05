# 함수 선언 부분
class Node:
    def __init__(self):
        self.data = None
        self.link = None


def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.add, end =' ')
    while current.link != None:
        current = current.link
        print(current.add, end =' ')
    print()



memory = []
head, current, pre = None, None, None
dataArray = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해씨"]

# 메인 코드 부분
if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    print(print_nodes(head))