# Custom Calendar Assignment
# Imports
import calendar
import datetime

# Create main function
def main():
    # Get the current year using datetime module
    current_year = datetime.datetime.now().year
    
    while True:
        try:
            # Ask the user for their birth month
            birth_month = int(input("Please enter your birth month (1-12): "))
            
            # Validate that the input is an integer between 1 and 12
            if 1 <= birth_month <= 12:
                # Generate and display the calendar for the birth month in the current year
                print(f"\nHere is the calendar for {calendar.month_name[birth_month]} {current_year}:\n")
                print(calendar.month(current_year, birth_month))
                break
            else:
                print("Error: Please enter a number between 1 and 12.")
        except ValueError:
            # Handle invalid inputs that cannot be converted to an integer
            print("Error: Invalid input. Please enter a valid integer between 1 and 12.")
    
# Call the main() function to run the program
main()
