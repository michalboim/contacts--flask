import sqlite3
from classes import Contact

def get_db(crud:str):
    with sqlite3.connect ('contacts.db') as conn:
        cur=conn.cursor()
        cur.execute(crud)
    return cur.fetchall()

def create_contact(table, column, value ):
    return get_db(F"INSERT INTO {table} ({column}) VALUES ({value})")

def read_all_contacts(table):
    return get_db(f"SELECT * FROM {table}")

def read_contact(table,tid:int):
    return get_db(f"SELECT * FROM {table} WHERE ID='{tid}'")

def delete_contact (table,tid:int):
    return get_db(f"DELETE FROM {table} WHERE ID={tid}")

def update_contact(table, column, new_value, tid:int):
    return get_db(f"UPDATE {table} SET ({column})=({new_value}) WHERE ID='{tid}'")

def search_name(table,name):
    return get_db(f"SELECT * FROM {table} WHERE name LIKE '{name}%'")

#contacts_info.sort(key=lambda c:c.name)