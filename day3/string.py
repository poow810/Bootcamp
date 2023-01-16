univ = 'Inha University'
print(univ[-10:-6])
print(univ[5:-6])
print(univ[::2])
print(univ[5:])
print(univ[5:15])
print(univ[-10:])

# len - 문자열의 개수
print(len(univ))

# split - 문자열을 리스트로 나눔
print(univ.split())  # 띄어쓰기를 기준으로 하여 두 개로 나눈다.

print(univ.split('i'))  # i를 기준으로 구분

# join - 리스트를 하나의 문자로 합침
pokemons = ['피카츄', '꼬부기', '파이리']
pokemons_string = ', '.join(pokemons)
print(pokemons_string)

# replace - 대체하기
inha = 'a duck goes into a sea'
print(inha.replace('a ', 'a famous '))

# strip - 제거
subjects = ' $ python, data structure, database    $$$'
print(subjects.strip())  # 맨 끝의 반복적으로 진행될 때 중복 제거
                         # 중간에 있는건 제거 안됨

# find, index - 문자열 찾기
print(subjects.find('data'), subjects.index('data'))  # 앞에서부터
print(subjects.rfind('data'), subjects.rindex('data'))  # 뒤에서부터
print(subjects.find('inha')) # -1 반환
# print(subjects.index('inha')) # exception

# title - 앞 글자만 대문자
print(subjects.title())

# 연습문제 5-1번
song = """When an eel grabs your arm,
... And it causes great harm,
... That's - a moray!"""
word = song.split()
word[16] = word[16].title()
song_string = ' '.join(word)
print(song_string)

# 연습문제 5-2번
question = []

# 연습문제 5-3번
print("My kitty cat likes %s, \nMy kitty cat like %s, \nMy kitty cat fell on his %s And now thinks he's a %s" % ('roast beef', 'ham', 'head', 'clam'))


