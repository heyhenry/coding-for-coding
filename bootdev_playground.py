class Owner:
    def __init__(self, owner_name):
        self.owner_name = owner_name

class Animal:
    def __init__(self, animal_type):
        self.animal_type = animal_type

class Pet(Owner, Animal):
    def __init__(self, years_as_pet):
        self.years_as_pet = years_as_pet
        Owner.__init__(self, "Henry")
        Animal.__init__(self, "Cat")

obj = Pet(21)
print(obj.years_as_pet)
print(obj.animal_type)
print(obj.owner_name)