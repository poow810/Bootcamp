import random


def find_index(ary, data):
    start = 0
    end = len(ary)-1
    while start <= end:
        mid = (start+end)//2
        if ary[mid] == data:
            return mid
        elif ary[mid] > data:
            end = mid - 1
        else:
            start = mid + 1
    return -1


menu = ['바나나맛우유', '레쓰비 캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sell = [random.choice(menu) for i in range(20)]
count_list = []

print(f"오늘 판매된 전체 물건 --> {sell}")
sell.sort()
print(f"오늘 판매된 전체 물건 --> {sell}")
sell_list = list(set(sell))
print(f"오늘 판매된 전체 물건 종류--> {sell}")

for product in sell_list:
    count = 0
    pos = 0
    while True:
        pos = find_index(sell, product)
        if pos != -1:
            count+=1
            del(sell[pos])
        else:
            break
    count_list.append((product, count))

print(count_list)