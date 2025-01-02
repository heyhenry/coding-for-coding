"""
3. Random Password Generator

Description: Write a program that generates secure, random passwords.

Features:
- Allow the user to specify the password length.
- Use a mix of uppercase, lowercase, numbers, and symbols.
- Display the generated password.

Stretch Goal: Add an option for the user to exclude certain characters or generate multiple passwords at once.
"""
class MainApp:
    
    def main_screen(self):
        print("===[Random Password Generator]===")
        print("1. Generate A Password")

        user_quantity_choice = int(input("Enter Choice (Associated Numeric Value): "))
        user_length_choice = int(input("Enter desired length of password: "))

        if user_quantity_choice == 1:
            self.generate_password(1, 2)


    def generate_password(self, quantity, length):
        print('poop')

if __name__ == "__main__":
    app = MainApp()
    app.main_screen()