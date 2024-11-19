# Pet Class Creation Assignment
# Create Pet Class
class Pet:
    def __init__(self,kind,breed,name):
        self.__kind=kind
        self.__breed=breed
        self.__name=name

    def get_kind(self):
        return self.__kind
    def get_breed(self):
        return self.__breed
    def get_name(self):
        return self.__name
    
    def set_kind(self,kind):
        self.__kind=kind
    def set_breed(self,breed):
        self.__breed=breed
    def set_name(self, name):
        self.__name=name
    
    def print_details(self):
        print(f"Pet Details\n  Kind: {self.__kind}\n  Breed: {self.__breed}\n  Name: {self.__name}")

pet1=Pet("Dog", "Scottish Terrier", "Pippin")
pet2=Pet("Cat", "Siamese", "Zoe")
pet3=Pet("Bird", "Cockatoo", "Richard")

pet1.print_details()
pet2.print_details()
pet3.print_details()

print(f"Class Name: {Pet.__name__}")
print(f"Base classes of Pet: {Pet.__module__}")
print(f"Is pet3 an instance of Pet? {isinstance(pet3, Pet)}")
