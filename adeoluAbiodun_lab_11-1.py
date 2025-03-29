# Name: Adeolu Abiodun  ||  Date: 03/12/2025  ||  Program file: adeoluAbiodun_lab_11-1.py

'''
This Python program stores employee details using an Employee class and a ProductionWorker subclass. It then retrieves and displays the information using accessor methods.
'''
# Here is the superclass Employee
class Employee:
    def __init__(self, employee_name, employee_num):
        self.employee_name = employee_name
        self.employee_num = employee_num

    def set_employee_name(self, employee_name):
        self.employee_name = employee_name

    def set_employee_num(self, employee_num):
        self.employee_num = employee_num

    def get_employee_name(self):
        return self.employee_name

    def get_employee_num(self):
        return self.employee_num

#Here is the subclass ProductionWorker
class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_num, shift_num, hourly_rate):
        super().__init__(employee_name, employee_num)
        self.shift_num = shift_num
        self.hourly_rate = hourly_rate

    def set_shift_num(self, shift_num):
        if shift_num in [1, 2]:
            self.shift_num = shift_num
        else:
            raise ValueError("Shift must be 1 (for day shift) or 2 (for night shift).")

    def set_hourly_rate(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def get_shift(self):
        return "Day" if self.shift_num == 1 else "Night"

    def get_hourly_rate(self):
        return self.hourly_rate


def main():
    print()
    print("Enter the data for the new Production Worker:")
    print("===========================================")

    employee_name = input("Employee Name: ")
    employee_num = input("Employee #: ")

    # Validate Shift Input
    while True:
        try:
            shift_num = int(input("Shift # (1 for day, 2 for night): "))
            if shift_num in [1, 2]:
                break
            else:
                print("Error: Please enter 1 for day shift or 2 for night shift.")
        except ValueError:
            print("Error: Invalid input. Please enter an integer (1 or 2).")

    hourly_rate = float(input("Hourly Rate: $"))

    # Create the ProductionWorker object
    productionworker = ProductionWorker(employee_name, employee_num, shift_num, hourly_rate)

    # Below is the employee details (output/display)
    print()
    print("Employee Information")
    print("<===================>")
    print(f"Employee Name: {productionworker.get_employee_name()}")
    print(f"Employee #: {productionworker.get_employee_num()}")
    print(f"Shift: {productionworker.get_shift()}")
    print(f"Hourly Rate: ${productionworker.get_hourly_rate():.2f}")
    

if __name__ == "__main__":
    main()
