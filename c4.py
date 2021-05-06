from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
import sqlite3

window = Tk()
window.geometry("1600x500")
width = 640
height = 480
window.title('Housekeeping')
window.resizable(True, True)
background_color = 'light gray'
labelFrame = Frame(window, width=width, height=height)

treeView = ttk.Treeview(window, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), show="headings", height=20)
treeView.pack()
treeView.heading(1, text="Room number")
treeView.heading(2, text="Housekeeper Name")
treeView.heading(3, text="Room Type")
treeView.heading(4, text="Room Status")
treeView.heading(5, text="Bathroom")
treeView.heading(6, text="Towels")
treeView.heading(7, text="Bed Sheets")
treeView.heading(8, text="Vacuum")
treeView.heading(9, text="Dusting")
treeView.heading(10, text="Electronics")

treeView.column(1, width=120)
treeView.column(2, width=120)
treeView.column(3, width=120)
treeView.column(4, width=120)
treeView.column(5, width=120)
treeView.column(5, width=120)
treeView.column(6, width=120)
treeView.column(7, width=120)
treeView.column(8, width=120)
treeView.column(9, width=120)
treeView.column(10, width=120)

instructions_label = Label(labelFrame, text='Select a room and then click any of the options to check off', bg=background_color, fg='black', font=('Arial', 12))
instructions_label.place(x=160, y=450)

bathroom_checkOff = Button(window, text="Check off Bathrooms")
bathroom_checkOff.place(x=70, y=30)

towels_checkOff = Button(window, text="Check off Towels")
towels_checkOff.place(x=70, y=60)

bedsheets_checkOff = Button(window, text="Check off Bed Sheets")
bedsheets_checkOff.place(x=70, y=90)

vacuum_checkOff = Button(window, text="Check off Vacuum")
vacuum_checkOff.place(x=70, y=120)

dusting_checkOff = Button(window, text="Check off Dusting")
dusting_checkOff.place(x=70, y=150)

electronics_checkOff = Button(window, text="Check off Electronics")
electronics_checkOff.place(x=70, y=180)

all_checkOff = Button(window, text="Check off All")
all_checkOff.place(x=70, y=210)

labelFrame.place(x=0, y=0)
window.mainloop()