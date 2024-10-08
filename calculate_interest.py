# Calculate interest with return
# Ask user for inputs
principal=int(input("Hello user I am an interest calulcator.\nPlease enter the prinipal amount:"))
rate=int(input("Now please enter the interest rate as a whole number(5% would be 5):"))
time=int(input("Lastly please enter the investment time in whole years:"))

# Establish function
def calculate_interest(principal, rate, time):
    interest=(principal*rate*time)/100
    return interest
interest=calculate_interest(principal, rate, time)
print(f"The simple interest for a principal amount of ${principal:,.2f} at a interest rate of {rate}% over a period of {time} years would be ${interest}. ")
