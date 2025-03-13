import sqlite3
from cryptography.fernet import Fernet
import os
import shutil

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
    connection.executescript(sql_script)
    connection.commit()

# delete the dump.sql
def delete_dump(filename):
    if os.path.exists(filename):
        os.remove("dump.sql")

# delete the database.db
def delete_database():
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
    

connection.close()

