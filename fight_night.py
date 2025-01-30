"""
Exercise: Turn-Based Battle System

Create a Python program that simulates a turn-based combat system between different character classes.

- Requirements:

  - Implement an abstract base class `Character` with:
    - Attributes:
      - `name` (str): The name of the character.
      - `health` (int): The character’s health points.
      - `attack_power` (int): The damage dealt per attack.
    - Methods:
      - `attack(target)`: Reduces the target's health by the character’s attack power.
      - `take_damage(amount)`: Reduces the character's health by the given amount.
      - `is_alive()`: Returns `True` if the character’s health is greater than 0, otherwise `False`.

  - Implement two subclasses:
    - `Warrior`:
      - Deals normal damage but has a chance to block an attack (reducing damage taken).
      - Overrides `take_damage(amount)` to apply damage reduction when blocking.
    - `Rogue`:
      - Has a chance to dodge attacks (taking no damage) and deals critical hits (double damage).
      - Overrides `attack(target)` to sometimes deal double damage.
      - Overrides `take_damage(amount)` to sometimes avoid damage entirely.

  - Implement a Game Loop where:
    - The characters take turns attacking each other.
    - The battle continues until one character's health reaches 0.
    - Display turn-by-turn logs of damage dealt, dodges, and blocks.

- Bonus Features (if you want to make it fancier):

  - Add a `Mage` class with mana and spells.
  - Implement items like health potions.
  - Add randomness (e.g., critical hit/dodge chances).
  - Format output neatly with colors (using `colorama`).
"""

from abc import ABC, abstractmethod
import random

class Character(ABC):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def take_damage(self, amount):
        pass

    def is_alive(self):
        if self.health > 0:
            return True
        return False
    
class Warrior(Character):
    def __init__(self, name, health, attack_power, shield):
        super().__init__(name, health, attack_power)
        self.shield = shield

    def attack(self, target):
        target.take_damage(self.attack_power)

    def take_damage(self, amount):
        block_roulette = [True, False]
        if random.choice(block_roulette):
            self.health = self.health - max(0, amount - self.shield)
        else:
            self.health -= amount
        if self.health < 0:
            self.health = 0

class Rogue(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

    def attack(self, target):
        crit_chance = [True, False]
        if random.choice(crit_chance):
            target.take_damage(self.attack_power * 2)
        if target.health < 0:
            target.health = 0

    def take_damage(self, amount):
        dodge_chance = [True, False]
        if not random.choice(dodge_chance):
            self.health -= amount
        if self.health < 0:
            self.health = 0

rogue = Rogue("NightShade", 100, 10)
warrior = Warrior("Brawnden", 100, 15, 5)

rogue_health = rogue.health
warrior_health = warrior.health

while True:
    # when rogue attacks
    print(f"Rogue {rogue.name} attacks Warrior {warrior.name}.")
    rogue.attack(warrior)
    # if the rogue landed a crit on the warrior
    if warrior.health == warrior_health - (rogue.attack_power * 2):
        print(f"Rogue {rogue.name} lands a critical hit on warrior {warrior.name} leading to double the damage received!")
        print(f"Warrior {warrior.name}'s health is {warrior.health}.")
    # if the rogue landed a crit on the warrior, but the warrior also was able to block with his shield
    elif warrior.health == (warrior_health + warrior.shield) - (rogue.attack_power * 2):
        print(f"Rogue {rogue.name} lands a critical hit on warrior {warrior.name} leading to double the damage received!")
        print(f"HOWEVER! Some damage has been blocked as Warrior {warrior.name} was able to shield in time.")
        print(f"Warrior {warrior.name}'s health is {warrior.health}.")
    # if the warrior shielded in time
    elif warrior.health == (warrior_health + warrior.shield) - rogue.attack_power:
        print(f"Warrior {warrior.name} blocked some damage by bracing with his shield.")
        print(f"Warrior {warrior.name}'s health is {warrior.health}.")
    else:
        print(f"Warrior {warrior.name}'s health is {warrior.health}.")
    # check if the warrior is dead
    if not warrior.is_alive():
        print(f"Rogue {rogue.name} is victorious!")
        break

    # update the local warrior health value for future comparisons
    warrior_health = warrior.health

    # when warrior attacks
    print(f"Warrior {warrior.name} attacks Rogue {rogue.name}")
    warrior.attack(rogue)
    # if the rogue dodges the attack
    if rogue.health == rogue_health:
        print(f"Rogue {rogue.name} was too nimble and dodged the Warrior {warrior.name}'s attack!")
        print(f"Rogue {rogue.name}'s health is {rogue.health}.")
    else:
        print(f"Rogue {rogue.name}'s health is {rogue.health}.")
    # check if the warrior is dead
    if not rogue.is_alive():
        print(f"Warrior {warrior.name} is victorious!")
        break

    rogue_health = rogue.health
