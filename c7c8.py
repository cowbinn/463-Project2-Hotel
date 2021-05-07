from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk
from tkcalendar import Calendar
from capability5 import guestInfo

# Database connection
conn = sqlite3.connect('hotel.db')
cur = conn.cursor()

def search_menu():
    search_guest = Tk()
    search_guest.title('Search for Guests')
    search_guest.geometry('900x400')

    searched_label = Label(search_guest)
    my_tree = ttk.Treeview(search_guest)
    open_guest_button = Button(search_guest)

    def search():
        nonlocal searched_label
        nonlocal my_tree
        nonlocal open_guest_button
        search_info = search_box.get()
        dropdown_selected = dropdown.get()
        
        # searching by selected item
        if dropdown_selected == "First Name":
            sql = "SELECT GUESTs.guest_id, GUESTS.first_name, GUESTS.last_name, ROOM.RoomNumber, GUESTS.phone_number, \
                        GUESTS.street_address, ROOM.CheckInDate, ROOM.CheckOutDate, ROOM.PaymentsMade \
                        FROM GUESTS INNER JOIN ROOM ON GUESTS.guest_id = ROOM.GuestID \
                        WHERE first_name = '" + search_info + "'"
        elif dropdown_selected == "Last Name":
            sql = "SELECT GUESTs.guest_id, GUESTS.first_name, GUESTS.last_name, ROOM.RoomNumber, GUESTS.phone_number, \
                        GUESTS.street_address, ROOM.CheckInDate, ROOM.CheckOutDate, ROOM.PaymentsMade \
                        FROM GUESTS INNER JOIN ROOM ON GUESTS.guest_id = ROOM.GuestID \
                        WHERE last_name = '" + search_info + "'"
        elif dropdown_selected == "Room Number":
            sql = "SELECT GUESTs.guest_id, GUESTS.first_name, GUESTS.last_name, ROOM.RoomNumber, GUESTS.phone_number, \
                        GUESTS.street_address, ROOM.CheckInDate, ROOM.CheckOutDate, ROOM.PaymentsMade \
                        FROM GUESTS INNER JOIN ROOM ON GUESTS.guest_id = ROOM.GuestID \
                        WHERE RoomNumber = '" + search_info + "'"
        elif dropdown_selected == "Phone Number":
            sql = "SELECT GUESTs.guest_id, GUESTS.first_name, GUESTS.last_name, ROOM.RoomNumber, GUESTS.phone_number, \
                        GUESTS.street_address, ROOM.CheckInDate, ROOM.CheckOutDate, ROOM.PaymentsMade \
                        FROM GUESTS INNER JOIN ROOM ON GUESTS.guest_id = ROOM.GuestID \
                        WHERE phone_number = '" + search_info + "'"
        elif dropdown_selected == "Street Address":
            sql = "SELECT GUESTs.guest_id, GUESTS.first_name, GUESTS.last_name, ROOM.RoomNumber, GUESTS.phone_number, \
                        GUESTS.street_address, ROOM.CheckInDate, ROOM.CheckOutDate, ROOM.PaymentsMade \
                        FROM GUESTS INNER JOIN ROOM ON GUESTS.guest_id = ROOM.GuestID \
                        WHERE street_address = '" + search_info + "'"
        elif dropdown_selected == "Check-In Date":
            sql = "SELECT GUESTs.guest_id, GUESTS.first_name, GUESTS.last_name, ROOM.RoomNumber, GUESTS.phone_number, \
                        GUESTS.street_address, ROOM.CheckInDate, ROOM.CheckOutDate, ROOM.PaymentsMade \
                        FROM GUESTS INNER JOIN ROOM ON GUESTS.guest_id = ROOM.GuestID \
                        WHERE CheckInDate = '" + search_info + "'"
        elif dropdown_selected == "Check-Out Date":
            sql = "SELECT GUESTs.guest_id, GUESTS.first_name, GUESTS.last_name, ROOM.RoomNumber, GUESTS.phone_number, \
                        GUESTS.street_address, ROOM.CheckInDate, ROOM.CheckOutDate, ROOM.PaymentsMade \
                        FROM GUESTS INNER JOIN ROOM ON GUESTS.guest_id = ROOM.GuestID \
                        WHERE CheckOutDate = '" + search_info + "'"
        # execute and retrieve data
        result = cur.execute(sql)
        result = cur.fetchall()
        # record not found
        if not result:
            result = "Record Not Found..."
            searched_label.destroy()
            my_tree.destroy()
            open_guest_button.destroy()
            searched_label = Label(search_guest, text=result)
            searched_label.pack()
        # show results
        else:    
            #header_list = ["First Name", "Last Name", "Room Number", "Phone Number", "Street Address", "Check-In Date", "Check-Out Date", "Price Paid"]
            my_tree.destroy()
            searched_label.destroy()
            open_guest_button.destroy()
            my_tree = ttk.Treeview(search_guest, columns=(1,2,3,4,5,6,7,8,9), show="headings", height="5")
            my_tree.pack()
            my_tree.heading(1, text="Guest ID")
            my_tree.column(1, width=100, anchor='center')
            my_tree.heading(2, text="First Name")
            my_tree.column(2, width=100, anchor='center')
            my_tree.heading(3, text="Last Name")
            my_tree.column(3, width=100, anchor='center')
            my_tree.heading(4, text="Room Number")
            my_tree.column(4, width=100, anchor='center')
            my_tree.heading(5, text="Phone Number")
            my_tree.column(5, width=100, anchor='center')
            my_tree.heading(6, text="Street Address")
            my_tree.column(6, width=100, anchor='center')
            my_tree.heading(7, text="Check-In Date")
            my_tree.column(7, width=100, anchor='center')
            my_tree.heading(8, text="Check-Out Date")
            my_tree.column(8, width=100, anchor='center')
            my_tree.heading(9, text="Price Paid")
            my_tree.column(9, width=100, anchor='center')
            
            for i in result:
                my_tree.insert('', 'end', values=i)
            curItem = my_tree.focus()
            values = my_tree.item(my_tree.focus())
            print(values)
            open_guest_button = Button(search_guest, text="View Guest Info", command=lambda: guestInfo(my_tree.item(my_tree.focus())["values"][1] + " " + my_tree.item(my_tree.focus())["values"][2] + " " + str(my_tree.item(my_tree.focus())["values"][0])) )
            open_guest_button.pack(pady=5)



    # search label
    search_box_label = Label(search_guest, text="Search: ")
    search_box_label.pack(pady=10)
    # search box
    search_box = Entry(search_guest)
    search_box.pack(pady=5)
    # search button
    search_button = Button(search_guest, text="Submit", command=search)
    search_button.pack(pady=5)
    # dropdown box
    selection_list = ["First Name", "Last Name", "Room Number", "Phone Number", "Street Address", "Check-In Date", "Check-Out Date"]
    dropdown = ttk.Combobox(search_guest, value=selection_list)
    dropdown.current(0)
    dropdown.pack(pady=5)

def daily_report_menu():
    daily_report = Tk()
    daily_report.title('Daily Report')
    daily_report.geometry('600x600')

    my_tree1 = ttk.Treeview(daily_report)
    daily_total = Label(daily_report)


    def search():
        nonlocal my_tree1
        nonlocal daily_total

        # execute and retrieve data
        sql = "SELECT ROOM.RoomNumber, GUESTS.first_name, GUESTS.last_name, ROOM.CheckInDate, ROOM.CheckOutDate, ROOM.PaymentsMade \
                        FROM GUESTS INNER JOIN ROOM ON GUESTS.guest_id = ROOM.GuestID \
                        WHERE CheckInDate = '" + cal.get_date() + "'"
        result = cur.execute(sql)
        result = cur.fetchall()

        sql_sum = "SELECT sum(PaymentsMade) FROM ROOM WHERE CheckInDate ='" + cal.get_date() + "'"
        sum = cur.execute(sql_sum)
        sum = cur.fetchone()
        total = sum[0]

        
        # show tree in window
        my_tree1.destroy()
        my_tree1 = ttk.Treeview(daily_report, columns=(1,2,3,4,5,6,7,8), show="headings", height="10")
        my_tree1.pack(pady=20)
        my_tree1.heading(1, text="Room Number")
        my_tree1.column(1, width=100, anchor='center')
        my_tree1.heading(2, text="First Name")
        my_tree1.column(2, width=100, anchor='center')
        my_tree1.heading(3, text="Last Name")
        my_tree1.column(3, width=100, anchor='center')
        my_tree1.heading(4, text="Check-In Date")
        my_tree1.column(4, width=100, anchor='center')
        my_tree1.heading(5, text="Check-Out Date")
        my_tree1.column(5, width=100, anchor='center')
        my_tree1.heading(6, text="Price Paid")
        my_tree1.column(6, width=100, anchor='center')
        for i in result:
            my_tree1.insert('', 'end', values=i)

        # show total in window
        total_str = 'Total Dollars Paid: $' + str(total)
        daily_total.destroy()
        daily_total = Label(daily_report, text=total_str)
        daily_total.pack()

    # search label
    daily_report_label = Label(daily_report, text="Daily Report: ")
    daily_report_label.pack()
    # Add calendar
    cal = Calendar(daily_report, selectmode = 'day')
    cal.pack(pady=5)
    # search button
    search_button = Button(daily_report, text="Submit", command=search)
    search_button.pack(pady=5)
    # Daily total label



