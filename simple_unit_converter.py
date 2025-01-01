"""
1. Simple Unit Converter

Description: Create a program that converts units, such as kilometers to miles, Celsius to Fahrenheit, or kilograms to pounds.

Features:
- The user selects the conversion type from a menu.
- The user inputs a value to convert, and the program outputs the converted value.

Stretch Goal: Add input validation to handle incorrect or non-numeric inputs.
"""
class MainApp():
    # selectable menu
    def menu():
        print("=== Menu ===")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Kilograms to Pounds")
        print("=== ==== ===")
        user_choice = int(input("Select an Option: "))

    