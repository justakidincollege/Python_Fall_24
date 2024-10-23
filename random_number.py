# Random number guessing game assignment
# Import the random module and generate the random number
import random
random_number=random.randint(1,100)
guess=0

# Define main function
def main():
    global guess
    print("Lets play a game!\nI am thinking of a random number.\nI'll let you know if your hot or cold.\nEnter -1 if you wish to quit the game.")
    while guess != random_number:
        try:
            guess=int(input("Now try to guess it: "))
            difference=abs(random_number-guess)
            if guess==random_number:
             print("Congratulations you guessed the number!")
             break
            elif guess== -1:
               print(f"{random_number} was the number\n Thank you for playing!")
               break
            elif difference<5:
               print("Very hot!!")
            elif difference<10:
               print("Hot!")
            elif difference<25:
               print("Cold")
            elif difference>=25:
               print("Very Cold")
        except ValueError:
            print("I'm sorry that is not a valid input.\nPlease try again.")

# Invoke the main function
main()