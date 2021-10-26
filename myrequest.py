from tkinter import *
import sqlite3
from sqlite3.dbapi2 import Cursor

try:
    con = sqlite3.connect('dashboard.db')

    sql = """ALTER TABLE record
    ADD request TEXT"""

    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    cursor.close()

except sqlite3.Error as e:
    print("Error while altering table", e)

finally:
    if (con):
        con.close()
        print("Conexion closed")

ws = Tk()
ws.title('My_Request')
ws.geometry('940x500')
ws.config(bg='#0B5A81')

def insert_request_record():
    counter = 0
    warm = ''
    