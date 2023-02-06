import random


class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()


def insert_nodes(find_data, insert_data):
    global head, current, pre
    if head.data == find_data:
        node = Node(insert_data)
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node

        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node(insert_data)
            node.link = current
            pre.link = node
            return

    node = Node(insert_data)
    current.link = node
    node.link = head


def delete_nodes(delete_data):
    global head, current, pre

    if head.data == delete_data:
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del current
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link
            del current
            return


def find_nodes(find_data):
    global head, current, pre

    current = head
    if current.data == find_data:
        return current

    while current.link != head:
        current = current.link
        if current.data == find_data:
            return current

    return Node(None)


def is_find(find_data):
    """

    :return: 연결 리스트안에서 원소가 존재하면 True리턴 아니면 False
    :param find_data: 찾고자 하는 원소, str
    """
    global head, current, pre

    current = head
    if current.data == find_data:
        return True

    while current.link != head:
        current = current.link
        if current.data == find_data:
            return True

    return False


def count_odd_even():
    global head, current

    even, odd = 0, 0

    current = head
    while True:
        if current.data % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
        if current.link == head:
            break
        current = current.link

    return odd, even


def count_plus_minus():
    global head, current

    plus, minus, zero = 0, 0, 0

    current = head
    while True:
        if current.data > 0:
            plus = plus + 1
        elif current.data < 0:
            minus = minus + 1
        else:
            zero = zero + 1
        if current.link == head:
            break
        current = current.link

    return plus, minus, zero


def makeSquareNumber(odd, even):
    if odd > even:
        remainder = 1
    else:
        remainder = 0

    current = head
    while True:
        if current.data % 2 == remainder:
            current.data = current.data * current.data
        if current.link == head:
            break
        current = current.link


def makeSignToggle():
    current = head
    while True:
        current.data = current.data * -1
        if current.link == head:
            break
        current = current.link


head, current, pre = None, None, None
data_array = []

if __name__ == "__main__":
    for _ in range(7):
        data_array.append(random.randint(-10, 10))

        node = Node(data_array[0])
        head = node
        node.link = head

        for data in data_array[1:]:
            pre = node
            node = Node(data)
            pre.link = node
            node.link = head

    print_nodes(head)
    plus_minus_zero = count_plus_minus()
    print(f'+ : {plus_minus_zero[0]}, - : {plus_minus_zero[1]}, 0 : {plus_minus_zero[2]}')
    # makeSquareNumber(odd_even[0], odd_even[1])
    makeSignToggle()
    print_nodes(head)

    # print_nodes(head)
    # delete_nodes("피카츄")
    # print_nodes(head)
    # delete_nodes("파이리")
    # print_nodes(head)
    # delete_nodes("어니부기")
    # print_nodes(head)

    # print_nodes(head)
    # insert_nodes("피카츄", "잠만보")
    # print_nodes(head)
    # insert_nodes("파이리", "어니부기")
    # print_nodes(head)
    # insert_nodes("성윤모", "거북왕")
    # print_nodes(head)
