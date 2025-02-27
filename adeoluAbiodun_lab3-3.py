# Name: Adeolu Abiodun  ||  Date: 08/29/2024  ||  Program file: adeoluAbiodun_lab3-3.py

# Program Description/Purpose: This program is a time calculator. It asks the user to input a number of seconds and use it to calculate the number of days, hours, minutes and seconds from the input seconds

# Here are the constants
Seconds_In_A_Minute = 60
Seconds_In_An_Hour = 3600
Seconds_In_A_Day = 86400

# Ask user to enter number of seconds
Total_Seconds = int(input("Enter the number of seconds: "))

# Calculate the number of days, hours, minutes, and seconds
Days = Total_Seconds // Seconds_In_A_Day
remaining_seconds = Total_Seconds % Seconds_In_A_Day

Hours = remaining_seconds // Seconds_In_An_Hour
remaining_seconds = remaining_seconds % Seconds_In_An_Hour

Minutes = remaining_seconds // Seconds_In_A_Minute
Seconds = remaining_seconds % Seconds_In_A_Minute

# Output/display the results
print(f"\n{Total_Seconds} seconds is equal to:")
print(f"{Days} day(s)")
print(f"{Hours} hour(s)")
print(f"{Minutes} minute(s)")
print(f"{Seconds} second(s)")