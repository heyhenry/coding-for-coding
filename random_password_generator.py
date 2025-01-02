"""
3. Random Password Generator

Description: Write a program that generates secure, random passwords.

Features:
- Allow the user to specify the password length.
- Use a mix of uppercase, lowercase, numbers, and symbols.
- Display the generated password.

Stretch Goal: Add an option for the user to exclude certain characters or generate multiple passwords at once.
"""
import string
import random

class MainApp:
    
    def main_screen(self):
        while True:
            print("\n===[Random Password Generator]===")
            print("1. Generate A Password")
            print("2. Generate Multiple Passwords")
            print("3. Exit Program")
            print("=================================")

            try:
                user_menu_choice = int(input("Enter Choice (Associated Numeric Value): "))

                if user_menu_choice == 1:
                    user_length_choice = int(input("Enter desired length of password: "))
                    print(self.generate_password(1, user_length_choice))
                elif user_menu_choice == 2:
                    user_specific_quantity_choice = int(input("Enter desired quantity of passwords: "))
                    user_length_choice = int(input("Enter desired length of password: "))
                    print(self.generate_password(user_specific_quantity_choice, user_length_choice))
                elif user_menu_choice == 3:
                    print("Exiting...")
                    break
                else:
                    print("Invalid Input! Enter a numeric value associated with an option in the menu.")
            except ValueError:
                print("Invalid Input! Enter numeric value associated with an option in the menu.")

    def generate_password(self, quantity, length):
        valid_chars = string.ascii_letters + string.digits + string.punctuation
        password_list = []
        for _ in range(quantity):    
            password = random.sample(valid_chars, length)
            password = ''.join(password)
            password_list.append(password)
        return password_list
        

if __name__ == "__main__":
    app = MainApp()
    app.main_screen()