# # Chapter 4
# # 응용예제 1번
# class Node():
#     def __init__(self):
#         self.data = None
#         self.link = None
#
#
# def printNodes(first):
#     current = first
#     if current == None:
#         return
#     print(current.data, end = "")
#     while current.link != None:
#         current = current.link
#         print(current.data, end = "")
#
#
#
# def makeLinkList(information):
#     global head, current, pre, list
#
#     node = Node()
#     node.data = information
#     list.append(node)
#     if head == None:    # 새 노드가 처음일경우
#         head = node
#         return
#     if head.data[0] > information[0]:    # 새 노드의 정보가 첫 노드의 정보보다 빠를경우,
#         node.link = head                 # 새 노드의 링크에 첫 노드를 지정 후, 헤드 지정
#         head = node
#         return
#
#     current = head
#     while current.link != None:
#         pre = current
#         current = current.link
#         if current.data[1] > information[1]:
#             pre.link = node
#             node.link = current
#             return
#     current.link = node
#
#
# head, current, pre = None, None, None
# list = []
#
# if __name__=="__main__":
#     while True :
#         name = input("이름 : ")
#         if name == "":
#             break
#         email = input("이메일 : ")
#         makeLinkList([name, email])
#         printNodes(head)
# import random
#
#
# # 응용예제 2번 - 로또 추첨하기
# class Node():
#     def __init__(self):
#         self.data = None
#         self.link = None
#
#
# def print_node(first):
#     current = first
#     if current == None:
#         return
#     print(current.data, end=" ")
#     while current.link != None:
#         current = current.link
#         print(current.data, end=" ")
#
#
#
# def makeLottoList(number):
#     global list, head, current, pre
#
#     node = Node()
#     node.data = number
#     list.append(node)
#     if head == None:        # 새 노드가 첫 번째 노드일 때
#         head = node
#         return
#
#     if head.data > number:      # 새 노드가 첫 노드보다 작을 때
#         node.link = head        # 새 노드의 링크를 첫 노드에 지정, head가 첫 노드
#         head = node
#
#     current = head
#     while current.link != None:     # 중간 노드로 삽입할 때
#         pre = current
#         current = current.link
#         if current.data > number:   # 새 노드가 현재 노드보다 작을 경우 (number가 작음)
#             pre.link = node         # 이전 노드와 현재 노드 사이에 노드 삽입
#             node.link = current
#             return
#
#     current.link = node             # 새 노드가 가장 클 경우 마지막에 노드 삽입
#
#
# def findNumber(number):
#     global list, head, current, pre
#
#     if head == None:
#         return False
#     current = head
#     if current.data == number:
#         return True
#     while current.link != None:
#         current = current.link
#         if current.data == number:
#             return True             # 중복 번호일 경우 판단
#     return False
#
#
# list = []
# head, current, pre = None, None, None
#
# if __name__=="__main__":
#     count = 0
#     lottoCount = 6
#
#     while True:
#         lottoNumber = random.randint(1, 45)
#         if findNumber(lottoNumber):
#             continue
#         count+=1
#         makeLottoList(lottoNumber)
#         if count>=6:
#             break
#     print_node(head)

