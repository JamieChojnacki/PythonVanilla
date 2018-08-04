import random

colors = ['Red', 'Black', 'Green']


""" 10 itterations with 18:18:2 chances """
# choices = random.choices(colors, weights=[18,18,2], k=10)
# print(choices)
#
# if 'Green' in choices:
#      print('winner')
# else:
#     print('looser')


""" lets work with ints """
deck = list(range(1,53))

# random.shuffle(deck)
hand = random.sample(deck, k=5)  # unique 5 card hand
print(hand)