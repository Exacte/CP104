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

CARDS = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
SUITS = 4
DEALT = 5

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
        for j in range(1, len(CARDS) + 1):
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
        print("{} ".format(CARDS[card - 1]), end="")
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
    print("{}----{}".format(print_hand(hand1), poker_hand(hand1)))
    print("{}----{}".format(print_hand(hand2), poker_hand(hand2)))
    print("{}----{}".format(print_hand(hand3), poker_hand(hand3)))
    print("{}----{}".format(print_hand(hand4), poker_hand(hand4)))
    print("{}----{}".format(print_hand(hand5), poker_hand(hand5)))
    print_hand(deck)

def poker_hand(phand):
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
    x = 0
    y = 1
    count = 13
    evalute = ""
    while x < DEALT:
        while y < DEALT:
            if phand[x] == phand[y]:
                evalute = "Loser"   
            y += 1
        x += 1
    
    if evalute != "Loser":
        while count > DEALT:
            if phand[DEALT-1] == count:
                evalute = "{}".format(CARDS[count-1])
            elif phand[DEALT-1] == (DEALT-1):
                evalute = "Wheel"
            count -= 1
    if evalute == "Loser" or evalute == "Wheel":
        return evalute
    else:
        evalute = " {} Low".format(evalute)
        return evalute
            
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
ask = "Y"
while ask != "N":
    deck = create_deck()
    full_deal(deck, DEALT)
    ask = input("Play again(Y/N)? ")
    ask = ask.upper()