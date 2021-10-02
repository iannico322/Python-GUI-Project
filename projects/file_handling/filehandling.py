from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3
import os

#DEVELOPED by:Author Ian Nico M. Caulin
#COURSE : BSIT-1R5

root = Tk()
root.title("Python - Save Data To Table (File Handling)")
root.iconbitmap('images/logo.ico')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 988
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)
root.config(bg='#17161b')
#==================================METHODS============================================

def Database():
    global conn, cursor
    conn = sqlite3.connect('projects/file_handling/Filehandling.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname TEXT, lastname TEXT, gender TEXT, address TEXT, username TEXT, password TEXT)")

def insertData():
    if FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == ""  or ADDRESS.get() == "" or USERNAME.get() == "" or PASSWORD.get() == "":
        txt_result.config(text="Please complete the required field!", fg="red")
    else:
        Database()
        cursor.execute("INSERT INTO `member` (firstname,lastname, gender, address, username, password) VALUES(?, ?, ?, ?, ?,?)", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), str(ADDRESS.get()), str(USERNAME.get()), str(PASSWORD.get())))
        conn.commit()
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        ADDRESS.set("")
        USERNAME.set("")
        PASSWORD.set("")
        txt_result.config(text="Saved a data!", fg="green")
        cursor.close()
        conn.close()
        displayData()

def displayData():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM member ORDER BY firstname ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(
            data[1], data[2], data[3], data[4],data[5],data[6], '******'))
    cursor.close()
    conn.close()


def Exit():
        result = tkMessageBox.askquestion('P A H I M A N G N O !', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            root.withdraw()
            os.system('main.py')
        
#==================================VARIABLES==========================================
titlepic = PhotoImage(file='images/filehandlingtitle.png')
FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
ADDRESS = StringVar()
USERNAME = StringVar()
PASSWORD = StringVar()
#==================================FRAME==============================================
Top = Frame(root)
Top.pack(side=TOP,anchor=W)
Left = Frame(root, width=700, height=500)
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=4,bg='#17161b')
Right.pack(side=RIGHT,padx=(0,0))
Forms = Frame(Right, width=100, height=750,bg='#17161b')
Forms.pack(side=TOP,pady=20)
Buttons = Frame(Right, width=300, height=100,bg='#17161b')
Buttons.pack(side=BOTTOM)
RadioGroup = Frame(Forms)
title = Frame(root)
#==================================LABEL WIDGET=======================================
txt_title = Label(Top,image=titlepic,bg='#050505',borderwidth=0)
txt_title.pack()
txt_firstname = Label(Forms, text="Firstname:",font='arial 14 ',fg='#c4c4c4',bg='#17161b',bd=15)
txt_firstname.grid(row=0, stick="e")

txt_lastname = Label(Forms, text="Lastname:",font='arial 14 ',fg='#c4c4c4',bg='#17161b',bd=15)
txt_lastname.grid(row=1, stick="e")

txt_gender = Label(Forms, text="Gender:",font='arial 14 ',fg='#c4c4c4',bg='#17161b',bd=15)
txt_gender.grid(row=2, stick="e")

txt_address = Label(Forms, text="Address:",font='arial 14 ',fg='#c4c4c4',bg='#17161b',bd=15)
txt_address.grid(row=3, stick="e")

txt_username = Label(Forms, text="Username:",font='arial 14 ',fg='#c4c4c4',bg='#17161b',bd=15)
txt_username.grid(row=4, stick="e")

txt_password = Label(Forms, text="Password:",font='arial 14 ',fg='#c4c4c4',bg='#17161b',bd=15)
txt_password.grid(row=5, stick="e")

txt_result = Label(Buttons,bg='#17161b')
txt_result.pack(side=TOP)
#==================================ENTRY WIDGET=======================================
firstname = Entry(Forms, textvariable=FIRSTNAME, width=28,font='arial 10 ',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN)
firstname.grid(row=0, column=1)

lastname = Entry(Forms, textvariable=LASTNAME, width=28,font='arial 10 ',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN)
lastname.grid(row=1, column=1)

gender1 = Radiobutton(Forms, text='Male', variable=GENDER, value="Male",bg='#17161b',fg='#1df700',selectcolor='#17161b',activebackground='#17161b').grid(row=2,columnspan=2)
gender2 =Radiobutton(Forms, text='Female', variable=GENDER, value="Female",bg='#17161b',fg='#1df700',selectcolor='#17161b',activebackground='#17161b').grid(row=2,column=1,columnspan=2)

address = Entry(Forms, textvariable=ADDRESS, width=30,font='arial 10 ',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN)
address.grid(row=3, column=1)

username = Entry(Forms, textvariable=USERNAME, width=28,font='arial 10 ',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,)
username.grid(row=4, column=1)

password = Entry(Forms, textvariable=PASSWORD, show="*", width=28,font='arial 10 ',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN)
password.grid(row=5, column=1)
#==================================BUTTONS WIDGET=====================================
btn_create = Button(Buttons,cursor='circle', width=10, text="Save",font='arial 10 bold',activebackground='#17161b',fg='#1df700',relief=SUNKEN,activeforeground='#1df700', command=insertData,bg='black',padx=10)
btn_create.pack(side=LEFT,expand=7)

btn_exit = Button(Buttons,cursor='circle',  width=10, text="Exit", command=Exit,bg='black',activebackground='#17161b',fg='#1df700',relief=SUNKEN,activeforeground='#1df700',font='arial 10 bold',padx=10)
btn_exit.pack(side=LEFT)
#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Left, orient=VERTICAL)
scrollbarx = Scrollbar(Left, orient=HORIZONTAL,)
tree = ttk.Treeview(Left, columns=("Firstname", "Lastname","Gender", "Address", "Username", "Password"),
                    selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Firstname', text="Firstname", anchor=W)
tree.heading('Lastname', text="Lastname", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.heading('Username', text="Username", anchor=W)
tree.heading('Password', text="Password", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=150)
tree.column('#5', stretch=NO, minwidth=0, width=120)
tree.column('#6', stretch=NO, minwidth=0, width=80)
tree.pack()
#==================================INITIALIZATION=====================================displayData()
root.mainloop()
