# 응용 예제 01 - 유명 맛집의 대기줄 구현하기
def is_queue_empty():
    global waiting, Size, front, rear
    if front == rear:
        return True
    else:
        return False


def is_quene_full():
    global waiting, Size, front, rear
    if rear == Size - 1:
        return True
    else:
        return False


def de_queue():
    global waiting, Size, front, rear

    if is_queue_empty():
        return
    front += 1
    data = waiting[front]
    waiting[front] = None

    for i in range(front+1, rear+1):
        waiting[i-1] = waiting[i]
        waiting[i] = None
    front = -1
    rear -= 1

    return data


waiting = ['정국', '뷔', '지민', '진', '슈가']
Size = 5
front = -1
rear = 4

if __name__ == "__main__":
    print(f"대기 줄 상태 : {waiting}")
    for j in range(Size):
        print(f"{de_queue()}님 식당에 들어감")
        print(f"대기 줄 상태 : {waiting}")
    print("식당 영업 종료!")
