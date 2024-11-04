# ASCII Value finder assignment
# Create main function
def main():
    user_input=input("Enter a character: ")
    while len(user_input)!=1:
        print("Please enter exactly one character.\nIf more than one character is entered you will be asked to revise your answer.")
        user_input=input("Enter a character: ")
    ascii_value=ord(user_input)
    print(f"The ASCII value of {user_input} is {ascii_value}")
# Invoke main function
main()