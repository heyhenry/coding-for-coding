import sqlite3

# create the 'test.db' file if it does not exist, else connect to the existing 'test.db'
connection = sqlite3.connect(r"test.db")
# create cursor handle for invoking methods like executing SQLite statements and fetching data
cursor = connection.cursor()

# create the accounts table if it does not exist
create_table_statement = '''
CREATE TABLE IF NOT EXISTS accounts (
    Account_Name TEXT,
    Username TEXT,
    Password TEXT
);
'''
# execute the statement to create a table if it does not exist
cursor.execute(create_table_statement)

# force sqlite to fully sync the changes (i.e. creation of the database in this case)
sync_changes_statement = "PRAGMA synchronous = FULL;"
connection.execute(sync_changes_statement)

# drop a table (aka delete a table from the database)
# drop_table_statement = " drop table accounts "
# cursor.execute(drop_table_statement)

# insert values for a new account
insert_account_statement = " INSERT INTO accounts (Account_Name, Username, Password) values ('Crunchyroll', 'Henryyy', 'Kokoro91') "
cursor.execute(insert_account_statement)

# save changes to the database
connection.commit()

sql_query = "Select * FROM accounts"
cursor.execute(sql_query)
result = cursor.fetchall()
print(result)

# # retrieve the list of existing tables in the database
# sql_query = " PRAGMA table_list "
# cursor.execute(sql_query)
# # the cursor will be holding the results of the recent query
# result = cursor.fetchall()
# print(result)

# close the database
connection.close()
