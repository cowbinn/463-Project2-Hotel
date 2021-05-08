from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
import sqlite3


def housekeeping():
    c4window = Tk()
    c4window.geometry("1600x500")
    width = 640
    height = 480
    c4window.title('Housekeeping')
    c4window.resizable(True, True)
    background_color = 'light gray'
    labelFrame = Frame(c4window, width=width, height=height)
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()

    treeView = ttk.Treeview(c4window, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), show="headings", height=20)
    treeView.pack(side='right')
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
    treeView.column(4, width=150)
    treeView.column(5, width=120)
    treeView.column(5, width=120)
    treeView.column(6, width=120)
    treeView.column(7, width=120)
    treeView.column(8, width=120)
    treeView.column(9, width=120)
    treeView.column(10, width=120)

    sql = "SELECT RoomNumber, HousekeeperName, RoomType, RoomStatus, Bathroom, Towels, BedSheets," \
        "Vacuum, Dusting, Electronics FROM Room"
    data = cur.execute(sql)
    data = cur.fetchall()
    for i in data:
        treeView.insert('', 'end', values=i)

    
    def bathrooms():
        selected = treeView.focus()
        temp = treeView.item(selected, 'values')
        cur.execute("UPDATE Room SET Bathroom='Checked' WHERE RoomNumber=?", (temp[0],))
        conn.commit()
        treeView.item(selected, text="", values=(temp[0], temp[1], temp[2], temp[3],
                                                "Checked", temp[5], temp[6], temp[7], temp[8], temp[9]))

    def towels():
        selected = treeView.focus()
        temp = treeView.item(selected, 'values')
        cur.execute("UPDATE Room SET Towels='Checked' WHERE RoomNumber=?", (temp[0],))
        conn.commit()
        treeView.item(selected, text="", values=(temp[0], temp[1], temp[2], temp[3],
                                                temp[4], "Checked", temp[6], temp[7], temp[8], temp[9]))
    def bedsheets():
        selected = treeView.focus()
        temp = treeView.item(selected, 'values')
        cur.execute("UPDATE Room SET BedSheets='Checked' WHERE RoomNumber=?", (temp[0],))
        conn.commit()
        treeView.item(selected, text="", values=(temp[0], temp[1], temp[2], temp[3],
                                                temp[4], temp[5], "Checked", temp[7], temp[8], temp[9]))

    def vacuum():
        selected = treeView.focus()
        temp = treeView.item(selected, 'values')
        cur.execute("UPDATE Room SET Vacuum='Checked' WHERE RoomNumber=?", (temp[0],))
        conn.commit()
        treeView.item(selected, text="", values=(temp[0], temp[1], temp[2], temp[3],
                                                temp[4], temp[5], temp[6], "Checked", temp[8], temp[9]))

    def dusting():
        selected = treeView.focus()
        temp = treeView.item(selected, 'values')
        cur.execute("UPDATE Room SET Dusting='Checked' WHERE RoomNumber=?", (temp[0],))
        conn.commit()
        treeView.item(selected, text="", values=(temp[0], temp[1], temp[2], temp[3],
                                                temp[4], temp[5], temp[6], temp[7], "Checked", temp[9]))

    def electronics():
        selected = treeView.focus()
        temp = treeView.item(selected, 'values')
        cur.execute("UPDATE Room SET Electronics='Checked' WHERE RoomNumber=?", (temp[0],))
        conn.commit()
        treeView.item(selected, text="", values=(temp[0], temp[1], temp[2], temp[3],
                                                temp[4], temp[5], temp[6], temp[7], temp[8], "Checked"))

    def checkAll():
        selected = treeView.focus()
        temp = treeView.item(selected, 'values')
        cur.execute("UPDATE Room SET RoomStatus = 'Available', Bathroom='Checked', Towels='Checked', BedSheets='Checked',"
                    "Vacuum='Checked', Dusting='Checked', Electronics='Checked' WHERE RoomNumber=?", (temp[0],))
        conn.commit()
        treeView.item(selected, text="", values=(temp[0], temp[1], temp[2], "Available",
                                                "Checked", "Checked", "Checked", "Checked", "Checked", "Checked"))

    def unavailable_maintenance():
        selected = treeView.focus()
        temp = treeView.item(selected, 'values')
        cur.execute("UPDATE Room SET RoomStatus='Unavailable/Maintenance', Bathroom=NULL, Towels=NULL, BedSheets=NULL,"
                    "Vacuum=NULL, Dusting=NULL, Electronics=NULL WHERE RoomNumber=?", (temp[0],))
        conn.commit()
        treeView.item(selected, text="", values=(temp[0], temp[1], temp[2], "Unavailable/Maintenance",
                                                "None", "None", "None", "None", "None", "None"))


    instructions_label = Label(labelFrame, text='Select a room and then click any of the options to check off', bg=background_color, fg='black', font=('Arial', 12))
    instructions_label.place(x=50, y=5)

    bathroom_checkOff = Button(c4window, text="Check off Bathrooms", command=bathrooms)
    bathroom_checkOff.place(x=70, y=30)

    towels_checkOff = Button(c4window, text="Check off Towels", command=towels)
    towels_checkOff.place(x=70, y=60)

    bedsheets_checkOff = Button(c4window, text="Check off Bed Sheets", command=bedsheets)
    bedsheets_checkOff.place(x=70, y=90)

    vacuum_checkOff = Button(c4window, text="Check off Vacuum", command=vacuum)
    vacuum_checkOff.place(x=70, y=120)

    dusting_checkOff = Button(c4window, text="Check off Dusting", command=dusting)
    dusting_checkOff.place(x=70, y=150)

    electronics_checkOff = Button(c4window, text="Check off Electronics", command=electronics)
    electronics_checkOff.place(x=70, y=180)

    all_checkOff = Button(c4window, text="Check off All/Make Available", command=checkAll)
    all_checkOff.place(x=70, y=210)

    unavailable_changeStatus = Button(c4window, text="Unavailable/Maintenance", command=unavailable_maintenance)
    unavailable_changeStatus.place(x=70, y=240)

    labelFrame.place(x=0, y=0)


