# Functions assignment
# Create the square and circle functions
def square(side):
    area=side*side
    print("The area of the sqaure is",area,"square units")
def circle(radius):
    circumference=((radius**2)*3.14)
    print("The circumference of the circle is",circumference,"square units")

# Ask for side and radius
side=int(input("Please enter the side of the square: "))
radius=int(input("Pleae enter the radius of the circle: "))
square(side)
circle(radius)