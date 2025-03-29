# Name: Adeolu T. Abiodun  ||  Date: 02/27/2025  ||  Program file: AdeoluAbiodun_lab10-2.py

'''
This Python program creates a simple trivia game for two players, displays the number of 
points earned by each player, and declares the player with the highest number of points as the winner.
'''

import random

class Questions:
    def __init__(self, question, choices, correct_answer):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer
    
    def Ask_Question(self):
        print(f"\n{self.question}")
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")
        
        while True:
            try:
                answer = int(input("Enter the number of your answer: "))
                if 1 <= answer <= 4:
                    return answer == self.correct_answer
                else:
                    print("Invalid option. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

# List of the 10 trivia questions
Trivia_Questions = [
    Questions("How many days are in a lunar year?", ["354", "365", "243", "379"], 1),
    Questions("What is the largest planet?", ["Mars", "Jupiter", "Earth", "Pluto"], 2),
    Questions("What is the largest kind of whale?", ["Orca", "Humpback", "Beluga", "Blue"], 4),
    Questions("Which dinosaur could fly?", ["Triceratops", "Tyrannosaurus Rex", "Pteranodon", "Diplodocus"], 3),
    Questions("Which of these Winnie the Pooh characters is a donkey?", ["Pooh", "Eeyore", "Piglet", "Kanga"], 2),
    Questions("What is the hottest planet?", ["Mars", "Pluto", "Earth", "Venus"], 4),
    Questions("Which dinosaur had the largest brain compared to body size?", ["Troodon", "Stegosaurus", "Ichthyosaurus", "Gigantoraptor"], 1),
    Questions("What is the largest type of penguin?", ["Chinstrap", "Macaroni", "Emperor", "White-flippered"], 3),
    Questions("Which children's story character is a monkey?", ["Winnie the Pooh", "Curious George", "Horton", "Goofy"], 2),
    Questions("How long is a year on Mars?", ["550 Earth days", "498 Earth days", "126 Earth days", "687 Earth days"], 4)
]


random.shuffle(Trivia_Questions)


player_scores = [0, 0] # Initializing the player scores

# Game loop for two players
for i in range(5):
    print(f"\nPlayer 1's Turn (Question {i+1})")
    if Trivia_Questions[i].Ask_Question():
        print("Correct!")
        player_scores[0] += 1
    else:
        print("Incorrect answer!")
    
    print(f"\nPlayer 2's Turn (Question {i+6})")
    if Trivia_Questions[i+5].Ask_Question():
        print("Correct!")
        player_scores[1] += 1
    else:
        print("Wrong answer!")

# Display Final Scores
print("\nThe game is over")
print(f"Player 1 Score: {player_scores[0]}")
print(f"Player 2 Score: {player_scores[1]}")

# Here is where winner is determine
if player_scores[0] > player_scores[1]:
    print("Player 1 is the winner!")
elif player_scores[0] < player_scores[1]:
    print("Player 2 is the winner!")
else:
    print("It's a tie!")
