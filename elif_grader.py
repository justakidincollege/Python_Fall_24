# Elif grader assignment

# Ask user to input numeric grade
grade=int(input("Hello user I am a grading program.\nPlease enter your numeric grade."))

# Run functions to determine and display letter grade
if grade<60:
    print("Your current letter grade is a F.")
elif grade<70:
    print("Your current letter grade is a D.")
elif grade<80:
    print("Your current letter grade is a C")
elif grade<90:
    print("Your current letter grade is a B")
elif grade<100:
    print("Your current letter grade is a A")
else: 
    print("Your current letter grade is a A")
