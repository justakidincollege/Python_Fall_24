# Create and use tuples assignment
# Create the tuple holding the class names
programming_classes=("Intro to Python","Advanced Python","Database Essentials","Web Development Basics","Data Structures in Python","Web Design Fundamentals")

# Define main function
def main():
    for i in programming_classes:
        print(i)
    print(f"There are {len(programming_classes)} classes in the tuple.")

# Call main function
main()