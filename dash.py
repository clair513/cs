"""
DESCRIPTION: Dashboard Prototype for GFIT Data Extraction Tool.

CRITICAL:
    > GUI Application Tkinter base is referred to as 'root'.
    > Input Pandas DataFrame necessarily needs to be renamed as 'df'.
"""


# Importing required packages:
import numpy as np
import pandas as pd
from tkinter import *
from tkinter.ttk import *
from pivottablejs import pivot_ui


# Publicly available sample DataFrame:
import seaborn as sns
df = sns.load_dataset('tips')


# Setting up application frame:
class myDash(Frame):

    # Initiating app base frame:
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.grid()
        self.create_widgets()

    # Creating widgets within application frame:
    def create_widgets(self):
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        # Calling 'winfo_toplevel' to get app root window (Avoid 'parent'):
        self.winfo_toplevel().title("Dashboard Prototype")
        #self.winfo_toplevel().geometry("1700x900")
        global df

        # Creating application header:
        header = Label(self, text='DATA EXTRACTION TOOL', font='Verdana')
        header.grid(row=0, column=0, padx=15, pady=5, columnspan=2)

        label = Entry(self, text='Sample Input Field: ')
        label.grid(row=1, column=0, padx=5, pady=10)

        btn = Button(self, text='Enter Value')
        btn.grid(row=1, column=1, padx=5)

        lf = Labelframe(self)
        lf.grid(row=2, column=0, sticky='nwes', padx=5, pady=5)
        tbl = pivot_ui(df)
        #tbl.grid(row=2, column=0, padx=10, pady=5, sticky=W, columnspan=2)
        canvas = FigureCanvasTkAgg(tbl, master=lf)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)


# Creating app main window ('root' later gets replaced):
if __name__ == '__main__':
    root = Tk()
    dash = myDash(root)
    root.mainloop()