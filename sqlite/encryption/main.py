import sqlite3
from cryptography.fernet import Fernet
import os
import shutil

connection = sqlite3.connect("sample_database.db")
cursor = connection.cursor()
key = Fernet("UBy1tA_tENd8h7NfXqNwH5c5Sx2H2CkqXbN1RXJYkFY=")

def create_dump():
    with open("dump.sql", 'w') as outfile:
        for line in connection.iterdump():
            outfile.write(f"{line}\n")

def restore_dump():
    with open("dump.sql", 'r') as file:
        sql_script = file.read()
    connection.executescript(sql_script)
    connection.commit()

def delete_dump():
    if os.path.exists("dump.sql"):
        os.remove("dump.sql")

def delete_database():
    if os.path.exists("sample_database.db"):
        os.remove("sample_database.db")

def encrypt_dump():
    with open('dump.sql', 'rb') as file:
        data = file.read()
        encrypted_data = key.encrypt(data)
        with open('encrypted_dump.sql', 'wb') as outfile:
            outfile.write(encrypted_data)

def decrypt_dump():
    with open('encrypted_dump.sql', 'rb') as file:
        data = file.read()
        decrypted_data = key.decrypt(data)
        with open('dump.sql', 'wb') as outfile:
            outfile.write(decrypted_data)
    

# create_dump()
# restore_dump()
# delete_dump()
# delete_database()
# encrypt_dump()
decrypt_dump()

connection.close()

