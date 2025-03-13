import sqlite3

connection = sqlite3.connect("sample_database.db")
cursor = connection.cursor()


def create_dump():
    with open("dump.sql", 'w') as outfile:
        for line in connection.iterdump():
            outfile.write(f"{line}\n")

def restore_dump():
    with open("dump.sql", 'r') as file:
        sql_script = file.read()
    connection.executescript(sql_script)
    connection.commit()

# create_dump()
restore_dump()

connection.close()

