from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
import sqlite3
from capability6 import room

def reservationSystem():
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()

    window = Tk()
    window.geometry("1600x500")
    width = 640
    height = 480
    window.title('Reservations')
    window.geometry('1600x500')
    window.resizable(True, True)
    background_color = 'light gray'
    labelFrame = Frame(window, width=width, height=height)

    treeView = ttk.Treeview(window, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), show="headings", height=20)
    treeView.pack(side='right')
    vertical_scroll_treeView = Scrollbar(window, orient="vertical", command=treeView.yview)
    vertical_scroll_treeView.pack(side='right',fill='y')
    treeView.configure(yscrollcommand=vertical_scroll_treeView.set)

    treeView.heading(1, text="First Name")
    treeView.heading(2, text="Last Name")
    treeView.heading(3, text="Date Made")
    treeView.heading(4, text="Date Check In")
    treeView.heading(5, text="Date Checkout")
    treeView.heading(6, text="Room Type")
    treeView.heading(7, text="Room Number")
    treeView.heading(8, text="Website Reservation Made")
    treeView.heading(9, text="Rate($/Day)")
    treeView.heading(10, text="Total Charge")

    treeView.column(1, width=120)
    treeView.column(2, width=120)
    treeView.column(3, width=120)
    treeView.column(4, width=120)
    treeView.column(5, width=120)
    treeView.column(5, width=120)
    treeView.column(6, width=120)
    treeView.column(7, width=120)
    treeView.column(8, width=160)
    treeView.column(9, width=120)
    treeView.column(10, width=120)

    sql = "SELECT guests.first_name, guests.last_name, Room.DateMade, Room.CheckInDate, Room.CheckOutDate, " \
          "Room.RoomType, Room.RoomNumber, Room.WebsiteReservation, Room.RoomRate, Room.TotalCharge FROM guests " \
          "INNER JOIN ROOM ON guests.guest_id = room.GuestID"
    data = cur.execute(sql)
    data = cur.fetchall()
    for i in data:
        treeView.insert('', 'end', values=i)

    def addReservation():

        def insert():
            roomScript = "UPDATE Room SET DateMade = ?, CheckInDate = ?, CheckOutDate = ?, RoomType = ?, " \
                         "RoomNumber = ?, WebsiteReservation = ?, RoomRate = ?, TotalCharge = ? WHERE RoomNumber = " + str(roomNumber_text.get())
            guestScript = "UPDATE guests SET first_name = ?, last_name = ? WHERE guest_id = " + str(roomNumber_text.get())
            cur.execute(roomScript, (str(dateMade_text.get()), str(dateCheckIn_label.get()), str(dateCheckOut_label.get()),
                        str(roomType_text.get()), str(roomNumber_text.get()), str(websiteReservation_text.get()), str(rate_text.get()),
                        str(totalCharge_text.get())))
            cur.execute(guestScript, (str(firstName_text.get()), str(lastName_text.get())))
            conn.commit()

        addResWindow = Toplevel(window)
        addResWindow.title("Add Reservation")
        addResWindow.geometry("500x550")
        reservation_frame = Frame(addResWindow, width=400, height=850)
        reservation_frame.place(x=0, y=0)

        firstName_label = Label(reservation_frame, text='First Name', bg=background_color, font=('Arial', 16))
        firstName_text = Entry(reservation_frame, bg='white', font=('Arial', 16))
        firstName_label.place(x=40, y=20)
        firstName_text.place(x=150, y=20)

        lastName_label = Label(reservation_frame, text='Last Name', bg=background_color, font=('Arial', 16))
        lastName_text = Entry(reservation_frame, bg='white', font=('Arial', 16))
        lastName_label.place(x=40, y=60)
        lastName_text.place(x=150, y=60)

        dateMade_label = Label(reservation_frame, text='Date Made', bg=background_color, fg='black',
                               font=('Arial', 16))
        dateMade_label.place(x=40, y=100)
        dateMade_text = DateEntry(reservation_frame, bg='white', font=('Arial', 16))
        dateMade_text.place(x=150, y=100)
        dateMade_text.delete(0, END)

        dateCheckIn_label = Label(reservation_frame, text='Date Check In', bg=background_color, fg='black',
                               font=('Arial', 16))
        dateCheckIn_label.place(x=40, y=140)
        dateCheckIn_label = DateEntry(reservation_frame, bg='white', font=('Arial', 16))
        dateCheckIn_label.place(x=180, y=140)
        dateCheckIn_label.delete(0, END)

        dateCheckOut_label = Label(reservation_frame, text='Date Check Out', bg=background_color, fg='black',
                               font=('Arial', 16))
        dateCheckOut_label.place(x=40, y=180)
        dateCheckOut_label = DateEntry(reservation_frame, bg='white', font=('Arial', 16))
        dateCheckOut_label.place(x=200, y=180)
        dateCheckOut_label.delete(0, END)

        roomType_label = Label(reservation_frame, text='Room Type', bg=background_color, fg='black', font=('Arial', 16))
        roomType_label.place(x=40, y=220)
        roomType_text = Entry(reservation_frame, bg='white', font=('Arial', 16))
        roomType_text.place(x=155, y=220)

        roomNumber_label = Label(reservation_frame, text='Room Number', bg=background_color, fg='black', font=('Arial', 16))
        roomNumber_label.place(x=40, y=260)
        roomNumber_text = Entry(reservation_frame, bg='white', font=('Arial', 16))
        roomNumber_text.place(x=180, y=260)

        websiteReservation_label = Label(reservation_frame, text='Website Reservation Made', bg=background_color, fg='black', font=('Arial', 16))
        websiteReservation_label.place(x=40, y=300)
        websiteReservation_text = Entry(reservation_frame, bg='white', font=('Arial', 16))
        websiteReservation_text.place(x=40, y=330)

        rate_label = Label(reservation_frame, text='Rate($/Day)', bg=background_color, fg='black', font=('Arial', 16))
        rate_label.place(x=40, y=360)
        rate_text = Entry(reservation_frame, bg='white', font=('Arial', 16))
        rate_text.place(x=165, y=360)

        totalCharge_label = Label(reservation_frame, text='Total Charge', bg=background_color, fg='black', font=('Arial', 16))
        totalCharge_label.place(x=40, y=400)
        totalCharge_text = Entry(reservation_frame, bg='white', font=('Arial', 16))
        totalCharge_text.place(x=170, y=400)

        addReservation = Button(addResWindow, text="Click to add", command=insert)
        addReservation.place(x=170, y=450)


    def deleteReservation():
        row_id = treeView.selection()[0]
        treeView.delete(row_id)

    addReservation_btn = Button(labelFrame, text='Add Reservation', bg='white', font=('Arial', 16), command=addReservation)
    addReservation_btn.place(x=160, y=130)
    deleteReservation_btn = Button(labelFrame, text='Delete Reservation', bg='white', font=('Arial', 16), command=deleteReservation)
    deleteReservation_btn.place(x=135, y=230)
    cap6_btn = Button(labelFrame, text='Check In', bg='white', font=('Arial', 16), command=room(101))
    cap6_btn.place(x=135, y=330)

    labelFrame.place(x=0, y=0)
    window.mainloop()
