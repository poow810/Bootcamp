import math
import random


class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printStore(first):
    current = first
    if current == None:
        return

    while current.link != head:
        current = current.link
        x, y = current.data[1:]
        print(current.data[0], "편의점, 거리 : ", math.sqrt(x * x + y * y))


def makeStoreList(store):
    global head, current, pre, storeList

    node = Node()
    node.data = store
    storeList.append(node)

    if head == Node:
        head = node
        node.link = head
        return
    nodeX, nodeY = node.data[1:]
    node1 = math.sqrt(nodeX * nodeX + nodeY * nodeY)
    headX, headY = head.data[1:]
    node2 = math.sqrt(headX * headX + headY * headY)

    if node2 > node1:  # 새 노드가 헤드보다 작을 경우( 앞에 위치 )
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head  # 중간 노드로 삽입하는 경우
    while current.link != head:
        pre = current
        current = current.link
        curX, curY = current.data[1:]
        node3 = math.sqrt(curX * curX + curY * curY)
        if node3 > node1:  # 새 노드가 현재 노드보다 작을 경우
            pre.link = node
            node.link = current
            return

    current.link = node  # 가장 커서 맨 뒤에 노드 삽입
    node.link = head


head, current, pre = None, None, None
storeList = list()

if __name__ == "__main__":
    catalog = []
    storeName = 'A'
    for _ in range(10):
        store = (storeName, random.randint(1, 100), random.randint(1, 100))
        catalog.append(store)
        storeName = chr(ord(storeName) + 1)  # store이름을 하나씩 변경하는 함수

    for store in catalog:
        makeStoreList(store)

    printStore(head)
