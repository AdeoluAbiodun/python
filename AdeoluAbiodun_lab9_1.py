# Name: Adeolu T. Abiodun  ||  Date: 02/12/2025  ||  Program file: AdeoluAbiodun_lab9_1.py

# This program deals a specified number of cards and counts the total value of the cards.

import random

# Constants
TOTAL_CARDS = 52

# Card values
CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
               'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
SUITS = ['Diamonds', 'Hearts', 'Spades', 'Clubs']

# Function to create and shuffle the deck dictionary
def create_deck():
    deck = [(rank, suit) for rank in CARD_VALUES.keys() for suit in SUITS]
    random.shuffle(deck)
    return deck

# Function to calculate the hand value
def calculate_hand_value(hand):
    value = sum(CARD_VALUES[card[0]] for card in hand)
    aces = sum(1 for card in hand if card[0] == 'Ace')
    
    while value > 21 and aces:
        value -= 10
        aces -= 1
    
    return value

# Function to play a round of blackjack
def play_blackjack(deck, wins):
    if len(deck) < 4:
        print("All cards have been dealt and the game is over")
        return False
    
    player1_hand = [deck.pop(), deck.pop()]
    player2_hand = [deck.pop(), deck.pop()]
    
    print(f"Player 1 was dealt {player1_hand[0][0]} of {player1_hand[0][1]}")
    print(f"Player 2 was dealt {player2_hand[0][0]} of {player2_hand[0][1]}")
    print(f"Player 1 was dealt {player1_hand[1][0]} of {player1_hand[1][1]}")
    print(f"Player 2 was dealt {player2_hand[1][0]} of {player2_hand[1][1]}")
    
    while True:
        value1 = calculate_hand_value(player1_hand)
        value2 = calculate_hand_value(player2_hand)
        
        if value1 >= 21 or value2 >= 21:
            break
        
        if len(deck) < 2:
            print("All cards have been dealt.")
            return False
        
        player1_hand.append(deck.pop())
        player2_hand.append(deck.pop())
        print(f"Player 1 was dealt {player1_hand[-1][0]} of {player1_hand[-1][1]}")
        print(f"Player 2 was dealt {player2_hand[-1][0]} of {player2_hand[-1][1]}")
    
    value1 = calculate_hand_value(player1_hand)
    value2 = calculate_hand_value(player2_hand)
    
    if value1 > 21 and value2 > 21:
        print("Both players busted. Dealer wins.")
        wins['dealer'] += 1
    elif value1 > 21:
        print("Player 2 wins.")
        wins['player2'] += 1
    elif value2 > 21:
        print("Player 1 wins.")
        wins['player1'] += 1
    elif value1 == 21 and value2 == 21:
        print("It's a tie! Both players win.")
        wins['ties'] += 1
    elif value1 == 21:
        print("Player 1 wins.")
        wins['player1'] += 1
    elif value2 == 21:
        print("Player 2 wins.")
        wins['player2'] += 1
    elif abs(21 - value1) < abs(21 - value2):
        print("Player 1 wins.")
        wins['player1'] += 1
    elif abs(21 - value2) < abs(21 - value1):
        print("Player 2 wins.")
        wins['player2'] += 1
    else:
        print("It's a tie!")
        wins['ties'] += 1
    
    input("Press Enter for next game...")
    return True

# Main function
def main():
    deck = create_deck()
    wins = {'player1': 0, 'player2': 0, 'ties': 0, 'dealer': 0}
    
    while play_blackjack(deck, wins):
        pass
    
    print("\nAll cards dealt ****** Final results ******")
    print(f"Player 1 won {wins['player1']} games")
    print(f"Player 2 won {wins['player2']} games")
    print(f"Tied games: {wins['ties']}")
    print(f"Dealer won {wins['dealer']} games")
    
    replay = input("Play again? 1=yes or press enter to end the program: ")
    if replay == '1':
        main()

if __name__ == '__main__':
    main()
