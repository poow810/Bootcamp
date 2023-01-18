# 8.11
set = {number for number in range(10) if number%4 == 1}
print(set)

# 8.12
set = (x for x in range(10) if x%4 == 1)
for i in set:
    print(i)
    print('Got')

# 8.13
a = 'optimist', 'pessimist', 'troll'
b = 'The glass is half full', 'The glass is half empty', 'How did you get a glass?'
dict(zip(a, b))

# 8.14
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a mon ster', 'A haunted yarn shop']
movies = list(zip(titles, plots))

