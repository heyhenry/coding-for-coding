import sqlite3
from cryptography.fernet import Fernet
import os
import shutil

connection = sqlite3.connect("sample_database.db")
cursor = connection.cursor()
# key = Fernet("123")

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

# def encrypt_sql_data(dump_file, enc):

# create_dump()
# restore_dump()
delete_dump()
connection.close()

