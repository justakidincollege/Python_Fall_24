# Inheritance assignment
# Create employee class 
class employee:
    def __init__(self,name,number):
        self.__name=name
        self.__number=number

    def get_name(self):
        return self.__name

    def get_employee_number(self):
        return self.__number

    def set_name(self, name):
        self.__name=name

    def set_employee_number(self,number):
        self.__number=number


    
# Create subclass for production worker under employee
class productionworker(employee):
    def __init__(self,name,number,shift_number,pay_rate):
        super().__init__(name,number)
        self.__shift_number=shift_number
        self.__pay_rate=pay_rate

    def get_shift_number(self):
        return self.__shift_number

    def get_pay_rate(self):
        return self.__pay_rate

    def set_shift_number(self, shift_number):
        self.__shift_number=shift_number

    def set_pay_rate(self,pay_rate):
        self.__pay_rate=pay_rate


def main():
    name = input("Enter the employee's name: ")
    number = input("Enter the employee's number: ")
    
    while True:
        try:
            shift_number = int(input("Enter the shift number (1 for day, 2 for night): "))
            if shift_number in [1, 2]:
                break
            else:
                print("Shift number must be 1 (day) or 2 (night).")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            pay_rate = float(input("Enter the hourly pay rate: "))
            if pay_rate >= 0:
                break
            else:
                print("Hourly pay rate must be non-negative.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    worker = productionworker(name, number, shift_number,pay_rate)

    print("\nProduction Worker Details:")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_employee_number()}")
    print(f"Shift Number: {worker.get_shift_number()}")
    print(f"Hourly Pay Rate: ${worker.get_pay_rate():.2f}")

main()
