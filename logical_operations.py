# Logical operations assignment

# Ask user for input
num_1=int(input("Hello user please input an interger:"))
num_2=int(input("Please input another interger:"))
total=num_1+num_2
product=num_1*num_2

# Enter operators
if not total>0:
    print("The sum of the two number is not positive.")
else:
    print("The sum of the two numbers is positive.")

if not product>0:
    print("The product of the two numbers is not positive.")
else:
    print("The product of the two numbers is positive.")

if num_1>0 and num_2>0:
    print("Both numbers are positive.")
elif num_1>0 and num_2<0:
    print("The first number is positive and the second number is negative.")
elif num_1<0 and num_2>0:
    print("The first number is negative and the second number is positive.")
elif num_1<0 and num_2<0:
    print("Both of the numbers are negative.")
else:
    print("Both numbers are zero.")

if num_1%2==0 and num_2%2==0:
    print("Both numbers are even.")
elif num_1%2==1 and num_2%2==0:
    print("The first number is odd and the second number is even.")
elif num_1%2==0 and num_2%2==1:
    print("The first number is even and the second number is odd.")
else:
    print("Both numbers are odd.")

if num_1>100 or num_2>100:
    print("At least one of the numbers is greater than 100.")
else:
    print("Neither of the numbers is greater than 100.")

if num_1<0 or num_2<0:
    print("At least on of the numbers is negative.")
else:
    print("Neither of the numbers is negative.")