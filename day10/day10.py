# 함수 선언 부분
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()


def insert_nodes(find_data, insert_data):
    global head, current, pre

    if head.data == find_data:  # 첫 번째 노드 삽입
        node = Node(insert_data)
        node.link = head
        head = node
        return

    current = head
    while current.link != None:  # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node(find_data)
            node.link = current
            pre.link = node
            return


    node = Node(insert_data)  # 마지막 노드 삽입
    current.link = node

def delete_node(delete_data):
    global memory, head, current, pre

    if head.data == delete_data:
        print("첫 노드가 삭제됨")
        current = head
        head = head.link
        del current
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == delete_data:
            print("중간 노드가 삭제됨")
            pre.link = current.link
            del current
            return

    print("삭제된 노드가 없음")
    # 삭제할 데이터를 못찾는 경우에 함수 종료


def find_nodes(find_data):
    global memory, head, current, pre
    current = head
    if current.data == find_data:
        return current

    while current.link != None:
        current = current.link
        if current.data == find_data:
            return current

    return Node(None)


memory = []
head, current, pre = None, None, None
data_array = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해씨"]

# 메인 코드 부분
if __name__ == "__main__":
    node = Node(data_array[0])
    head = node

    for data in data_array[1:]:
        pre = node
        node = Node(data)
        pre.link = node

    print_nodes(head)
    insert_nodes("피카츄", "잠만보")
    print_nodes(head)
    insert_nodes("파이리", "어니부기")
    print_nodes(head)
    insert_nodes("성윤모", "거북왕")
    print_nodes(head)
    delete_node("잠만보")
    print_nodes(head)
    delete_node("어니부기")
    print_nodes(head)
    delete_node("강찬석")
    print_nodes(head)
    print(find_nodes("파이리").data)        # return을 node객체로 받았기 때문에
    print(find_nodes("박민석").data)        # .data로 출력 방식을 설정 해주어야함
