import sqlite3 

def schema(dbpath= 'numbers.db'):
    with sqlite3.connect(dbpath) as connection:
        cursor = connection.cursor()

        sql = '''CREATE TABLE phone_numbers(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        phone_number TEXT
        );'''

        cursor.execute(sql)

        sql = '''CREATE TABLE already_used_phone_numbers(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        phone_number TEXT
        );'''

        cursor.execute(sql)
  
if __name__ == "__main__":
  schema()
