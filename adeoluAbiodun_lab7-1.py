# Name: Adeolu Abiodun  ||  Date: 09/24/2024  ||  Program file: adeoluAbiodun_lab7-1.py

# Program Description/Purpose: This Python program uses the WorldSeriesWinners.csv file from my downloads folder and allows the user to either search by team name or enter a span of years to list the winners for that period.

import csv

# My file name for file processing
DATA_FILE = 'Downloads/WorldSeriesWinners.csv'

#Using some of the functions included in the class materials
def displayMenu():
    """Displays the main menu options."""
    print("\nWorld Series Winners Program")
    print("1 - Search by Team Name")
    print("2 - Search by Year Range")
    print("3 - Quit")

def loadWinnersData(filename):
    """Loads the World Series winners data from the CSV file."""
    winners = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                year = int(row[0])
                team = row[1].strip().lower()
                winners.append((year, team))
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return winners

def countTeamWins(winners, team_name):
    """Counts the number of wins for a given team."""
    team_name = team_name.lower()
    count = sum(1 for year, team in winners if team == team_name)
    return count

def listWinnersByYearRange(winners, start_year, end_year):
    """Lists the winners within a given year range."""
    winners_in_range = [(year, team) for year, team in winners if start_year <= year <= end_year]
    return winners_in_range

def getTeamName():
    """Prompts the user for a team name and returns it."""
    return input("Enter the name of the team: ").strip()

def getYearRange():
    """Prompts the user for a start and end year and returns them as a tuple."""
    while True:
        try:
            start_year = int(input("Enter the start year (1903 - 2023): "))
            end_year = int(input("Enter the end year (1903 - 2023): "))
            if start_year > end_year or start_year < 1903 or end_year > 2023:
                print("Invalid year range. Please enter a valid range between 1903 and 2023.")
            else:
                return start_year, end_year
        except ValueError:
            print("Invalid input. Please enter numeric values for the years.")

def main():
    """Main function to run the program."""
    winners = loadWinnersData(DATA_FILE)
    
    if not winners:
        print("No data loaded. Exiting program.")
        return

    while True:
        displayMenu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                team_name = getTeamName()
                wins = countTeamWins(winners, team_name)
                if wins > 0:
                    print(f"The {team_name.title()} have won the World Series {wins} times.")
                else:
                    print(f"The {team_name.title()} have never won the World Series.")
            elif choice == 2:
                start_year, end_year = getYearRange()
                winners_in_range = listWinnersByYearRange(winners, start_year, end_year)
                if winners_in_range:
                    print(f"\nWorld Series Winners from {start_year} to {end_year}:")
                    for year, team in winners_in_range:
                        print(f"{year}: {team.title()}")
                else:
                    print(f"No winners found in the range {start_year} to {end_year}.")
            elif choice == 3:
                print("Thank you for using the World Series Winners Program.")
                break
            else:
                print(f"{choice} is not a valid choice. Please choose from the menu options.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu options.")

# Start the program
if __name__ == '__main__':
    main()