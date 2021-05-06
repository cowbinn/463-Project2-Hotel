from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
import sqlite3

window = Tk()
window.geometry("640x480")
width = 640
height = 480
window.title('Reservations')
window.geometry('640x480')
window.resizable(True, True)
background_color = 'light gray'
labelFrame = Frame(window, width=width, height=height)

def addReservation():

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
    websiteReservation_label = Entry(reservation_frame, bg='white', font=('Arial', 16))
    websiteReservation_label.place(x=40, y=330)

    rate_label = Label(reservation_frame, text='Rate($/Day)', bg=background_color, fg='black', font=('Arial', 16))
    rate_label.place(x=40, y=360)
    rate_label = Entry(reservation_frame, bg='white', font=('Arial', 16))
    rate_label.place(x=165, y=360)

    totalCharge_label = Label(reservation_frame, text='Total Charge', bg=background_color, fg='black', font=('Arial', 16))
    totalCharge_label.place(x=40, y=400)
    totalCharge_label = Entry(reservation_frame, bg='white', font=('Arial', 16))
    totalCharge_label.place(x=170, y=400)

    addReservation = Button(addResWindow, text="Click to add")
    addReservation.place(x=170, y=450)

def deleteReservation():
    addDelWindow = Toplevel(window)
    addDelWindow.title("Delete Reservation")
    addDelWindow.geometry("500x450")
    deleteReservation_frame = Frame(addDelWindow, width=400, height=850)
    deleteReservation_frame.place(x=0, y=0)

    reservation_label = Label(deleteReservation_frame, text='Enter Reservation Last Name', bg=background_color, font=('Arial', 16))
    reservation_text = Entry(deleteReservation_frame, bg='white', font=('Arial', 16))
    reservation_label.place(x=40, y=60)
    reservation_text.place(x=40, y=90)

    searchBtn = Button(addDelWindow, text="Search")
    searchBtn.place(x=40, y=120)


addReservation_btn = Button(labelFrame, text='Add Reservation', bg='white', font=('Arial', 16), command=addReservation)
addReservation_btn.place(x=220, y=10)
deleteReservation_btn = Button(labelFrame, text='Delete Reservation', bg='white', font=('Arial', 16), command=deleteReservation)
deleteReservation_btn.place(x=220, y=50)

labelFrame.place(x=0, y=0)
window.mainloop()


