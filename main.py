from tkinter import *
from tkinter import messagebox
import os

#DEVELOPED by:Author Ian Nico M. Caulin
#COURSE : BSIT-1R5

#functions=========================================
def aboutMe():
    root.withdraw()
    os.system('py projects/biodata/biodataWithGui.py')
    
def facebook():
    os.system("start https://www.facebook.com/why.stalking/")

def instagram():
    os.system("start https://www.instagram.com/diakosinico/")

def exit():
    root.withdraw()
    os.system('login.py')


def filehandling():
    root.withdraw()
    os.system('py projects/file_handling/filehandling.py')

def gradesummary():
    root.withdraw()
    os.system('py projects/grade_summary/grade.py')
def payroll():
    root.withdraw()
    os.system('py projects/payroll/payroll.py')

def help():
    os.system("start https://www.facebook.com/messages/t/100004702322887")

def hover(e):
    short_info.config(text='Are you ready to Know me? Click it now!')
def hover_out(e):
    short_info.config(text=' ')    
#/functions=========================================
root = Tk()
root.title('My  Portfolio')
root.iconbitmap('images/logo.ico')
width = 780
height = 489
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(False, False)

#frames=======================================================
bottom = Frame(root, bg='#050505')
bottom.pack(fill=X,side=BOTTOM)
left = Frame(root)
left.pack(side=LEFT)
right = Frame(root)
right.pack(side=RIGHT)

#images variable=====================================================
profile = PhotoImage(file='images/profile.png')
footer = PhotoImage(file='images/footer.png')
button = PhotoImage(file='images/botton.png')

#/menusbar============================================================
menubar = Menu(root,activeborderwidth=20,activeforeground='#1df700')
me = Menu(menubar, tearoff=False,bd=0,activeforeground='#1df700',activebackground='#0f1012')
menubar.add_cascade(label='  Ian Nico     |', menu=me)
me.add_command(label='About Me', command=aboutMe)
me.add_command(label='Facebook', command=facebook)
me.add_command(label='Instagram', command=instagram)
me.add_separator()
me.add_command(label='Exit', command=exit)

file_h = Menu(menubar, tearoff=0,bd=0,foreground='#1df700',background='#0f1012',activeforeground='white',activebackground='#0f1012',cursor='circle')
file_h.add_command(label='This project allows the user to save', command=filehandling)
file_h.add_command(label=' information to the database table', command=filehandling)

GSS = Menu(menubar,borderwidth=0, tearoff=0,bd=0,foreground='#1df700',background='#0f1012',activeforeground='white',activebackground='#0f1012',cursor='circle')
GSS.add_command(label='This project can calculate and record ', command=gradesummary)
GSS.add_command(label='all information to the database table', command=gradesummary)

PS = Menu(menubar, tearoff=0,bd=0,foreground='#1df700',background='#0f1012',activeforeground='white',activebackground='#0f1012',cursor='circle')
PS.add_command(label='This project can calculate,save,delete and update',command=payroll)
PS.add_command(label='information in the Database table',command=payroll)

edit = Menu(menubar, tearoff=0,bd=0,activeforeground='#1df700',activebackground='#0f1012')
menubar.add_cascade(label='Projects     |', menu=edit)
num1= edit.add_cascade(label='File Handling', menu=file_h, command=filehandling)
num2= edit.add_cascade(label='Grade Summary System', menu=GSS, command=gradesummary)
edit.add_cascade(label='Payroll System', menu=PS,command=payroll)
edit.add_separator()

help_ = Menu(menubar, tearoff=0,bd=0,activeforeground='#1df700',activebackground='#0f1012')
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='For assignment', command=help)
help_.add_command(label='For Projects', command=help)
help_.add_command(label='For Activities', command=help)
help_.add_separator()
#menusbar/============================================================

prof =Label(left,image=profile,bg='#17161b')
prof.grid(row=0, column=0, padx=(0, 0))

name=Entry(root,fg='#5e5f5e',bg='#17161b',font=('Century Gothic',32),bd=0)
name.insert(END, 'Ian Nico M. Caulin ')
name.place(x=352,y=169)

short_info = Label(root,text=' ',bg='#17161b',fg='#1df700',font='arial 8')
short_info.place(x=442,y=348)



hi=Entry(root,fg='#ffa500',bg='#17161b',font='Arial 25',bd=0)
hi.insert(END, 'Hi I’m')
hi.place(x=352,y=138)

description=Entry(root,fg='#545555',bg='#17161b',font=('Segoe UI Emoji',13),bd=0,width=40)
description.insert(END, 'A  S O F T W A R E  E N G I N E E R')
description.place(x=357,y=219)

btn = Button(root,image=button,borderwidth=0,bg='#17161b',command=aboutMe,activebackground='#17161b',cursor= 'hand2')
btn.place(x=457,y=279)

btn.bind('<Enter>',hover)
btn.bind('<Leave>',hover_out)
Label(bottom, image=footer, bg='#050505',bd=0).grid(row='0', column='0', columnspan=3, pady=(0,0))


root.config(bg='#17161b')
left.config(bg='#17161b')
right.config(bg='#17161b')
root.config(menu=menubar)

root.mainloop()

