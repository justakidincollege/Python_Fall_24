# First Class Assignment
# Create Person class
class Person:
    def __init__(self,name,address,age,number):
        self.__name=name
        self.__address=address
        self.__age=age
        self.__number=number

    def get_name(self):
        return self.__name
    def get_adress(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_number(self):
        return self.__number
        
    def set_name(self,name):
        self.__name=name
    def set_address(self,address):
        self.__address=address
    def set_age(self, age):
        self.__age=age
    def set_number(self,number):
        self.__number=number

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Address: {self.__address}")
        print(f"Age: {self.__age}")
        print(f"Number: {self.__number}")

person1=Person("Elmo", "Sesame Street, Manhattan", 3, "123-456" )
person2=Person("Dipper Pines", "618 Gopher Road, Gravity Falls", 13, "323-283-8650" )
person3=Person("Gumball Watterson", "1026 York Street, Vallejo", 12, "375-114" )

print("Person 1 Information:")
person1.display_info()

print("Person 2 Information:")
person2.display_info()

print("Person 3 Information:")
person3.display_info()