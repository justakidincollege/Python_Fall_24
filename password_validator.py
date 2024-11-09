# Password Validator Assignment
# Create main function
def main():
    valid=False
    while valid!=True:
        valid=True
        print("Please enter a password that meets the following criteria\n- A uppercase letter\n- A lowercase letter\n- A number\n- A symbol from this set(!@#$%&*)\n- 8-20 characters long")
        password=str(input("Now please input your password: "))
        password_again=str(input("Now please input your password again to confirm: "))
        if password_again!=password:
            valid=False
            print("Password do not match.")
        
        length=len(password)
        if not 7<length<21:
            print("Your password is not a valid length.")
            valid=False
            continue

        upperv=False
        lowerv=False
        symbolv=False
        numberv=False
        symbol=["!","@","#","$","%","&","*"]
        number=["1","2","3","4","5","6","7","8","9","0"]
        
        for char in password:
            if char.isupper():
                upperv=True
            elif char.islower():
                lowerv=True
            elif char in symbol:
                symbolv=True
            elif char in number:
                numberv=True

        if upperv==False:
            valid=False
            print("Your password must contain a capital letter.")
        elif lowerv==False:
            valid=False
            print("Your password must include a lowercase letter.")
        elif symbolv==False:
            valid=False
            print("Your password must include a symbol.")
        elif numberv==False:
            valid=False
            print("Your password must contain a number.")
        
        if valid==True:
            print("Your password has been registered.")
        




main()