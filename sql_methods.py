from random import randint
import sqlite3

def insert_number(table_name, number):
    with sqlite3.connect('numbers.db') as connection:
        cursor = connection.cursor()
        sql = f'''INSERT INTO {table_name}(
                phone_number) VALUES ({number});'''
        cursor.execute(sql)

def get_phone_number():
    with sqlite3.connect('numbers.db') as connection:
        cursor = connection.cursor()
        sql = f'''SELECT * FROM phone_numbers WHERE pk={randint(1, 10000)};'''
        cursor.execute(sql)
        return cursor.fetchone()

def check_table(number):
    with sqlite3.connect('numbers.db') as connection:
        cursor = connection.cursor()
        sql = f'''SELECT * FROM already_used_phone_numbers WHERE phone_number = {number};'''
        cursor.execute(sql)
        return cursor.fetchone()

# def read_table():
#     with sqlite3.connect('numbers.db') as connection:
#         cursor = connection.cursor()
#         sql = f'''SELECT * FROM already_used_phone_numbers;'''
#         cursor.execute(sql)
#         nums = cursor.fetchall()
#         print(nums)

# if __name__ == '__main__':
#     read_table()
