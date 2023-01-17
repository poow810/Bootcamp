# 7.5 ~ 7.6
things = ["mozzarella", "cinderella", "salmonella"]
things[-2] = things[-2].title()     # cinderella 첫 글자만 대문자로 변환
print(things)
things[0] = things[0].upper()       # mozzarella를 대문자로 변환
print(things)
things.pop(2)       # salmonella 제거
print(things)

