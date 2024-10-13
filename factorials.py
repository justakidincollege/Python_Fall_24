# Factorials assignment
# Establish function to represent n as the number we are solving for
def factorial(n):
    if n==1 or n==0:
        return 1
    elif n>1:
        return n*factorial(n-1)

    


# Create the main function to invoke the previous one and to get input from the user
def main():
    n=int(input("Hello user I am a factorial calculator please enter a non-negative whole number and I will give you its factorial: "))
    print(f"The factorial of {n} is {factorial(n)}. ")

# Call the main function
main()