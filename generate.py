#Using from
'''
from random import choice
coin = choice(["heads", "tails"])
print(coin)
'''

#Without using from 
'''
import random 
coin = random.choice(["heads", "tails"])

print(coin)
'''

#Using Randint
'''
import random
num = random.randint(0, 10)
print(num)
'''

cards = ['jack', 'queen', 'king']
random.shuffle(cards)
for card in cards:
    print(card)

import statistics
print(statistics.mean([100, 90]))