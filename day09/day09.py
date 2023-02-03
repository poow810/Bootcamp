# 함수 선언 부분
def find_and_insert_data(friend, count):
    """
    다항식을 포맷에 맞게 출력하는 함수
    :param px: 계수를 가진 list
    :return: 다항식 문자열
    """
    findPos = -1        # index를 맨 뒷자리 (-1)로 출발
    for i in range(len(px)):
        pair = px[i]
        if count >=pair[1]:     # pair는 0에 friend, 1에 count
            findPos = i         # 입력된 count가 pair 1번인 count보다 클 때, break
            break
    if findPos == -1:       # 맨 뒷자리에 배치
        findPos = len(px)

    insert_data(findPos, (friend, count))       # insert(index, 입력할 요소)


def insert_data(position, friend):
    """
    다항식의 산술연산을 계산하는 함수
    :param x_val: x값 integer
    :param px: 계수를 원소로 가지고 있는 list
    :return: 다항식의 계산 결과 값
    """
    px.append(None)

    for i in range(len(px)-1, position, -1):    # 배열에 원하는 위치에
        px[i] = px[i - 1]                       # 요소를 입력하기
        px[i - 1] = None

    px[position] = friend


# 전역 변수 선언 부분
px = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]

# 메인 코드 부분
if __name__ == "__main__":
    friend = input("추가할 친구-->")
    count = int(input("카톡 횟수-->"))
    find_and_insert_data(friend, count)
    print(px)


