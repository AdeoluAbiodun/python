# Name: Adeolu Abiodun  ||  Date: 04/29/2025  ||  Program file: adeoluAbiodun_pc8.py

# This program accepts a sequence of comma separated 4 digit binary numbers, checks whether each is divisible by 5, and displays the results accordingly.

while True:
    userInput = input("\ninput binary numbers: ").split(",")

    result = [x for x in userInput if int(x, 2) % 5 == 0]

    print("\nBinary numbers divisible by 5 are show below: ")
    print(",".join(result) if result else "No values are divisible by 5")

    retry = input("\nTest another set of binary numbers? 1=yes OR ENTER to stop: ")
    if retry.strip() != "1":
        break
