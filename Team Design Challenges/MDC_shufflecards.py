import random

suits = ['C', 'D', 'H', 'S']
values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

deck = []
player_hand = []
computer_hand = []

for value in values:
    for suit in suits:
        deck.append(str(value) + suit)

deck_shuffled = deck[:]
random.shuffle(deck_shuffled)

print('Starting deck:', deck)
print('Shuffled deck:', deck_shuffled)

for card in range(5):
    player_hand.append(deck_shuffled[card])
    deck_shuffled.pop(card)

for card in range(5):
    computer_hand.append(deck_shuffled[card])
    deck_shuffled.pop(card)

print('Your hand:', player_hand)
print('Computer\'s hand:', computer_hand)
print('Remaining deck:', deck_shuffled)

