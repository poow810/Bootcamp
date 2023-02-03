# 3-1
# 선형 리스트

# 3-2
# 1

# 3-3
# 4 - 2 - 3 - 1

# 3-4
# katok[-1] = None

# 3-5
# del katok[-1]

# 3-6
# def add_data(friend) :
# katok.append(None)
# kLen = len(katok)
# katok[kLen-1] = friend

# 3-7
# 4

# 3-8
# 3

# 자동 삽입하기

def find_and_insert_data(pokemon, hp):
    findPos = -1
    for i in range(len(pokemons)):
        pair = pokemons[i]
        if hp >= pair[1]:
            findPos = i
            break
    if findPos == -1:
        findPos = len(pokemons)

    insert_data(findPos, (pokemon, hp))


def insert_data(position, pokemon):
    if position < 0 or position > len(pokemons):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    pokemons.append(None)

    for i in range(len(pokemons)-1, position, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[position] = pokemon


pokemons = [["꼬부기", 300], ["파이리", 200], ["피카츄", 100]]

if __name__ == "__main__":
        add = input("추가할 포켓몬--> ")
        hp = int(input("체력--> "))
        find_and_insert_data(add, hp)
        print(pokemons)
