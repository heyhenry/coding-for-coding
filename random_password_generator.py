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
        print("===[Random Password Generator]===")
        print("1. Generate A Password")

        user_quantity_choice = int(input("Enter Choice (Associated Numeric Value): "))
        user_length_choice = int(input("Enter desired length of password: "))

        if user_quantity_choice == 1:
            print(self.generate_password(user_length_choice, user_length_choice))


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