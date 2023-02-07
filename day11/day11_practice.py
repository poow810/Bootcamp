# 응용 예제 02 - 콜센터의 응답 대기 시간 계산하기
def is_queue_empty():
    global waiting, Size, front, rear
    if front == rear:
        return True
    else:
        return False


def is_quene_full():
    global waiting, Size, front, rear
    if front == (rear+1) % Size:
        return True
    else:
        return False


def en_queue(data):
    global calling, Size, front, rear

    if is_quene_full():
        return
    rear = (rear+1) % Size
    calling[rear] = data


def de_queue():
    global calling, Size, front, rear

    if is_queue_empty():
        return
    front = (front+1) % Size
    data = calling[front]
    calling[front] = None
    return data


def wait_time():
    global calling, Size, front, rear
    time = 0
    for i in range((front+1)%Size, (rear+1)%Size):
        time = time + calling[i][1]
    return time



Size = 6
calling = [None for _ in range(Size)]
front = rear = 0

if __name__ == "__main__":
    waiting = [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3)]

    for call in waiting:
        print(f"귀하의 대기 예상시간은 {wait_time()} 분입니다.")
        print(f"현재 대기 콜 --> {calling}")
        en_queue(call)
        print()

    print(f"최종 대기 콜 --> {calling}")
    print("프로그램 종료!")