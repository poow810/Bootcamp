def insert_data(index, pokemon):
    if index < 0 or index > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons) - 1, index, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[index] = pokemon  # 지정한 위치에 친구 추가


def delete_data(index):


        if index < 0 or index > len(pokemons):
            print("데이터를 삭제할 범위를 벗어났습니다.")
            return

        len_pokemons = len(pokemons)
        pokemons[index] = None  # 데이터 삭제

        for i in range(index + 1, len_pokemons):
            pokemons[i - 1] = pokemons[i]
            pokemons[i] = None

        del (pokemons[len_pokemons - 1])



if __name__ == "__main__":
    pokemons = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해씨"]
    print(pokemons)
#    insert_data(2, '어니부기')
    delete_data(1)  # 라이츄 지움
    print(pokemons)
    delete_data(6)
    print(pokemons)
