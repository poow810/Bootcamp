from operator import itemgetter


def make_index(ary, pos):
    """

    :param ary:
    :param pos:
    :return:
    """
    before_array = []
    index = 0
    for data in ary:
        before_array.append((data[pos], index))
        index += 1

    sorted_ary = sorted(before_array, key=itemgetter(0))
    return sorted_ary


def book_search(ary, f_data):
    """

    :param ary:
    :param f_data:
    :return:
    """
    pos = -1
    start = 0
    end = len(ary) - 1

    while start <= end:
        mid = (start + end) // 2
        if f_data == ary[mid][0]:
            return ary[mid][1]
        elif f_data > ary[mid][0]:
            start = mid + 1
        else:
            end = mid - 1

    return pos


book_ary = [['어린왕자', '쌩떽쥐베리'], ['이방인', '까뮈'], ['부활', '톨스토이'],
            ['신곡', '단테'], ['돈키호테', '세르반테스'], ['동물농장', '조지오웰'],
            ['데미안', '헤르만헤세'], ['파우스트', '괴테'], ['대지', '펄벅'], ['이것이 자바다', '신용권']]
name_index = []
auth_index = []

## 메인 코드 부분 ##
print('#책장의 도서 ==>', book_ary)
name_index = make_index(book_ary, 0)
print('#도서명 색인표 ==>', name_index)
auth_index = make_index(book_ary, 1)
print('#작가명 색인표 ==>', auth_index)

find_name = '신곡'
find_pos = book_search(name_index, find_name)
if find_pos != -1:
    print(find_name + '의 작가는 ' + book_ary[find_pos][1] + '입니다.')
else:
    print(find_name + '책은 없습니다.')

find_name = '괴테'
find_pos = book_search(auth_index, find_name)
if find_pos != -1:
    print(find_name + '의 도서는 '+ book_ary[find_pos][0] + '입니다.')
else:
    print(find_name + ' 작가는 없습니다.')
