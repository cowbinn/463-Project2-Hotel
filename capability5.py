import io
from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import sqlite3
import base64


def loadFile(win, photo):
    file_path = askopenfilename(filetypes=(('all files', '.*'),
                                           ('text files', '.txt'),
                                           ('image files', '.png'),
                                           ('image files', '.jpg')), parent=win)

    with open(file_path, 'rb') as imageFile:
        imageB64 = base64.b64encode(imageFile.read())

    fh = io.BytesIO(base64.b64decode(imageB64))
    img = Image.open(fh, mode='r')
    img = img.resize((400, 200), Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(img)
    photo.configure(image=photo1, text=imageB64)
    photo.image = photo1
    photo.text = imageB64


def save(guestID, firstName, lastName, phoneNumber, address, emailAddress, idLabel, vehicleLicensePlate, pic, win):
    if len(firstName.get()) == 0 or firstName.get().isspace() or len(lastName.get()) == 0 or lastName.get().isspace() or len(phoneNumber.get()) == 0 or phoneNumber.get().isspace() or len(address.get('1.0', END)) == 0 or address.get('1.0', END).isspace() or len(emailAddress.get()) == 0 or emailAddress.get().isspace() or len(idLabel.get()) == 0 or idLabel.get().isspace() or len(vehicleLicensePlate.get()) == 0 or vehicleLicensePlate.get().isspace():
        error = ''
        if len(firstName.get()) == 0 or firstName.get().isspace():
            error += 'First name is empty\n'
        if len(lastName.get()) == 0 or lastName.get().isspace():
            error += 'Last name is empty\n'
        if len(phoneNumber.get()) == 0 or phoneNumber.get().isspace():
            error += 'Phone number is empty\n'
        if len(address.get()) == 0 or address.get().isspace():
            error += 'Address is empty\n'
        if len(emailAddress.get()) == 0 or emailAddress.get().isspace():
            error += 'Email Address is empty\n'
        if len(idLabel.get()) == 0 or idLabel.get().isspace():
            error += 'ID is empty\n'
        if len(vehicleLicensePlate.get()) == 0 or vehicleLicensePlate.get().isspace():
            error += 'Vehicle license plate is empty\n'
        messagebox.showerror('Missing Information', error, parent=win)
    else:
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        sql = 'UPDATE guests SET first_name = "' + str(firstName.get()) + '", last_name = "' + str(lastName.get()) + '", phone_number = "' + str(phoneNumber.get()) + '", street_address = "' + str(address.get('1.0', END)) + '", email_address = "' + str(emailAddress.get()) + '", id_info = "' + str(idLabel.get()) + '", vehicle_license_plate = "' + str(vehicleLicensePlate.get()) + '", image = "' + pic.text.decode('ascii') + '" WHERE guest_id = ' + str(guestID.get().rsplit(' ', 1)[1])
        cur.execute(sql)
        conn.commit()
        messagebox.showinfo('Data Saved', 'Saved Successfully', parent=win)


def guestInfo(guestID):
    print(guestID)
    if guestID.isspace() or len(guestID) == 0:
        messagebox.showerror('Invalid Guest ID', 'Guest Not Selected')
    else:
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        sql = 'SELECT * FROM guests WHERE guest_id=' + str(guestID.rsplit(' ', 1)[1])
        cur.execute(sql)
        guest = cur.fetchall()
        window = Toplevel()
        window.grab_set()
        width = 800
        height = 730
        window.title('Guest Information')
        window.geometry('800x730')
        window.resizable(False, False)
        background_color = 'light gray'
        label_frame = Frame(window, width=width, height=height, bg=background_color)
        photo = Label(label_frame)
        imageB64 = guest[0][8].encode('ascii')
        fh = io.BytesIO(base64.b64decode(imageB64))
        img = Image.open(fh, mode='r')
        img = img.resize((400, 200), Image.ANTIALIAS)
        photo1 = ImageTk.PhotoImage(img)
        photo.configure(image=photo1)
        photo.image = photo1
        photo.text = imageB64
        photo.place(x=40, y=30)
        browse = Button(label_frame, text='Browse', font=('Arial', 16), command=lambda: loadFile(window, photo))
        browse.place(x=200, y=260)
        first_name_label = Label(label_frame, text='First Name', bg=background_color, font=('Arial', 16))
        first_name_label.place(x=500, y=30)
        first_name_text = Entry(label_frame, font=('Arial', 16))
        first_name_text.place(x=500, y=60)
        first_name_text.insert(0, guest[0][1])
        last_name_label = Label(label_frame, text='First Name', bg=background_color, font=('Arial', 16))
        last_name_label.place(x=500, y=110)
        last_name_text = Entry(label_frame, font=('Arial', 16))
        last_name_text.place(x=500, y=140)
        last_name_text.insert(0, guest[0][2])
        phone_number_label = Label(label_frame, text='Phone Number', bg=background_color, font=('Arial', 16))
        phone_number_label.place(x=500, y=190)
        phone_number_text = Entry(label_frame, font=('Arial', 16))
        phone_number_text.place(x=500, y=220)
        phone_number_text.insert(0, guest[0][3])
        address_label = Label(label_frame, text='Address', bg=background_color, font=('Arial', 16))
        address_label.place(x=500, y=270)
        address_text = Text(label_frame, font=('Arial', 16), height=3, width=20)
        address_text.place(x=500, y=300)
        address_text.insert(INSERT, guest[0][4])
        email_address_label = Label(label_frame, text='Email Address', bg=background_color, font=('Arial', 16))
        email_address_label.place(x=500, y=400)
        email_address_text = Entry(label_frame, font=('Arial', 16))
        email_address_text.place(x=500, y=430)
        email_address_text.insert(0, guest[0][5])
        id_label_label = Label(label_frame, text='ID info', bg=background_color, font=('Arial', 16))
        id_label_label.place(x=500, y=480)
        id_label_text = Entry(label_frame, font=('Arial', 16))
        id_label_text.place(x=500, y=510)
        id_label_text.insert(0, guest[0][6])
        vehicle_license_plate_label = Label(label_frame, text='Vehicle License Plate', bg=background_color,
                                            font=('Arial', 16))
        vehicle_license_plate_label.place(x=500, y=560)
        vehicle_license_plate_text = Entry(label_frame, font=('Arial', 16))
        vehicle_license_plate_text.place(x=500, y=590)
        vehicle_license_plate_text.insert(0, guest[0][7])
        btn = Button(label_frame, text='Save', font=('Arial', 16), command=lambda guest_id=guestID, first_name=first_name_text, last_name=last_name_text, phone_number=phone_number_text, address=address_text, email_address=email_address_text, id_label = id_label_text, vehicle_license_plate=vehicle_license_plate_text, image=photo: save(guest_id, first_name, last_name, phone_number, address, email_address, id_label, vehicle_license_plate, image, window))
        btn.place(x=367, y=650)
        label_frame.place(x=0, y=0)
        window.mainloop()
