# practicing usage of inheritance
"""
Exercise 3: Game Characters

Create a class hierarchy to represent different types of RPG game characters:

- Character Class (Parent Class):  
  - Define properties `name` and `health` to store the character’s name and health value.  
  - Include methods `take_damage(amount)` to reduce health and `is_alive()` to check if the character is still alive.  

- Warrior Class (Child Class):  
  - Inherit from the `Character` class.  
  - Add an additional property `shield` to represent the warrior’s shield value.  
  - Override the `take_damage` method to reduce incoming damage based on the shield value.  

- Mage Class (Child Class):  
  - Inherit from the `Character` class.  
  - Add an additional property `mana` to represent the mage’s mana pool.  
  - Include a method `cast_spell(cost)` that decreases mana by the specified amount.  

Your goal is to:  

- Understand how inheritance allows child classes to extend and modify the behavior of a parent class.  
- Use `super()` to call the parent class’s constructor and initialize shared properties (`name` and `health`) while handling child-specific properties (`shield` or `mana`).  
- Create a Warrior and a Mage, make them attack each other, and print their status.  

"""
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount

    def is_alive(self):
        if self.health > 0:
            return True
        return False

class Warrior(Character):
    def __init__(self, name, health, shield):
        super().__init__(name, health)
        self.shield = shield

    def take_damage(self, amount):
        if self.shield < amount:
            super().take_damage(amount - self.shield)

class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    def cast_spell(self, cost):
        if cost <= self.mana:
            self.mana -= cost

def test_game_characters():
    # Create a Warrior and a Mage
    warrior = Warrior(name="Thor", health=100, shield=20)
    mage = Mage(name="Merlin", health=80, mana=50)

    # Initial status
    print("Initial Status:")
    print(f"Warrior - Name: {warrior.name}, Health: {warrior.health}, Shield: {warrior.shield}")
    print(f"Mage - Name: {mage.name}, Health: {mage.health}, Mana: {mage.mana}")

    # Mage casts a spell
    mage.cast_spell(10)
    print("\nAfter Mage casts a spell:")
    print(f"Mage's remaining mana: {mage.mana}")

    # Warrior takes damage
    warrior.take_damage(30)
    print("\nAfter Warrior takes 30 damage (shield reduces impact):")
    print(f"Warrior's remaining health: {warrior.health}")

    # Mage takes damage
    mage.take_damage(40)
    print("\nAfter Mage takes 40 damage:")
    print(f"Mage's remaining health: {mage.health}")

    # Check if characters are alive
    print("\nIs Warrior alive?", warrior.is_alive())
    print("Is Mage alive?", mage.is_alive())

    # Apply fatal damage to Mage
    mage.take_damage(50)
    print("\nAfter Mage takes fatal damage:")
    print(f"Mage's remaining health: {mage.health}")
    print("Is Mage alive?", mage.is_alive())

# Run the test
test_game_characters()

