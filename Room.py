from tkinter import  Label, Menubutton, Tk, Scrollbar
from tkinter import *
import array
import tkinter.messagebox
from datetime import *
import calendar
import sqlite3
import datetime
from datetime import date
from capability6 import room
from c3 import reservationSystem


def RoomAvailibity():
    currentDate= datetime.datetime.now()
    currentDay= date.today()#current date for schedule
    nextDay1=date.today() + datetime.timedelta(days=1)
    nextDay2=date.today() + datetime.timedelta(days=2)
    nextDay3=date.today() + datetime.timedelta(days=3)
    nextDay4=date.today() + datetime.timedelta(days=4)
    nextDay5=date.today() + datetime.timedelta(days=5)
    nextDay6=date.today() + datetime.timedelta(days=6)
    nextDay7=date.today() + datetime.timedelta(days=7)

    year = currentDate.year
    day= currentDate.day
    month= currentDate.month

    # root=Tk()
    # root.title("Key")
    # root.geometry("200x200+1000+100")
    c2window= Tk()
    c2window.title("Available rooms")
    c2window.geometry("1000x600+10+100")
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    sql = ' SELECT * FROM Room'
    cur.execute(sql)
    getAll = cur.fetchall()
    print(getAll[0])

    def checkIn(h):
        c2window.destroy()
        room(h)
        
        
    a=99

    for row in range (22):

        for column in range (9):

            if row == 0 :  #day of the week
                lable0= Label(c2window, text="Room Number",bg="black",fg="white",padx= 3,pady=3)
                lable0.grid(row=0, column=0,sticky= "nsew",padx= 1,pady=1)
                lable3 = Label(c2window, text=currentDay.strftime('%A'),bg="black",fg="white",padx= 3,pady=3 )
                lable3.grid(row=0, column=1,sticky= "nsew",padx= 1,pady=1)
                lable4 = Label(c2window, text=nextDay1.strftime('%A'),bg="black",fg="white",padx= 3,pady=3 )
                lable4.grid(row=0, column=2,sticky= "nsew",padx= 1,pady=1)
                lable3 = Label(c2window, text=nextDay2.strftime('%A'),bg="black",fg="white",padx= 3,pady=3 )
                lable3.grid(row=0, column=3,sticky= "nsew",padx= 1,pady=1)
                lable3 = Label(c2window, text=nextDay3.strftime('%A'),bg="black",fg="white",padx= 3,pady=3 )
                lable3.grid(row=0, column=4,sticky= "nsew",padx= 1,pady=1)
                lable3 = Label(c2window, text=nextDay4.strftime('%A'),bg="black",fg="white",padx= 3,pady=3 )
                lable3.grid(row=0, column=5,sticky= "nsew",padx= 1,pady=1)
                lable3 = Label(c2window, text=nextDay5.strftime('%A'),bg="black",fg="white",padx= 3,pady=3 )
                lable3.grid(row=0, column=6,sticky= "nsew",padx= 1,pady=1)
                lable3 = Label(c2window, text=nextDay6.strftime('%A'),bg="black",fg="white",padx= 3,pady=3 )
                lable3.grid(row=0, column=7,sticky= "nsew",padx= 1,pady=1)
                lable3 = Label(c2window, text=nextDay7.strftime('%A'),bg="black",fg="white",padx= 3,pady=3 )
                lable3.grid(row=0, column=8,sticky= "nsew",padx= 1,pady=1)
            elif row == 1:#date
                lable2= Label(c2window, text=str(currentDay.month) +"/" + str(currentDay.day))
                lable2.grid(row= 1, column= 1,sticky= "nsew",padx= 1,pady=1)
                lable2= Label(c2window, text=str(nextDay1.month) +"/" + str(nextDay1.day))
                lable2.grid(row= 1, column= 2,sticky= "nsew",padx= 1,pady=1)
                lable2= Label(c2window, text=str(nextDay2.month) +"/" + str(nextDay2.day))
                lable2.grid(row= 1, column= 3,sticky= "nsew",padx= 1,pady=1)
                lable2= Label(c2window, text=str(nextDay3.month) +"/" + str(nextDay3.day))
                lable2.grid(row= 1, column= 4,sticky= "nsew",padx= 1,pady=1)
                lable2= Label(c2window, text=str(nextDay4.month) +"/" + str(nextDay4.day))
                lable2.grid(row= 1, column= 5,sticky= "nsew",padx= 1,pady=1)
                lable2= Label(c2window, text=str(nextDay5.month) +"/" + str(nextDay5.day))
                lable2.grid(row= 1, column= 6,sticky= "nsew",padx= 1,pady=1)
                lable2= Label(c2window,text=str(nextDay6.month) +"/" + str(nextDay6.day))
                lable2.grid(row= 1, column= 7,sticky= "nsew",padx= 1,pady=1)
                lable2= Label(c2window,text=str(nextDay7.month) +"/" + str(nextDay7.day))
                lable2.grid(row= 1, column= 8,sticky= "nsew",padx= 1,pady=1)
                

            elif column==0:
                a+=1
                label= Label(c2window, text=a)
                label.grid (row=row, column =column,sticky= "nsew",padx= 1,pady=1)
            else:
            
                label6 = Menubutton(c2window,text="Available")
                label6.grid(row=row, column= column,sticky= "nsew",padx= 1,pady=1)
                c2window.grid_columnconfigure(column, weight= 1, uniform =1)
                label6.menu= Menu (label6)
                label6["menu"]= label6.menu
                if column==1:
                    label6.menu.add_command (label = "check In",command=lambda roomNumber= a :checkIn(roomNumber))
                else:
                    label6.menu.add_command (label = "Reservation",command=lambda roomNumber= a : reservationSystem())
                # lambda  h = h ,row= row, column=column, l= label : availableRoom(row,column,h,l))
                # label.menu.add_command (label = "Reservation", command=lambda  h= h, row= row, column=column, l= label : occupiedRoom(row,column,h,l))

    def loadCheckin():
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        sql = ' SELECT * FROM Room WHERE CheckIN =  '+str(1)
        cur.execute(sql)
        result = cur.fetchall()
        def loadrooms(row,column,first_name):
            widget= c2window.grid_slaves(row=row, column=column)[0]
            widget.configure(bg="blue",fg="white",text=first_name)

        for row in result:
            if row[2] == 'Unavailable/Occupied':
                cur = conn.cursor()
                # sql = 'SELECT first_name, last_name FROM guests WHERE guest_id=' + str(row[6])
                # sql= 'SELECT CheckInDate , CheckOutDate from Room UNION ALL SELECT  first_name, last_name from guests WHERE guest_id=' +str(row[6])
                sql= 'SELECT RoomNumber,first_name, last_name, CheckInDate, CheckOutDate from guests INNER JOIN Room on Room.guestID = guests.guest_id'
                cur.execute(sql)
                guest = cur.fetchall()

        for row in guest:
            print(row)
            year1, month1, day1 = map(int, row[4].split('/'))
            d= date(year1,month1,day1)
            year, month, day = map(int, row[3].split('/'))
            c=date(year, month, day)
            days=(d-c).days
            cur = conn.cursor()
            # sql = 'SELECT first_name, last_name FROM guests WHERE guest_id=' + str(row[6])
            # sql= 'SELECT CheckInDate , CheckOutDate from Room UNION ALL SELECT  first_name, last_name from guests WHERE guest_id=' +str(row[6])
            sql=  'SELECT RowX, ColumnY FROM RoomAvailability WHERE RoomNumber ='+ row[0]
            cur.execute(sql)
            roomHere = cur.fetchall()
            print(days)
            if days==0:
                loadrooms(roomHere[0][0],roomHere[0][1],row[1])
            elif days==1:
                loadrooms(roomHere[0][0],roomHere[0][1],row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+1,row[1])
                
            elif days==2:
                loadrooms(roomHere[0][0],roomHere[0][1],row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+1,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+2,row[1])
            elif days==3:
                loadrooms(roomHere[0][0],roomHere[0][1],row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+1,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+2,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+3,row[1])
            elif days==4:
                loadrooms(roomHere[0][0],roomHere[0][1],row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+1,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+2,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+3,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+4,row[1])
            elif days==5:
                loadrooms(roomHere[0][0],roomHere[0][1],row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+1,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+2,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+3,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+4,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+5,row[1])
            elif days==6:
                loadrooms(roomHere[0][0],roomHere[0][1],row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+1,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+2,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+3,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+4,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+5,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+6,row[1])
            elif days==7:
                loadrooms(roomHere[0][0],roomHere[0][1],row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+1,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+2,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+3,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+4,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+5,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+6,row[1])
                loadrooms(roomHere[0][0],roomHere[0][1]+7,row[1])
    loadCheckin()      
                       
