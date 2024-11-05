# String practice assignment
#Create main function and do each task
def main():
    example_string = "Hello,_Python_programmers!"
    for x in (example_string):
        print(x,end=" ")
    print(f"\nThe character with the lowest value is {min(example_string)}")
    print(f"The character with the highest value is {max(example_string)}")
    print(f"The index of o is {example_string.index("o")}")
    list_string=list(example_string)
    print(f"Converting string to a list of characters: {list_string}")
    print(f"Count of 'o' in the string: {example_string.count("o")}")
main()