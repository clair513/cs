# -*- coding: utf-8 -*-
"""
Project: Data Extraction Tool
"""

# Loading dependencies:
from tkinter import *
from PIL import ImageTk, Image
import sqlite3


# Initiating GUI:
root = Tk()
root.title('Data Tool')
root.geometry('1020x700')


# Creating Test Database & Table:
conn = sqlite3.connect('gui_db.db')
c = conn.cursor()
c.execute("""CREATE TABLE sample (
        first_name text,
        last_name text,
        age integer,
        salary integer,
        organization text,
        tenure_months real,
        annual_rating integer
        )""")
conn.commit()
conn.close()



root.mainloop()