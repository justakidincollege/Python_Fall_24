# Personal Diary Assignment
# Create main function
def main():
    # Ask user for inputs
    date = input("Please enter the current date and time: ")
    diary_entry = input("Please write your diary entry: ")
    with open("Diary folder.txt", "a") as file:
        file.write(f"{date}\n")
        file.write(f"{diary_entry}\n")
        file.write("\n")

main()