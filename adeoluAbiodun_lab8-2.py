# Name: Adeolu Abiodun  ||  Date: 01/30/2025  ||  Program file: adeoluAbiodun_lab8-2.py

# Program Description/Purpose: This python program reads the file's contents and calculates the average number of words per sentence.


import tkinter as tk
from tkinter import filedialog

def get_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a text file")
    return file_path

def read_file(filename):
    
    try:
        with open(filename, 'r') as file: # Reading the content the file and returning the lines as a list
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Here is for the program to calculate the average number of words per sentence/line
def Average_words(lines):
    if not lines:
        print("The file is empty or could not be read.")
        return None
    
    total_words = sum(len(line.strip().split()) for line in lines)
    total_sentences = len(lines)
    
    return total_words / total_sentences if total_sentences > 0 else 0

def main():
    file_name = get_file_path()
    
    if not file_name:
        print("No file selected. Please try again.")
        return
    
    lines = read_file(file_name)
    
    if lines is not None:
        avg_words = Average_words(lines)
        
        if avg_words is not None:
            print(f"For the input file > {file_name}")
            print(f"The average number of words per line is: {avg_words:.1f}")

if __name__ == "__main__":
    main()