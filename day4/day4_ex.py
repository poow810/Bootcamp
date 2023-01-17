# 8.1
ef2 = {'dog' : 'chine', 'cat' : 'chat', 'walrus' : 'morse'}
print(ef2)

# 8.2
print(ef2['walrus'])

# 8.3
list(ef2.items())
f2e = dict(ef2)
print(f2e)

# 8.4
for k, v in ef2.items():
    print(k)
    break       #break로 멈추는 방법 말고 첫번째만 얻는 방법?
print(list(ef2.keys())[0])

# 8.5
for k in ef2.keys():
    print(k, end=" ")