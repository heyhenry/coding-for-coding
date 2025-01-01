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
        # selection option from menu
        print("=== Menu ===")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Kilograms to Pounds")
        print("=== ==== ===")
        
        # attempt to get a valid user input
        try: 
            user_menu_choice = int(input("Select an Option: "))
        # if the input value is a non-integer then showcase the menu again
        except ValueError:
            # notify user with an error message
            print("Invalid User Input! Please enter a number.")
            self.menu()

        # call relevant funciton based on selected menu option
        if user_menu_choice == 1:
            self.kilometers_to_miles()
        elif user_menu_choice == 2:
            self.celsius_to_fahrenheit()
        elif user_menu_choice == 3:
            self.kilograms_to_pounds()
        else:
            print("Invalid User Input!")
            
    # kilometers to miles converter
    def kilometers_to_miles(self):
        user_given_value = float(input("Enter value (in kilometers): "))
        # conversion formula (km to mi)
        result = user_given_value * 0.62137
        # display result
        return print(f'{user_given_value} kilometers converts to {round(result, 1)} miles.')

    # celsius to fahrenheit converter
    def celsius_to_fahrenheit(self):
        user_given_value = float(input("Enter value (in celsius): "))
        # conversion formula (C to F)
        result = (user_given_value * 9/5) + 32
        # display result
        return print(f'{user_given_value} celsius converts to {round(result, 1)} fahrenheit.')

    # kilograms to pounds converter
    def kilograms_to_pounds(self):
        user_given_value = float(input("Enter value (in kilograms): "))
        # conversion formula (kg to lb)
        result = user_given_value * 2.205
        # display result
        return print(f'{user_given_value} kilograms converts to {round(result, 1)} pounds.')  

if __name__ == "__main__":
    app = MainApp()
    app.menu()
    
    # to see the code in a document style in the terminal
    # help(MainApp)