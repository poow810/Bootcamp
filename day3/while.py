# while & for 문
while True:
    dan = int(input('Dan (0 to quit):'))
    if dan == 0:
        break
    if 1 < dan < 10:
        for i in range(1, 10):
            print('{0} * {1} = {2}'.format(dan, i, dan * i))
    else:
        print('2에서 9사이의 값을 입력 하세요')


numbers = [2, 4, 6]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number %2 ==0:
        print('Found even number', number)
    position += 1
else:
    print('No even number found')

# break 문
word = 'thud'
for letter in word:
    if letter =='u':
        break
    print(letter)

# range 함수

