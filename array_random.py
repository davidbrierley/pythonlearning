import random

for x in range(1):
    chance = (random.randint(1,100))

    if chance > 35:
        print('You got through safely.')
    else:
        print('You Died.')
