# Age Calculator Assignment
# Import datetime
from datetime import datetime
# Create maiin function
def main():
    try:
        # Get the current date
        today=datetime.today()
        
        # Ask for the user's birth year, month, and day
        birth_year=int(input("What year were you born?  "))
        month=int(input("What month were you born (as a number. May would be 5):  "))
        day=int(input("What day of the month were you born?  "))
        
        # Create a datetime object for the birthday
        birthday=datetime(birth_year, month, day)
        print("Your birthday is:")
        birthday_output=birthday.strftime("%Y-%m-%d")
        print(birthday_output)

        # Calculate the difference in days between today and the birthday
        delta=today-birthday
        print(f"About {delta.days} have passed since you where born.")
        
        # Calculate the age in years, months, weeks, and days
        total_days=delta.days
        years=total_days//365
        remaining_days=total_days%365
        months=remaining_days//30
        remaining_days%=30
        weeks=remaining_days//7
        days=remaining_days%7

        # Print the results in a clear and understandable manner
        print(f"You are approximately:")
        print(f"Years: {years}")
        print(f"Months: {months}")
        print(f"Weeks: {weeks}")
        print(f"Days: {days}")

    except Exception as e:
        # Handle errors gracefully and allow the user to try again
        print(f"\nOops! Something went wrong: {e}") 
        main()

# Call the main function to execute the program
main()
