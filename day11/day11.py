# 간단 구현
# 데이터 삽입
queue = [None, None, None, None, None]
front = rear = -1
rear += 1
queue[rear] = "화사"
rear += 1
queue[rear] = "문별"
rear += 1
queue[rear] = "솔라"  # rear은 2인 상태

# 데이터 추출
front += 1
data = queue[front]
queue[front] = None   # queue의 0번째를 데이터로 추출 후 None

# 일반 구현
# 큐가 꽉 찼는지 확인하는 함수
def is_quene_full():
    global Size, queue, front, rear
    if (rear == Size-1):
        return True
    else:
        return False

# 큐가 비었는지 확인하는 함수
def is_queue_empty():
    global Size, queue, front, rear
    if (front == rear):
        return True
    else:
        return False
# 큐에 데이터를 삽입하는 함수
def en_queue():
    global Size, queue, front, rear
    if (is_quene_full()):
        return
    rear += 1
    queue[rear] = data

# 큐의 데이터를 추출하는 함수
def de_queue():
    global Size, queue, front, rear
    if (is_queue_empty()):
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

# 큐에서 front+1 위치의 데이터를 확인하는 함수
def peek():
    global Size, queue, front, rear
    if (is_queue_empty()):
        return
    return queue[(front+1)]