#python program to shuffle a deck of cards and draw 5 cards using itertools and random module

#import modules
import random
import itertools

#make a decks of card
deck = list(itertools.product(range(1,14),['Spades','Diamond','Hearts','Club']))
'''we use product() function to create a deck of cards.This function providdes a cartesian product of two sequences.these
two sequences can be nos ranging from 1 to 14 and 4 suites.So althogether we have 
13*4 = 52 items in the deck with each card as a tuple.eg- deck[0]=(1,'Spades')'''

#shuffle the deck of cards.
random.shuffle(deck)

#draw five cards.
print("YOUR CARDS ARE:")
for i in range (5):
	print(deck[i][0],'of',deck[i][1])
