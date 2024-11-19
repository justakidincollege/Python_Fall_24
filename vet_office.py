# Vet Office assignment
# Create Pet class
class Pet:
    vet_name="PetCo"
    def __init__(self,owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    def get_owner_first_name(self):
        return self.__owner_first_name
    def get_owner_last_name(self):
        return self.__owner_last_name
    def get_pet_id(self):
        return self.__pet_id
    def get_pet_name(self):
        return self.__pet_name
    def get_pet_type(self):
        return self.__pet_type
    
    def set_owner_first_name(self,first_name):
        self.__owner_first_name=first_name
    def set_owner_last_name(self,last_name):
        self.__owner_last_name=last_name
    def set_pet_id(self,pet_id):
        self.__pet_id=pet_id
    def set_pet_name(self,pet_name):
        self.__pet_name=pet_name
    def set_pet_type(self,pet_type):
        self.__pet_type=pet_type
        
    def display_pet_info(self):
        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")
        print(f"Veterinary Clinic: {self.vet_name}")
        
pet1=Pet("Kureha", "Drum", 6, "Chopper", "Reindeer")
pet2=Pet("Mabel", "Pines", 1, "Waddles", "Pig")
pet3=Pet("Matthew","Smith", 4, "Zoe", "Siamese Cat")

pet1.set_owner_first_name("Luffy")
pet1.set_owner_last_name("Strawhat")

pet1.display_pet_info()
pet2.display_pet_info()
pet3.display_pet_info()

def check_property(pet_object, property_name):
    return hasattr(pet_object, property_name)

print(f"Does pet2 have '__owner_first_name'? {check_property(pet2, '_Pet__owner_first_name')}")


    