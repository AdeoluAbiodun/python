# Name: Adeolu T. Abiodun  ||  Date: 02/13/2025  ||  Program file: AdeoluAbiodun_lab9-2.py
'''
Here is my lab9-2 Python program that:
1. Reads the contents of a text file,
2. Creates a dictionary where each unique word in the file serves as a key, 
3. Values are the number of occurrances of each word,
4. The program will display each word and the frequency as 5 columns
'''

from collections import Counter
from tkinter import Tk, filedialog

def select_file():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text Files", "*.txt")])
    return file_path

def process_file(filename):
    if not filename:
        print("No file selected. Exiting program.")
        return
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return
    
    # Remove punctuation and convert to lowercase
    words = text.replace(',', '').replace('.', '').split()
    word_counts = Counter(words)
    
    # Sort words alphabetically
    sorted_words = sorted(word_counts.items())
    
    # Print output in five columns
    print("Words and number of occurrences")
    print("-" * 60)
    
    col_count = 0
    for word, count in sorted_words:
        print(f"{word:<15}{count:<5}", end=' ')
        col_count += 1
        if col_count % 5 == 0:
            print()
    
    print("\nProgram is finished.")

# Run the function
file_path = select_file()
process_file(file_path)
