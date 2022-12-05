from tkinter import Tk, Frame, BOTH, ttk
from tkinter.ttk import Button, Style
from tkinter import *

from db import manage_db
from config import host, user, password, db_name


manager = manage_db()

global window
window = Tk()

class manage_db_Gui(Frame):
# DBMS: class to rule db

    def __init__(self, parent):
    # __init__ function for initalization off class methods and atributs
        frame_execute_btn = Frame.__init__(self, parent)
        self.parent = parent

        self.row_list = Listbox()
        self.row_list.pack(fill=BOTH, expand=True)
        self.scrollbar = ttk.Scrollbar(orient="vertical", command=self.row_list.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.label = ttk.Label()
        self.label.pack()

        self.initUI()
        self.centerWindow()
        self.entery_line()
        self.execute_btn()
        self.connect_to_db()


    def initUI(self):
        # Title name

        self.parent.title("manage_db")
        self.pack(fill=BOTH, expand=1)

    def centerWindow(self):
        # Place window on screen center

        w = 500
        h = 450

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))



    def read_line(self):
        # function for read entery line and execute SQL query

        self.label["text"] = entery.get()
        query = self.label["text"]

        # get names of collumns of table in select statement
        columns_names = manager.get_col_names(connection, query = query)
        print(columns_names)

        # execute data from table
        result = manager.execute_read_query(connection, query = query)
        result_arr = []
        try:
            for row in result:
                print(row)
                result_arr.append(row)
        except Exception as e:
            self.label["text"] = f"The error '{e}' occurred"
            print(f"The error '{e}' occurred")


        self.row_list.delete(0,END)


        for i in range(0, len(result_arr)):
            self.row_list.insert(0, result_arr[i])

        self.row_list.insert(0, columns_names)

    def execute_btn(self):
        # Create execute Button to execute sql queries

        btn = ttk.Button(window,  text="Execute", command=self.read_line)
        btn.pack()#anchor=NW, padx=6, pady=6)


    def connect_to_db(self):
        # connection to db

        global connection
        connection = manager.create_connection(host, user, password, db_name[0])

    def entery_line(self):
        # create line to enter queries

        global entery
        entery= ttk.Entry()
        entery.pack()



def __main__():
    window.geometry("250x150+300+300")
    app = manage_db_Gui(window)
    window.mainloop()

if __name__ == "__main__":
    __main__()
