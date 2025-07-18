# joel moore     11/2024    ch09_cardDeal.py
'''
this program deals a specified number of cards and counts the
total value of the cards

'''
# =========================  constants
TOTAL_CARDS=52

# =======================  imports
import random

# =====================  start the program

def main():
    # Create a deck of cards.
    values,suits = create_deck()

    # ====================Get the number of cards to deal.
    num_cards=99
    while num_cards <0 or num_cards>=TOTAL_CARDS:
        num_cards = int(input('How many cards should I deal? '))

    # Deal the cards.
    deal_cards(values,suits, num_cards)

# The create_deck function returns a dictionary
# representing a deck of cards.

def create_deck():
    # Create a dictionary with each card and its value stored as key-value pairs.
  
    values = {'Ace':1, '2':2, '3':3,'4':4, '5':5, '6':6,
            '7':7, '8':8, '9':9, '10':10, 'Jack':10,'Queen':10, 'King': 10}
        
    suits=['Diamonds','Hearts','Spades','Clubs']

    # Return the deck.
    return values, suits

# ====================deals a specified number of cards from the deck.

def deal_cards(values,suits, number):
    # =====================Initialize an accumulator for the hand value.
    hand_value = 0

    # =======================Deal the cards and accumulate their values.
    for count in range(number):
        card = random.choice(list(values))
        suit=random.choice(list(suits))
        print(card,suit)
        hand_value += values[card]

    # ======================Display the value of the hand.
    print(f'Value of this hand: {hand_value}')

# ========================Call the main function.
while True:
    if __name__ == '__main__':
        main()
        again=input('\ndeal again? 1=yes or press enter to stop ')
        if len(again)==0:
            break
        