# practicing usage of inheritance
"""
Exercise 5: Banking System

Create a class hierarchy to represent a banking system:

1.  Person Class:
    -   Represents a person with the following properties:
        -   name: The name of the person.
        -   address: The address of the person.

2.  BankAccount Class:
    -   Inherits from Person and represents a bank account. Adds:
        -   account_number: The unique account number.
        -   balance: The current balance of the account.
    -   Includes methods:
        -   deposit(amount): Adds the specified amount to the account balance.
        -   withdraw(amount): Deducts the specified amount from the account balance, if sufficient funds are available.

3.  SavingsAccount Class:
    -   Inherits from BankAccount and represents a savings account. Adds:
        -   interest_rate: The interest rate associated with the savings account.
    -   Includes a method:
        -   calculate_interest(): Calculates and returns the interest earned based on the current balance.

4.  CheckingAccount Class:
    -   Inherits from BankAccount and represents a checking account. Adds:
        -   checks_written: Tracks the number of checks written from the account.
    -   Includes methods to update and track check usage.
"""
class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class BankAccount(Person):
    def __init__(self, name,  address, account_number, balance):
        super().__init__(name, address)
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise Exception("Insufficent Funds.")
        else:
            self.balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self, name, address, account_number, balance, interest_rate):
        super().__init__(name, address, account_number, balance)
        self.interest_rate = interest_rate
    
    def calcualate_interest(self):
        return self.balance * self.interest_rate

class CheckingAccount(BankAccount):
    def __init__(self, name, address, account_number, balance, checks_written):
        super().__init__(name, address, account_number, balance)
        self.check_written = checks_written
    
    def update_checks(self):
        self.check_written += 1

    def write_check(self, date, amount, payee):
        self.update_checks()
        return f"Check Created! Date: {date}, Amount: {amount}, Payee: {payee}"

# test cases

print(f"Test Case 1: Person Initialisation")
person = Person("Alice", "123 Elm Street")
print(person.name)    # Output: Alice
print(person.address) # Output: 123 Elm Street
print(f"--- Test Case 1 End ---")

print(f"Test Case 2: BankAccount Deposit and Withdraw")
account = BankAccount("Bob", "456 Oak Street", "BA123", 1000)
print(account.name)              # Output: Bob
print(account.address)           # Output: 456 Oak Street
print(account.account_number)    # Output: BA123
print(account.balance)           # Output: 1000

account.deposit(500)
print(account.balance)           # Output: 1500

account.withdraw(300)
print(account.balance)           # Output: 1200

try:
    account.withdraw(2000)
except Exception as e:
    print(e)                     # Output: Insufficient Funds.
print(f"--- Test Case 2 End ---")

print(f"Test Case 3: SavingsAccount Interest Calculation")
savings = SavingsAccount("Charlie", "789 Pine Street", "SAV456", 2000, 0.05)
print(savings.calcualate_interest()) # Output: 100.0 (2000 * 0.05)

savings.deposit(500)
print(savings.balance)              # Output: 2500

savings.withdraw(1000)
print(savings.balance)              # Output: 1500
print(f"--- Test Case 3 End ---")

print(f"Test Case 4: Check Writing and Tracking")
checking = CheckingAccount("David", "101 Maple Avenue", "CHK789", 1500, 0)
print(checking.check_written)     # Output: 0

# Write a check
print(checking.write_check("2025-01-28", 200, "Store A"))
# Output: Check Created! Date: 2025-01-28, Amount: 200, Payee: Store A

print(checking.check_written)     # Output: 1

# Write another check
print(checking.write_check("2025-01-29", 100, "Store B"))
# Output: Check Created! Date: 2025-01-29, Amount: 100, Payee: Store B

print(checking.check_written)     # Output: 2
print(f"--- Test Case 4 End ---")

