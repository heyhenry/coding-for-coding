"""
1. Simple Unit Converter

Description: Create a program that converts units, such as kilometers to miles, Celsius to Fahrenheit, or kilograms to pounds.

Features:
- The user selects the conversion type from a menu.
- The user inputs a value to convert, and the program outputs the converted value.

Stretch Goal: Add input validation to handle incorrect or non-numeric inputs.
"""
class MainApp:
    """
    A simple unit converter application.

    Features:
    - Kilometers to Miles conversion
    - Celsius to Fahrenheit conversion
    - Kilograms to Pounds conversion
    - Smooth handling of invalid inputs
    """

    # selectable menu
    def menu(self):
        while True:
            # selection option from menu
            print("\n=== Menu ===")
            print("1. Kilometers to Miles")
            print("2. Celsius to Fahrenheit")
            print("3. Kilograms to Pounds")
            print("4. Exit Program")
            print("=== ==== ===")
            
            # attempt to get a valid user input
            try: 
                user_menu_choice = int(input("Select an Option: "))
            # if the input value is a non-integer then showcase the menu again
            except ValueError:
                # notify user with an error message
                print("Error: Invalid User Input! Please enter a number.")

            # call relevant funciton based on selected menu option
            if user_menu_choice == 1:
                print(self.kilometers_to_miles())
            elif user_menu_choice == 2:
                print(self.celsius_to_fahrenheit())
            elif user_menu_choice == 3:
                print(self.kilograms_to_pounds())
            elif user_menu_choice == 4:
                print("Exiting...")
                break
            else:
                print("Error: Invalid User Input! Please select a number from the menu.")
    
    # kilometers to miles converter
    def kilometers_to_miles(self):
        """
        Function: kilometers_to_miles()
        Description: Converts the given kilometers value to miles
        Conversion Formula: user_given_value * 0.62137
        """
        try:
            user_given_value = float(input("Enter value (in kilometers): "))
            # conversion formula (km to mi)
            result = user_given_value * 0.62137
            # create string formatted result
            result_string = f'Result: {user_given_value} kilometers converts to {round(result, 1)} miles.'
            return result_string
        except ValueError:
            return "Error: Invalid User Input! Please enter a number (Integer or Float)."

    # celsius to fahrenheit converter
    def celsius_to_fahrenheit(self):
        """
        Function: celsius_to_fahrenheit()
        Description: Converts the given celsius value to fahrenheit
        Conversion Formula: (user_given_value * 9/5) + 32
        """
        try:
            user_given_value = float(input("Enter value (in celsius): "))
            # conversion formula (C to F)
            result = (user_given_value * 9/5) + 32
            # create string formatted result
            result_string = f'Result: {user_given_value} celsius converts to {round(result, 1)} fahrenheit.'
            return result_string
        except ValueError:
            return "Error: Invalid User Input! Please enter a number (Integer or Float)."

    # kilograms to pounds converter
    def kilograms_to_pounds(self):
        """
        Function: kilograms_to_pounds()
        Description: Converts the given kilograms value to pounds
        Conversion Formula: user_given_value * 2.205
        """
        try:
            user_given_value = float(input("Enter value (in kilograms): "))
            # conversion formula (kg to lb)
            result = user_given_value * 2.205
            # create string formatted result
            result_string = f'Result: {user_given_value} kilograms converts to {round(result, 1)} pounds.'
            return result_string 
        except ValueError:
            return "Error: Invalid User Input! Please enter a number (Integer or Float)."

if __name__ == "__main__":
    app = MainApp()
    # app.menu()
    
    # to see the code in a document style in the terminal
    help(MainApp)