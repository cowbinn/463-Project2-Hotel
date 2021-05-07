from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk

from c7c8 import daily_report_menu, search_menu
from Roomtype import roomType

root = Tk()
root.title("Main Screen")
root.geometry("800x600")

logo_label = Label(root, text="Antares Hotel Management Company", font=('Arial', 24)).place(x=120,y=10)

room_type_button = Button(root, text="C1 - Room Status", command=roomType)
room_type_button.place(x=280, y=100)

search_menu_button = Button(root, text="C7 - Search for Guest", command=search_menu)
search_menu_button.place(x=280, y=150)

daily_report_button = Button(root, text="C8 - Daily Report", command=daily_report_menu)
daily_report_button.place(x=280, y=200)


root.mainloop()