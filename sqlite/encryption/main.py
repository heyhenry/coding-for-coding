import sqlite3
from cryptography.fernet import Fernet
import os

if os.path.exists("sample_database.db"):
    connection = sqlite3.connect("sample_database.db")
    cursor = connection.cursor()

key = Fernet("UBy1tA_tENd8h7NfXqNwH5c5Sx2H2CkqXbN1RXJYkFY=")

# create a dump.sql script of the given database
def create_dump():
    with open("dump.sql", 'w') as outfile:
        for line in connection.iterdump():
            outfile.write(f"{line}\n")
    # remove the database, we have the sql script
    delete_database()

# recreate the database based on the dump.sql script
def recreate_database():
    with open("dump.sql", 'r') as file:
        sql_script = file.read()
    delete_dump('dump.sql')
    connection = sqlite3.connect("sample_database.db")
    connection.executescript(sql_script)
    connection.commit()
    connection.close()
    quit()

# delete the dump.sql
def delete_dump(filename):
    if os.path.exists(filename):
        os.remove(filename)

# delete the database.db
def delete_database():
    connection.close()
    if os.path.exists("sample_database.db"):
        os.remove("sample_database.db")

# create an encrypted version of the dump.sql script
def encrypt_dump():
    with open('dump.sql', 'rb') as file:
        data = file.read()
        encrypted_data = key.encrypt(data)
        with open('encrypted_dump.sql', 'wb') as outfile:
            outfile.write(encrypted_data)
    # delete the unencrypted dump.sql script
    delete_dump('dump.sql')

# create a decrypted version of the dump.sql script
def decrypt_dump():
    with open('encrypted_dump.sql', 'rb') as file:
        data = file.read()
        decrypted_data = key.decrypt(data)
        with open('dump.sql', 'wb') as outfile:
            outfile.write(decrypted_data)
    delete_dump('encrypted_dump.sql')

print('menu')
print("1. Create Dump")
print("2. Encrypt Dump")
print("3. Decrypt Dump")
print("4. Recreate Database")
choice = int(input("Pick: "))

if choice == 1:
    create_dump()
elif choice == 2:
    encrypt_dump()
elif choice == 3:
    decrypt_dump()
elif choice == 4:
    recreate_database()

if os.path.exists('sample_database.db'):
    connection.close()