from tkinter import *
import sqlite3
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from capability5 import guestInfo


def checkIn(guestName, checkInDate, checkOutDate, roomNumber, totalCharge, paymentsMade, balance, label, window):
    if len(guestName.get()) == 0 or len(checkInDate.get()) == 0 or len(
            checkOutDate.get()) == 0 or len(totalCharge.get()) == 0 or len(paymentsMade.get()) == 0 or len(
        balance.get()) == 0:
        error = ''
        if len(guestName.get()) == 0:
            error += 'Guest Name not selected\n'
        if len(checkInDate.get()) == 0:
            error += 'Check In Date not selected\n'
        if len(checkOutDate.get()) == 0:
            error += 'Check Out Date not selected\n'
        if len(totalCharge.get()) == 0:
            error += 'Total Charge is not a number\n'
        if len(paymentsMade.get()) == 0:
            error += 'Payments Made is not a number\n'
        if len(balance.get()) == 0:
            error += 'Balance is not a number\n'
        messagebox.showerror('Missing Information', error)
    else:
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        sql = 'UPDATE Room SET RoomStatus = "Unavailable/Occupied", CheckInDate = "' + str(
            checkInDate.get()) + '", CheckOutDate = "' + str(
            checkOutDate.get()) + '", GuestID = ' + str(guestName.get().rsplit(' ', 1)[1]) + ', TotalCharge = ' + str(
            totalCharge.get()) + ', PaymentsMade = ' + str(paymentsMade.get())+ ', CheckIN = ' + str(1) + ', Balance = ' + str(
            balance.get()) + ' WHERE roomNumber = ' + str(roomNumber.get())
        cur.execute(sql)
        conn.commit()
        messagebox.showinfo('Check In Success', 'Guest ' + guestName.get().rsplit(' ', 1)[0] + ' is checked in')
        window.destroy()
        label.configure(bg="blue", fg="black")


def checkOut(roomNumber, label, window):
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    sql = 'UPDATE Room SET RoomStatus = "Unavailable/Dirty", CHeckIN = ' + str(
            0) + ', GuestID = '+ str('null') +'  WHERE roomNumber = ' + str(roomNumber.get())
    cur.execute(sql)
    conn.commit()
    messagebox.showinfo('Check Out Success', 'Checked Out Successfully')
    window.destroy()
    label.configure(bg="pink", fg="black")


def my_tracer(a, b, c):
    new_a = a.get()
    if new_a == '':
        new_a = 0.0
    new_b = b.get()
    if new_b == '':
        new_b = 0.0
    new_c = float(new_a) - float(new_b)
    c.config(state=NORMAL)
    c.delete(0, END)
    c.insert(0, new_c)
    c.config(state=DISABLED)


def room(roomNumber, label, firstName=None, lastName=None, dateMade=None, dateCheckIn=None, dateCheckOut=None):
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    sql = 'SELECT * FROM Room WHERE RoomNumber=' + str(roomNumber)
    cur.execute(sql)
    result = cur.fetchall()
    print(result)

    window = Toplevel()
    width = 400
    height = 850
    background_color = 'light gray'
    window.title('Guest Information')
    window.geometry('400x850')
    window.resizable(False, False)

    label_frame = Frame(window, width=width, height=height, bg=background_color)

    guest_name_label = Label(label_frame, text='Guest Name', bg=background_color, font=('Arial', 16))
    guest_name_label.place(x=40, y=20)

    check_in_label = Label(label_frame, text='Check In Date and Time', bg=background_color, fg='black',
                           font=('Arial', 16))
    check_in_label.place(x=40, y=100)
    check_in_text = DateEntry(label_frame, bg='white', font=('Arial', 16))
    check_in_text.place(x=40, y=130)
    check_in_text.delete(0, END)

    expected_check_out_label = Label(label_frame, text='Expected Check Out Date and Time', bg=background_color,
                                     fg='black', font=('Arial', 16))
    expected_check_out_label.place(x=40, y=180)
    expected_check_out_text = DateEntry(label_frame, bg='white', font=('Arial', 16))
    expected_check_out_text.place(x=40, y=210)
    expected_check_out_text.delete(0, END)

    room_number_label = Label(label_frame, text='Room Number', bg=background_color, fg='black',
                              font=('Arial', 16))
    room_number_label.place(x=40, y=260)
    room_number_text = Entry(label_frame, bg='white', font=('Arial', 16))
    room_number_text.place(x=40, y=290)
    room_number_text.insert(0, roomNumber)
    room_number_text.config(state='disabled')

    room_type_label = Label(label_frame, text='Room Type', bg=background_color, fg='black', font=('Arial', 16))
    room_type_label.place(x=40, y=340)
    room_type_text = Entry(label_frame, bg='white', font=('Arial', 16))
    room_type_text.place(x=40, y=370)
    room_type_text.insert(0, result[0][1])
    room_type_text.config(state='disabled')

    room_rate_label = Label(label_frame, text='Room Rate ($/Day)', bg=background_color, fg='black',
                            font=('Arial', 16))
    room_rate_label.place(x=40, y=420)
    room_rate_text = Entry(label_frame, bg='white', font=('Arial', 16))
    room_rate_text.place(x=40, y=450)
    room_rate_text.insert(0, '$' + str(result[0][3]))
    room_rate_text.config(state='disabled')

    total_charge_var = StringVar()
    total_charge_label = Label(label_frame, text='Total Charge', bg=background_color, fg='black',
                               font=('Arial', 16))
    total_charge_label.place(x=40, y=500)
    total_charge_text = Entry(label_frame, bg='white', font=('Arial', 16), textvariable=total_charge_var)
    total_charge_text.place(x=40, y=530)

    payments_made_var = StringVar()
    payments_made_label = Label(label_frame, text='Payments Made', bg=background_color, fg='black',
                                font=('Arial', 16))
    payments_made_label.place(x=40, y=580)
    payments_made_text = Entry(label_frame, bg='white', font=('Arial', 16), textvariable=payments_made_var)
    payments_made_text.place(x=40, y=610)

    balance_label = Label(label_frame, text='Balance', bg=background_color, fg='black', font=('Arial', 16))
    balance_label.place(x=40, y=660)
    balance_text = Entry(label_frame, bg='white', font=('Arial', 16))
    balance_text.place(x=40, y=690)
    balance_text.config(state='disabled')

    total_charge_var.trace('w', lambda a, b, c: my_tracer(total_charge_text, payments_made_text, balance_text))
    payments_made_var.trace('w', lambda a, b, c: my_tracer(total_charge_text, payments_made_text, balance_text))

    if result[0][2] == 'Unavailable/Occupied':
        cur = conn.cursor()
        sql = 'SELECT first_name, last_name, guest_id FROM guests WHERE guest_id=' + str(result[0][6])
        cur.execute(sql)
        guest = cur.fetchall()

        guest_name_text = Entry(label_frame, bg='white', fg='black', font=('Arial', 16))
        guest_name_text.place(x=40, y=50)
        guest_name_text.insert(0, str(guest[0][0]) + ' ' + str(guest[0][1]) + ' ' + str(result[0][6]))
        guest_name_text.config(state='disabled')

        check_in_text.insert(0, result[0][4])
        # check_in_text.config(state='disabled')
        expected_check_out_text.insert(0, result[0][5])
        # expected_check_out_text.config(state='disabled')
        total_charge_text.insert(0, result[0][7])
        # total_charge_text.config(state='disabled')
        payments_made_text.insert(0, result[0][8])
        # payments_made_text.config(state='disabled')
        balance_text.insert(0, result[0][9])
        balance_text.config(state='disabled')
        btn = Button(label_frame, text='Check Out', bg='white', font=('Arial', 16),
                     command=lambda room_number=room_number_text, l=label, w=window: checkOut(room_number, l, w))

        view_button = Button(label_frame, text='View Guest', font=('Arial', 12),
                             command=lambda: guestInfo(guest_name_text.get()))

        btn.place(x=140, y=760)
        view_button.place(x=305, y=50)

    elif result[0][2] == 'Available':
        if firstName is None and lastName is None and dateCheckIn is None and dateCheckOut is None:
            cur = conn.cursor()
            sql = 'SELECT first_name, last_name, guest_id FROM guests'
            cur.execute(sql)
            guests = cur.fetchall()
            guests = sorted(guests)

            guest_name_text = ttk.Combobox(label_frame, font=('Arial', 16))
            guest_name_text.place(x=40, y=50)
            guest_name_text['values'] = guests
            label_frame.option_add('*TCombobox*Listbox.font', ('Arial', 16))
            check_in_text.config(state='readonly')
            expected_check_out_text.config(state='readonly')
        else:
            guest_name_text = Entry(label_frame, font=('Arial', 16))
            guest_name_text.place(x=40, y=50)
            guest_name_text.insert(0, str(firstName) + ' ' + str(lastName))
            guest_name_text.config(state='disabled')
            check_in_text.insert(0, dateCheckIn)
            check_in_text.config(state='disabled')
            expected_check_out_text.insert(0, dateCheckOut)
            expected_check_out_text.config(state='disabled')

        btn = Button(label_frame, text='Check In', bg='white', font=('Arial', 16),
                     command=lambda guest_name=guest_name_text, check_in_date=check_in_text,
                                    check_out_date=expected_check_out_text, room_number=room_number_text,
                                    total_charge=total_charge_text,
                                    payments_made=payments_made_text, balance=balance_text, l=label, w=window: checkIn(guest_name,
                                                                                                    check_in_date,
                                                                                                    check_out_date,
                                                                                                    room_number,
                                                                                                    total_charge,
                                                                                                    payments_made,
                                                                                                    balance, l, w))

        view_button = Button(label_frame, text='View Guest', font=('Arial', 12),
                             command=lambda: guestInfo(guest_name_text.get()))

        btn.place(x=140, y=760)
        view_button.place(x=305, y=50)

    label_frame.place(x=0, y=0)
    window.mainloop()