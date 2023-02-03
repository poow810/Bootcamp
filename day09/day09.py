def insert_data(index, pokemon):
    """
    선형 리스트 index 위치에 data 삽입
    :param index: int
    :param pokemon: str
    :return: void
    """
    if index < 0 or index > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons) - 1, index, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[index] = pokemon  # 지정한 위치에 친구 추가


def delete_data(index):
    """
    선형 리스트 index 위치의 원소 삭제
    :param index: int
    :return: void
    """
    if index < 0 or index > len(pokemons):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    pokemons[index] = None  # 데이터 삭제
    len_pokemons = len(pokemons)

    for i in range(index + 1, len_pokemons):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None

    pokemons.pop()


def add_data(pokemon):
    """
    선형 리스트 맨 뒤에 원소 삽입
    :param pokemon: str
    :return:
    """
    pokemons.append(None)
    pokemon_len = len(pokemons)
    pokemons[len(pokemons) - 1] = pokemon


pokemons = []
menu = -1
if __name__ == "__main__":
    while True:

        menu = input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> ")

        if menu == '1':
            data = input("추가할 데이터--> ")
            add_data(data)
            print(pokemons)
        elif menu == '2':
            pos = int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(pos, data)
            print(pokemons)
        elif menu == '3':
            pos = int(input("삭제할 위치--> "))
            delete_data(pos)
            print(pokemons)
        elif menu == '4':
            print(pokemons)
            break
        else:
            print("1~4 중 하나를 입력하세요.")
            continue
