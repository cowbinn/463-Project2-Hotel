from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk

from c7c8 import daily_report_menu, search_menu
from Roomtype import roomType
from Room import RoomAvailibity
from c4 import housekeeping

root = Tk()
root.title("Main Screen")
root.geometry("600x300")

logo_label = Label(root, text="Antares Hotel Management Company", font=('Arial', 18)).place(x=100,y=30)

room_type_button = Button(root, text="C1 - Room Status", command=roomType)
room_type_button.place(x=100, y=120)

room_list_button = Button(root, text="C2 - Room List", command=RoomAvailibity)
room_list_button.place(x=400, y=120)

reservation_button = Button(root, text="C3 - Reservation", command=print('reservationfunctionhere'))
reservation_button.place(x=100, y=170)

housekeeping_button = Button(root, text="C4 - Housekeeping", command=housekeeping)
housekeeping_button.place(x=400, y=170)


search_menu_button = Button(root, text="C7 - Search for Guest", command=search_menu)
search_menu_button.place(x=100, y=220)

daily_report_button = Button(root, text="C8 - Daily Report", command=daily_report_menu)
daily_report_button.place(x=400, y=220)


root.mainloop()