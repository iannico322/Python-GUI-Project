from tkinter import *
import sqlite3
import os
from tkinter import messagebox

#DEVELOPED by:Author Ian Nico M. Caulin
#COURSE : BSIT-1R5

root = Tk()
root.title("LOGIN PAGE")
root.iconbitmap('images/logo.ico')
width = 400
height = 235
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
#==============================METHODS========================================


def Database():
    global conn, cursor
    conn = sqlite3.connect("LoginCache.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS dbmembr (mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM dbmembr WHERE username = 'iannico' AND password ='iannico'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO dbmembr (username, password) VALUES('iannico', 'iannico')")
        conn.commit()

def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Butngi pud og input badi!" , fg="#1df700")
    else:
        cursor.execute("SELECT * FROM dbmembr WHERE username = ? AND password = ?",(USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            root.withdraw()
            os.system('main.py')
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Wrong username or password", fg="#1df700")
            USERNAME.set("")
            PASSWORD.set("")
            cursor.close()
            conn.close()

#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()
login = PhotoImage(file='images/login.png')
header = PhotoImage(file='images/loginheader.png')
#==============================FRAMES=========================================
Top = Frame(root, relief=RAISED)
Top.pack(side=TOP, fill=X)
Form = Frame(root)
Form.pack(side=TOP, pady=20)
#==============================LABELS=========================================
lbl_title = Label(Top, image=header,bd=0,fg="orange",bg="black")
lbl_title.pack(fill=X,side=LEFT)
lbl_username = Label(Form, text="Username:",font='arial 14 ',fg='#c4c4c4',bg='#17161b').grid(row=0,column=0, sticky="e",padx=(20,30),pady=(0,20))

lbl_password = Label(Form, text="Password:",font='arial 14 ',fg='#c4c4c4',bg='#17161b').grid(row=1,column=0, sticky="e",padx=(20,30),pady=(0,0))
lbl_text = Label(Form,bg='#17161b')
lbl_text.grid(row=2, columnspan=2,column=1)
#==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME,font='arial 12 bold ',justify=CENTER,fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN)
username.grid(row=0, column=1,pady=(6,20))
password = Entry(Form, textvariable=PASSWORD, show="*",font='arial 12 bold ',justify=CENTER,fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN)
password.grid(row=1, column=1,pady=(6,0))
    
#==============================BUTTON WIDGETS=================================
login_tuplok = Button(Form,image=login,command=Login,borderwidth=0,fg='#050505',bg='#17161b',border=0,activebackground='#17161b',cursor='hand2')
login_tuplok.grid(pady=(0,0),column=1, row=3,padx=(4,0))
login_tuplok.bind(Login)
root.config(bg='#17161b')
Form.config(bg='#17161b')
Top.config(bg='#17161b')
root.mainloop()

