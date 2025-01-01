"""
1. Simple Unit Converter

Description: Create a program that converts units, such as kilometers to miles, Celsius to Fahrenheit, or kilograms to pounds.

Features:
- The user selects the conversion type from a menu.
- The user inputs a value to convert, and the program outputs the converted value.

Stretch Goal: Add input validation to handle incorrect or non-numeric inputs.
"""
class MainApp:
    
    # selectable menu
    def menu(self):
        print("=== Menu ===")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Kilograms to Pounds")
        print("=== ==== ===")
        
        user_choice = int(input("Select an Option: "))

        if user_choice == 1:
            self.kilometers_to_miles()
        elif user_choice == 2:
            self.celsius_to_fahrenheit()
        elif user_choice == 3:
            self.kilograms_to_pounds()
        else:
            print("invalid user input!")
            
    def kilometers_to_miles(self):
        print('kilometers!')

    def celsius_to_fahrenheit(self):
        print('celsius!')

    def kilograms_to_pounds(self):
        print('kg!')    

if __name__ == "__main__":
    app = MainApp()
    app.menu()