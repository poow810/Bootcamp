import random
small = random.choice([True, False])
green = random.choice([True, False])
if small:
    if green:
        print('완두콩입니다.')
    else:
        print('체리입니다.')

else:
    if green:
        print('수박입니다')
    else:
        print('호박입니다')

#import random
# secret = random.randint(1, 10)
# guess = int(input('1~10사이의 수를 결정:'))
#
# if secret > guess:
#     print('too low')
# elif secret < guess:
#     print('too high')
# else:
#     print('just light')  # (f"~". ~{secret!}")
#
