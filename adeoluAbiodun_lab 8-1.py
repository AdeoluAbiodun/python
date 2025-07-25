# Name: Adeolu Abiodun  ||  Date: 01/30/2025  ||  Program file: adeoluAbiodun_lab7-1.py

'''# Program Description/Purpose: This Pig Latin python program accepts an input (sentence) and converts each word to Pig Latin. The program will keep running until the user presses enter without typing anything.

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
    '''
'''
# Name: Adeolu Abiodun  ||  Date: 04/10/2025  ||  Program file: adeoluAbiodun_lab13-2.py

# This modular Python GUI program allows users to select any or all services offered by Joe's Automotive and displays the total charges accordingly.
import tkinter as tk

# Define service charges
services = {
    "Oil change": 30,
    "Lube job": 20,
    "Radiator flush": 40,
    "Transmission flush": 100,
    "Inspection": 35,
    "Muffler replacement": 200,
    "Tire rotation": 20
}

class JoesAutomotiveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Joe's Automotive Services")
        self.service_vars = {}

        # Create check buttons for each service
        row = 0
        for service, cost in services.items():
            var = tk.BooleanVar()
            cb = tk.Checkbutton(root, text=f"{service} (${cost})", variable=var)
            cb.grid(row=row, column=0, sticky='w', padx=10, pady=2)
            self.service_vars[service] = var
            row += 1

        # Button to calculate total
        calc_button = tk.Button(root, text="Calculate Total", command=self.calculate_total)
        calc_button.grid(row=row, column=0, pady=10)

        # Label to display total
        self.total_label = tk.Label(root, text="Total: $0")
        self.total_label.grid(row=row + 1, column=0, pady=5)

    def calculate_total(self):
        total = sum(cost for service, cost in services.items() if self.service_vars[service].get())
        self.total_label.config(text=f"Total: ${total}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = JoesAutomotiveApp(root)
    root.mainloop()

    '''
