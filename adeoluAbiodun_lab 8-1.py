# Name: Adeolu Abiodun  ||  Date: 01/30/2025  ||  Program file: adeoluAbiodun_lab7-1.py

# Program Description/Purpose: This Pig Latin python program accepts an input (sentence) and converts each word to Pig Latin. The program will keep running until the user presses enter without typing anything.

def pig_latin_converter(sentence):
    words = sentence.split()  # Split the sentence into different words
    pig_latin_words = []  # List to store the splitted words.

    for word in words:
        first_letter = word[0]  # The first letter
        rest_of_word = word[1:]  # The rest of the word minus the first letter
        pig_latin_word = (rest_of_word + first_letter + 'AY').upper()  # Convert to pig latin and uppercase
        pig_latin_words.append(pig_latin_word)  # Add to the list variable previously initiated.

    return ' '.join(pig_latin_words)

# Keep the program running until the user decides to stop
while True:
    user_input = input("Enter a string or press either enter or Space with Enter to stop the program: ")

    if user_input.strip() == "":
        print("Program stopped." + "\nThank you for using the program.")
        break

    pig_latin_output = pig_latin_converter(user_input)  # Convert input to Pig Latin
    print("Your input converted to upper-case pig latin is as follows:")
    print(pig_latin_output)
    print()