# Adding Excpetion Handling assignment
# The code given for the assignment with added try and except statements
def square_number():
    number = input("Enter a number to square: ")
    try:
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    except:
        print("Sorry but I can not calculate the square of a decimal.\nPlease try another number.")

# Calling main function to run program
square_number()