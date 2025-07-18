# Name: Adeolu Abiodun  ||  Date: 04/06/2025  ||  Program file: adeoluAbiodun_lab 13_1.py

# This modular GUI Python program converts Celsius temperatures to Fahrenheit based on user input, using the conversion formula: F = (9/5) × C + 32


import tkinter as tk


class TemperatureConverter: # Creating a class for the assignment
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Celsius to Fahrenheit Converter")

        self.label1 = tk.Label(self.window, text="Enter Celsius temperature:")
        self.label1.pack()

        self.celsius_entry = tk.Entry(self.window)
        self.celsius_entry.pack()


        self.middle_frame = tk.Frame(self.window)
        self.middle_frame.pack()

        self.converted_label = tk.Label(self.middle_frame, text="Converted to Fahrenheit:")
        self.converted_label.pack(side="left")

       
        self.display_var = tk.StringVar()
        self.display_label = tk.Label(self.middle_frame, textvariable=self.display_var)
        self.display_label.pack(side="left")

        
        self.convert_button = tk.Button(self.window, text="Convert", command=self.convert, relief="solid")
        self.convert_button.pack(side="left", padx=10, pady=10)

        self.quit_button = tk.Button(self.window, text="Quit", command=self.window.quit, relief="solid")
        self.quit_button.pack(side="left", padx=10, pady=10)

        
        self.window.mainloop()

    def convert(self):
        
        C = self.celsius_entry.get()

        try:
            C = float(C)
            F = (9/5) * C + 32
            self.display_var.set(f"{F:.2f} °F")
        
        except ValueError:
            self.display_var.set("Invalid input!")


if __name__ == "__main__":
    TemperatureConverter()
