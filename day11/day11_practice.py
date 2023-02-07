# 응용 예제 1 - 편의점에서 판매된 물건 목록 출력하기
import random


class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data, end=' ')
    inorder(node.right)


menu = ['레쓰비캔커피', '도시락', '삼각김밥', '코카콜라', '삼다수', '츄파춥스']
sell = [random.choice(menu) for i in range(20)]
print(f'오늘 판매된 물건(중복O) --> {sell}')

node = TreeNode()
node.data = sell[0]
root = node


for food in sell[1:]:
    node = TreeNode()
    node.data = food

    current = root
    while True:
        if food == current.data:
            break
        if food < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right

print('오늘 판매된 종류(중복X)--> ', end='')
print(inorder(root))

