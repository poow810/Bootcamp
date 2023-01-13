import random

secret = random.randint(1, 10)
guess = random.randint(1, 10)
if secret > guess:
    print('too law')
elif secret < guess:
    print('too high')
else:
    print('just right')