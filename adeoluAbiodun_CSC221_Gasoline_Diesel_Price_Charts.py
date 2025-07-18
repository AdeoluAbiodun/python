# Name: Adeolu Abiodun  ||  Date: 05/05/2025  ||  Program file: adeoluAbiodun_pc5.py

''' This Python program enables users to select weekly and monthly data from any 5years (between 2008 to 2024) and
generates both bar and line charts for each year. The charts display the week numbers on the Y azis and the prices
on the X-axis, with seperate lines for each grade of gas and diesel, each represented by different color.'''

import matplotlib.pyplot as plt
import pandas as pd
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        print(f"The file not found: {file_path}")
        return None

    df = pd.read_csv(file_path)
    df = df.rename(columns={
        "Date (Monday)": "Date",
        "Regular Gas": "Regular",
        "Midgrade Gas": "Midgrade",
        "Premium Gas": "Premium",
        "Diesel Ultra Low Sulfur": "Diesel"
    })
    df["Date"] = pd.to_datetime(df["Date"])
    df["Year"] = df["Date"].dt.year
    df["Week"] = df["Date"].dt.isocalendar().week
    df["Month"] = df["Date"].dt.month
    return df

def plot_weekly_prices(df, years):
    for year in years:
        yearly_data = df[df["Year"] == year]
        plt.figure(figsize=(10, 6))
        plt.plot(yearly_data["Regular"], yearly_data["Week"], label="Regular", color='blue')
        plt.plot(yearly_data["Midgrade"], yearly_data["Week"], label="Midgrade", color='orange')
        plt.plot(yearly_data["Premium"], yearly_data["Week"], label="Premium", color='green')
        plt.xlabel("Price ($)")
        plt.ylabel("Week Number")
        plt.title(f"Weekly Gasoline Prices in {year}")
        plt.legend()
        plt.gca().invert_yaxis()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

def plot_monthly_averages(df, years):
    for year in years:
        yearly_data = df[df["Year"] == year]
        monthly_avg = yearly_data.groupby("Month")[["Regular", "Midgrade", "Premium", "Diesel"]].mean()
        monthly_avg.plot(kind='barh', figsize=(10, 6), colormap="Set2")
        plt.xlabel("Average Price ($)")
        plt.ylabel("Month")
        plt.title(f"Monthly Average Fuel Prices in {year}")
        plt.legend(title="Fuel Type")
        plt.tight_layout()
        plt.show()

def get_years():
    while True:
        input_str = input("Enter 5 years separated by commas (e.g., 2008,2009,2014,2015,2022): ").strip()
        try:
            years = [int(year.strip()) for year in input_str.split(",") if year.strip().isdigit()]
            if len(years) != 5:
                print("Please enter exactly 5 valid years (between 2008 to 2024).")
                continue
            return years
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    file_path = input("Enter the full/relative path to the CSV file: ").strip()
    df = load_data(file_path)
    if df is not None:
        selected_years = get_years()
        plot_weekly_prices(df, selected_years)
        plot_monthly_averages(df, selected_years)
