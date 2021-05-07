from tkinter import  Label, Menubutton, Tk
from tkinter import *
import array
import tkinter.messagebox
import sqlite3
from tkinter import messagebox
from capability6 import room




def roomType():
    root= Tk()
    root.title("Key")
    root.geometry("375x150+850+50")
    window = Toplevel()
    window.title("Room Type")
    window.geometry("800x200+0+50")
    h=99#set room to start at 99 then add 1 to make 100 initial starting room
    def closeWindow(roomNumber,l):
        window.destroy()
        room(roomNumber,l)
        root.destroy()
    def makeAvailable(roomNumber):
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        sql = 'UPDATE Room SET RoomStatus = "Available" WHERE roomNumber = ' + str(roomNumber)
        cur.execute(sql)
        conn.commit()
    def makeUnavailable(roomNumber):
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        sql = 'UPDATE Room SET RoomStatus = "Unavailable/Occupied" WHERE roomNumber = ' + str(roomNumber)
        cur.execute(sql)
        conn.commit()
    def makeRoomDirty(roomNumber):
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        sql = 'UPDATE Room SET RoomStatus = "Unavailable/Dirty" WHERE roomNumber = ' + str(roomNumber)
        cur.execute(sql)
        conn.commit()
    def makeRoomMaintance(roomNumber):
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        sql = 'UPDATE Room SET RoomStatus = "Unavailable/Maintenance" WHERE roomNumber = ' + str(roomNumber)
        cur.execute(sql)
        conn.commit()
    #function to change color depends on status of the room
    def loadDirtyRoom(row,column):
        widget= window.grid_slaves(row=row, column=column)[0]
        widget.configure(bg="pink",fg="black")
    def loadOccupiedRoom(row,column):
        widget= window.grid_slaves(row=row, column=column)[0]
        widget.configure(bg="blue",fg="black")
    def loadMaintenanceRoom(row,column):
        widget= window.grid_slaves(row=row, column=column)[0]
        widget.configure(bg="red",fg="white")
    def loadAvailableRoom(row,column):
        widget= window.grid_slaves(row=row, column=column)[0]
        widget.configure(bg="green")
    def availableRoom(row,column,h,l):
        # print(label.grid_info())
        makeAvailable(h)
        # widget= window.grid_slaves(row=row, column=column)[0]
        # widget.configure(bg="green")
        l.configure(bg="green")
    def dirtyRoom(row,column,h,l):
        #print(label.grid_info())
        # makeRoomDirty(h)
        # loadDirtyRoom(row,column)
        # # widget= window.grid_slaves(row=row, column=column)[0]
        # # widget.configure(bg="pink",fg="black")
        # l.configure(bg="pink",fg="black")
        MsgBox = messagebox.askquestion('Make room available ?','Make room available?')
        if MsgBox =='yes':
            availableRoom(row,column,h,l)
        else:
            pass

    def occupiedRoom(row,column,h,l):
        #print(label.grid_info())
        room(h,l)
        l.config (bg = 'blue', fg='black')
        # widget= window.grid_slaves(row=row, column=column)[0]
        # widget.configure(bg="blue",fg="black")
    
    def maintenanceRoom(row,column,h,l):
        #print(label.grid_info())
        # l.config(bg="red", fg="white")
        # makeRoomMaintance(h)
        # widget= window.grid_slaves(row=row, column=column)[0]
        # widget.configure(bg="red",fg="white")
        conn = sqlite3.connect('hotel.db')
        sql5 = 'SELECT * FROM Room WHERE RoomNumber='+str(h)
        cur = conn.cursor()
        cur.execute(sql5)
        print (h)
        result = cur.fetchall()
        print(result)
        for row in result:
            if (row[2] == "Available"):
                MsgBox = messagebox.askquestion('Room Maintanance?','Room Need Maintenance?')
                if MsgBox =='yes':
                    l.config(bg="red", fg="white")
                    makeRoomMaintance(h)
                else:
                    pass
            if (row[2] == "Unavailable/Maintenance"):
                MsgBox = messagebox.askquestion('Room Maintanance?','Make room Available?')
                if MsgBox =='yes':
                    availableRoom(row,column,h,l)
                else:
                    pass
            

    for row in range (10):#populate room and room types


        for column in range (6):
            
            if row == 0 :
                lable1 = Label(window,text="Room Number",bg="black",fg="white",padx= 3,pady=3)
                lable1.grid(row=0,column=1,sticky= "nsew",padx= 1,pady=1,columnspan=8)    
            elif row == 0 and column==0:
                lable0= Label(window,text="")
                lable0.grid(row=0, column=0,sticky= "nsew",padx= 1,pady=1)

            elif column == 0 and row ==1:
                lable2=Label(window,text="King Size bed",bg="black",fg="white",padx= 3,pady=3)
                lable2.grid(row=1, column=0,sticky= "nsew",padx= 1,pady=1)
            elif column == 0 and row ==2:
                lable3=Label(window,text="Double Queen Bed",bg="black",fg="white",padx= 3,pady=3)
                lable3.grid(row=2, column=0,sticky= "nsew",padx= 1,pady=1)
            elif row ==3 and column==0:
                lable4=Label(window,text="Double Queen Bed With Kitchen",bg="black",fg="white",padx= 3,pady=3)
                lable4.grid(row=3, column =0,sticky= "nsew",padx= 1,pady=1)
            elif row ==4 and column==0:
                lable5=Label(window,text="Suite",bg="black",fg="white",padx= 3,pady=3)
                lable5.grid(row=4, column =0,sticky= "nsew",padx= 1,pady=1)
            elif row == 5 :
                label6= Label(text= "Key", bg="Gray", fg="white",padx=3,pady=3,font="24")
                label6.grid(row=5, column= 1,sticky= "nsew",padx= 1,pady=1, columnspan= 6)
            elif row== 6 :
                labelG= Label(text= "Maintenance", bg="red", fg="white")
                labelG.grid(row=6, column= 5,sticky= "nsew",padx= 0,pady=1,columnspan=1)
                labelG= Label(text= "Available", bg="green", fg="white")
                labelG.grid(row=6, column= 2,sticky= "nsew",padx= 0,pady=1,columnspan=1)
                labelG= Label(text= "Occupied", bg="blue", fg="white")
                labelG.grid(row=6, column= 3,sticky= "nsew",padx= 0,pady=1,columnspan=1)
                labelG= Label(text= "Dirty", bg="pink", fg="black")
                labelG.grid(row=6, column= 4,sticky= "nsew",padx= 0,pady=1,columnspan=1)
            elif row==7:
                labelh= Label(text= "To check out please select occupied again",font="18",bg= "grey",fg="white")
                labelh.grid(row=7,column =2, columnspan =4)
            elif row==8:
                labelh= Label(text= "To Make room Available click on the coressponding Status",font="18",bg= "grey",fg="white")
                labelh.grid(row=8,column =2, columnspan =4)
            elif row==9:
                labelh= Label(text= "To exit please close the Key window",font="18",bg= "grey",fg="white")
                labelh.grid(row=9,column =2, columnspan =4)

                
            
            
            else:  
                h+=1  #using Menu Button to let user select status of the room
                label = Menubutton(window, text=h,bg="green",fg="white",padx= 1,pady=1)
                label.grid(row=row, column= column,sticky= "nsew",padx= 1,pady=1)
                window.grid_columnconfigure(column, weight= 1, uniform =1)
                label.menu= Menu (label)
                label["menu"]= label.menu
                label.menu.add_command (label = "available",command=lambda  h = h ,row= row, column=column, l= label : availableRoom(row,column,h,l))
                label.menu.add_command (label = "occupied", command=lambda  h= h, row= row, column=column, l= label : occupiedRoom(row,column,h,l))
                label.menu.add_command (label = "dirty", command=lambda h=h, row= row, column=column, l= label: dirtyRoom(row,column,h,l))
                label.menu.add_command (label = "maintenance", command=lambda  h=h,row= row, column=column, l= label: maintenanceRoom(row,column,h,l))

    def reloadWindow():          
        conn = sqlite3.connect('hotel.db')
        sql5 = 'SELECT * FROM Room'
        cur = conn.cursor()
        cur.execute(sql5)
        result = cur.fetchall()


        for row in result:
            print(row)
            if (row[2]== "Unavailable/Occupied"):
                sql2 = 'SELECT RowX, ColumnY FROM RoomType WHERE RoomNumber =' +row[0]
                cur.execute(sql2)
                roomResult = cur.fetchall()
                for temp in roomResult:
                    loadOccupiedRoom(temp[0],temp[1])
            if (row[2]== "Unavailable/Dirty"):
                sql3 = 'SELECT RowX, ColumnY FROM RoomType WHERE RoomNumber =' +row[0]
                cur.execute(sql3)
                roomResult1 = cur.fetchall()
                for temp in roomResult1:
                    loadDirtyRoom(temp[0],temp[1])
            if (row[2]== "Unavailable/Maintenance"):
                sql4 = 'SELECT RowX, ColumnY FROM RoomType WHERE RoomNumber =' +row[0]
                cur.execute(sql4)
                roomResult2 = cur.fetchall()
                for temp in roomResult2:
                    loadMaintenanceRoom(temp[0],temp[1])
            if (row[2]== "Available"):
                sql4 = 'SELECT RowX, ColumnY FROM RoomType WHERE RoomNumber =' +row[0]
                cur.execute(sql4)
                roomResult2 = cur.fetchall()
                for temp in roomResult2:
                    loadAvailableRoom(temp[0],temp[1])
    reloadWindow()
    window.mainloop()
roomType()