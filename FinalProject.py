import os

def processDataFile():
    try:
        # Correctly joining the path using os.path.join with separate arguments
        file_path = os.path.join("Downloads", "Downloads/TelephoneData.txt")
        
        with open(file_path, "r") as file:
            for line in file:
                # Strip any extraneous whitespace from the line
                line = line.strip()

                # Skip empty lines
                if not line:
                    continue

                # Attempt to split the line and ensure it has exactly 6 fields
                parts = line.split(',')
                if len(parts) != 6:
                    print(f"Skipping invalid line: {line}")
                    continue

                # Unpack the parts safely
                name, address, city, state, zip_code, minutes = parts
                try:
                    minutes = int(minutes)  # Validate minutes is an integer
                except ValueError:
                    print(f"Invalid minutes value for line: {line}. Skipping.")
                    continue

                # Calculate and display the amount owed (assuming calcAmountOwed is defined elsewhere)
                amount_owed = calcAmountOwed(minutes)
                print(f"{name}\n{address}\n{city}, {state} {zip_code}")
                print(f"Amount Owed: ${amount_owed:.2f}")

    except FileNotFoundError:
        print("Error: TelephoneData.txt file not found in the Downloads folder.")
    except Exception as e:
        print(f"An error occurred: {e}")