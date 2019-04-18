"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-11-14
-------------------------------------------------------
"""
import random

CARDSLOW = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
CARDSHIGH = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
SUITS = 4

def create_deck():
    """
    -------------------------------------------------------
    Create a deck of cards, 4 times 13 values, A through K.
    -------------------------------------------------------
    Postconditions:
        returns:
        deck - a deck of cards (list of int)
    -------------------------------------------------------
    """
    deck = []

    for i in range(SUITS):
        for j in range(1, len(cards) + 1):
            deck.append(j)
    return deck

def deal(deck):
    """
    -------------------------------------------------------
    Deals a hand of cards.
    -------------------------------------------------------
    Preconditions:
        deck - a deck of cards (list of int)
        cards - the number of cards in the hand (int > 0, <= len(deck))
    Postconditions:
        returns:
        hand - a sorted hand of cards (list of int)
    -------------------------------------------------------
    """

    hand = []
    random.shuffle(deck)
    card = deck.pop()
    hand.append(card)
    return hand

def print_hand(hand):
    """
    -------------------------------------------------------
    Formatted print of a hand of cards.
    -------------------------------------------------------
    Preconditions:
        hand - a hand of cards (list of int)
    Postconditions:
        prints:
        The contents of hand separated by spaces
    -------------------------------------------------------
    """
    for card in hand:
        print("{} ".format(cards[card - 1]), end="")
    print()
    
def full_deal(deck, numb):
    """
    -------------------------------------------------------
    Formatted print of a hand of cards.
    -------------------------------------------------------
    Preconditions:
        hand - a hand of cards (list of int)
    Postconditions:
        prints:
        The contents of hand separated by spaces
    -------------------------------------------------------
    """
    hand1 = []
    hand2 = []
    hand3 = []
    hand4 = []
    hand5 = []
    for i in range(numb):
        hand1 += deal(deck)
        hand2 += deal(deck)
        hand3 += deal(deck)
        hand4 += deal(deck)
        hand5 += deal(deck)
    hand1.sort()
    hand2.sort()
    hand3.sort()
    hand4.sort()
    hand5.sort()
    print_hand(hand1)
    print_hand(hand2)
    print_hand(hand3)
    print_hand(hand4)
    print_hand(hand5)
    print_hand(deck)
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
numb = int(input("Number of cards in hand (0 to quit): "))
ask = input("Would you like an Ace High or Ace low deck(H/L):")
ask = ask.upper()
if ask == "H":
    cards = CARDSHIGH
elif ask == "L":
    cards = CARDSLOW

while numb > 0:
    deck = create_deck()
    full_deal(deck, numb)
    numb = int(input("Number of cards in hand (0 to quit): "))
    ask = input("Would you like an Ace High or Ace low deck(H/L):")