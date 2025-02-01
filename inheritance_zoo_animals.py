# practicing usage of inheritance
"""
Exercise 4: Zoo Animals

Build a zoo management system:

- An Animal class with species and diet.
- A Bird class that inherits from Animal and adds wing_span.
- A Mammal class that inherits from Animal and adds fur_type.
- Add a ZooKeeper class that interacts with all the animals.

Task: Create a ZooKeeper that feeds the animals and prints their details.
"""
from abc import ABC, abstractmethod

class Animal:
    def __init__(self, species : str, diet : str):
        self.species = species
        self.diet = diet

    def get_details(self):
        return f"Species: {self.species}, Diet: {self.diet}"

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self):
        return f"{self.species} has been fed."

class Bird(Animal):
    def __init__(self, species : str, diet : str, wing_span : int):
        super().__init__(species, diet)
        self.wing_span = wing_span
    
    def fly(self):
        return "The bird is flying."

    def make_sound(self):
        return "Tweet Tweet"
    
class Mammal(Animal):
    def __init__(self, species : str, diet : str, fur_type : str):
        super().__init__(species, diet)
        self.fur_type = fur_type

    def run(self):
        return "The mammal is running!"
    
    def make_sound(self):
        return "Whomp Whomp"
    
class Zookeeper:
    def __init__(self, name : str, experience_level : int):
        self.name = name
        self.experience_level = experience_level

    def feed_animal(self, animal: Animal, food : str):
        return f"{self.name} is feeding {animal.species} some {food}.\n{animal.species} has been fed."
    
    def check_animal(self, animal : Animal):
        return f"Animal Details: {animal.get_details()}\n{animal.make_sound()}"
    
    def perform_routine(self, animals : list):
        for i in animals:
            print(i.species)

def run_tests():
    print("Running tests...\n")

    # Test Bird
    bird = Bird("Eagle", "Carnivore", 2)
    assert bird.get_details() == "Species: Eagle, Diet: Carnivore"
    assert bird.make_sound() == "Tweet Tweet"
    assert bird.fly() == "The bird is flying."
    assert bird.feed() == "Eagle has been fed."

    # Test Mammal
    mammal = Mammal("Tiger", "Carnivore", "Striped")
    assert mammal.get_details() == "Species: Tiger, Diet: Carnivore"
    assert mammal.make_sound() == "Whomp Whomp"
    assert mammal.run() == "The mammal is running!"
    assert mammal.feed() == "Tiger has been fed."

    # Test Zookeeper
    zookeeper = Zookeeper("John", 5)
    assert zookeeper.feed_animal(mammal, "Meat") == "John is feeding Tiger some Meat.\nTiger has been fed."
    assert zookeeper.check_animal(bird) == "Animal Details: Species: Eagle, Diet: Carnivore\nTweet Tweet"

    # Test Routine
    print("\nPerforming daily routine:")
    zookeeper.perform_routine([bird, mammal])

    print("\nAll tests passed!")

# Run test cases
if __name__ == "__main__":
    run_tests()
