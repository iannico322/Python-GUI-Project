from tkinter import*
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import os
import sqlite3

root = Tk()
root.title("Simple Student Grading Summary Reports")
root.iconbitmap('images/logo.ico')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1488
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(False, False)
root.config(bg='#17161b')

#styling for combo box=============================
style = ttk.Style()
style.theme_create('combostyle', parent='alt',
                   settings={'TCombobox':
                             {'configure':
                              {'selectbackground': '#0f1012',
                               'fieldforebackground': '#1df700',
                               'fieldbackground': '#0f1012',
                               'foreground': '#1df700',
                               'background': '#0f1012',
                               'bd': 1,
                               'relief': SUNKEN,
                               'width': 10,
                               }}}
                   )
style.theme_use('combostyle')

def Database():
    global conn, cursor
    conn = sqlite3.connect('projects/grade_summary/Gradesummary.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `student` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,studentNo TEXT,studentN TEXT, course TEXT, subject TEXT, prelimG TEXT, midtermG TEXT,finalG TEXT,average TEXT,remarks TEXT,GPE TEXT)")


def result():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title('Result')
    frame = Frame(Home)
    Home.resizable(False, False)
    Top = Frame(Home, bd=2, relief=RAISED, bg='#050505')
    Home.iconbitmap('images/logo.ico')
    Top.pack(fill=X)
    Bottom = Frame(Home, bd=2, bg='black')
    Bottom.pack(fill=X, side=BOTTOM)
    frame = Frame(Home)

    width = 490
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(True, False)

    Home.configure(bg="#17161b")
    frame.configure(bg="#17161b")

    #variables=============================

    name = student_name.get()
    course = student_course.get()
    subject = student_subject.get()
    prelim =int( student_prelim_grade.get())
    midterm = int(student_midterm_grade.get())
    finals = int(student_finals_grade.get())
    global average
    average = (prelim + midterm + finals)/3

    #REMARKS===============================
    global remarks
    if average >= 95 and average <= 100:
        remarks = 'Excellent'
    elif average >= 91 and average <= 94.99:
        remarks = 'Superior'
    elif average >= 88 and average <= 90.99:
        remarks = 'Very Good'
    elif average >= 86 and average <= 87.99:
        remarks = 'Good'
    elif average >= 84 and average <= 85.99:
        remarks = 'Very Satisfactory'
    elif average >= 82 and average <= 83.99:
        remarks = 'High Average'
    elif average >= 79 and average <= 81.99:
        remarks = 'Average'
    elif average >= 77 and average <= 78.99:
        remarks = 'Fair'
    elif average >= 75 and average <= 76.99:
        remarks = 'Pass'
    elif average >= 58 and average <= 74.99:
        remarks = 'Conditional if Pass/Failed'
    elif average > 0 and average < 58.49:
        remarks = 'Failing Final Grade'
    else:
        remarks = 'none'

    #GPE===================================
    global GPE1
    def GPE(rem):
        switcher = {
            'Excellent': 1.0,
            'Superior': 1.25,
            'Very Good': 1.50,
            'Good': 1.75,
            'Very Satisfactory': 2.00,
            'High Average': 2.25,
            'Average': 2.50,
            'Fair': 2.75,
            'Pass': 3.00,
            'Conditional if Pass/Failed': 4.00,
            'Failing Final Grade': 5.00,
            'none':00,
        }
        return switcher.get(rem)

    GPE1 = GPE(remarks)
    #change-color for remarks======================================
    result_color = '#1df700'
    if remarks =='Conditional if Pass/Failed' or remarks == 'Failing Final Grade':  
        result_color = 'red'
    
        

    Label(Top, text=f"        Hi {name}, from {course}.",
          font='ArialNarrow 20 bold', fg='gray', bg='#050505').grid(row='0', column='1', padx=(0, 20))
    Label(Top, text=f"      This is your Average,Remarks and GPE in ",
          font='ArialNarrow 16 bold', fg='#ffa500', bg='#050505').grid(row='1', column='1', padx=(0, 20))
    Label(Top, text=f"      {subject}",
          font='ArialNarrow 20 bold', fg='#1df700', bg='#050505').grid(row='2', column='1', padx=(0, 20))

    #Average=======================================================
    Label(frame, text="      Average: ", font='arial 15 bold',
          fg='#c4c4c4', bg='#17161b').grid(row='3', column='0', pady=(50, 10))
    Label(frame, text=average, font='arial 15 bold', fg=result_color,
          bg='#0f1012', bd=1, relief=SUNKEN, width=22).grid(row='3', column='1', pady=(50, 10))

    #Remarks=======================================================
    Label(frame, text="      Remarks: ", font='arial 15 bold',
          fg='#c4c4c4', bg='#17161b').grid(row='4', column='0', pady=(0, 10))
    Label(frame, text=remarks, font='arial 15 bold', fg=result_color, bg='#0f1012',
          bd=1, relief=SUNKEN, width=22).grid(row='4', column='1', pady=(0, 10))

    #GPE=======================================================
    Label(frame, text="            GPE : ", font='arial 15 bold',
          fg='#c4c4c4', bg='#17161b').grid(row='5', column='0', pady=(0, 10))

    Label(frame, text=GPE1, font='arial 15 bold', fg=result_color, bg='#0f1012',
          bd=1, relief=SUNKEN, width=22).grid(row='5', column='1', pady=(0, 10))

    #BUTTONS===================================================
    Button(frame, text="Save Info", font='ArialNarrow 10 bold', fg='black',
           bg='orange', command=insertData, borderwidth=0,height=2,width=20).grid(row='6', column='1', pady=(10, 10))

    Button(Bottom, text="Back", font='ArialNarrow 20 bold', fg='#ffa500',
           bg='#050505', command=back).grid(row='20', column='0', padx=(0, 10))

    frame.pack()
    

#Database==============================
def insertData():
    Database()
    cursor.execute("INSERT INTO `student` (studentNo ,studentN, course, subject, prelimG, midtermG,finalG,average,remarks,GPE) VALUES(?, ?, ?, ?, ?,?, ?,?,?,?)", (str(studentNo.get()), str(studentN.get()), str(course.get()), str(subject.get()), str(prelimG.get()), str(midtermG.get()), str(finalG.get()), str(average),str(remarks), str(GPE1)))
    conn.commit()
    cursor.close()
    conn.close()
    displayData()


def displayData():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `student` ORDER BY `studentNo` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(
            data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10]))
    cursor.close()
    conn.close()

#Variables==========================

title = PhotoImage(file='images/gradesummarytitle.png')
student_num = StringVar()
student_name = StringVar()
student_course = StringVar()
student_subject = StringVar()

student_prelim_grade = StringVar()
student_midterm_grade = StringVar()
student_finals_grade = StringVar()


#  Functions for buttons================
def check():
    if student_num.get()=='' or student_name.get()=='' or student_course.get()=='' or student_subject.get() =='' or student_prelim_grade.get() =='' or student_midterm_grade.get() =='' or student_finals_grade.get() =='' :
        log_message.config(text="Invalid Process", fg="#ff1100")
        log_message.grid(row='15', column='0',columnspan=2,padx=(50,0),pady=(20,0))
        tkMessageBox.showerror ('Invalid Process','Action require\'s Filled entries', icon="warning")   
    else:
        log_message.config(text="Submit Successfully", fg="#1df700")
        log_message.grid(row='15', column='0',columnspan=2,padx=(50,0),pady=(20,0))
        result()

def back():
    Home.withdraw()
    root.deiconify()

def Exit():
        result = tkMessageBox.askquestion('P A H I M A N G N O !', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            root.withdraw()
            os.system('main.py')          

#frames-------------------------------------
Left = Frame(root, width=600, height=500, bd=8,bg='orange')
Left.pack(side=LEFT)
Top = Frame(root, bg='#050505')
Top.pack(fill=X)
frame = Frame(root)
Left.pack(side=RIGHT)
frame.pack(side=LEFT)
frame.config(bg='#17161b')


#MainWindow===============================================

#TITLe============================================================
Label(Top,image=title,borderwidth=0, bg='#050505').grid(row=0, column=0,pady=0)

#Student No=======================================================
Label(frame, text="          Student No:", font='arial 12 bold',
      fg='#c4c4c4', bg='#17161b').grid(row=1, column=0, pady=(0, 10))

studentNo = Entry(frame, font='arial 12 bold', fg='#1df700',
                 bg='#0f1012', width=16, textvariable=student_num)
studentNo.grid(row='1', column='1', pady=(0, 10))

#Student Name=====================================================
Label(frame, text="        Student Name:   ", font='arial 12 bold',
      fg='#c4c4c4', bg='#17161b').grid(row='2', column='0', pady=(0, 10))

studentN = Entry(frame, font='arial 12 bold', fg='#1df700',
                 bg='#0f1012', width=16, textvariable=student_name)
studentN.grid(row='2', column='1', pady=(0, 10))

#Course===========================================================
Label(frame, text="                     Course:   ", font='arial 12 bold',
      fg='#c4c4c4', bg='#17161b').grid(row='3', column='0', pady=(0, 10))

course = ttk.Combobox(frame, values=['BSIT', 'BSCE', 'BSA'], font='arial 13 bold', width=14, textvariable=student_course)

course['state'] = 'readonly'
course.grid(row='3', column='1', pady=(0, 10))

#Subject===========================================================
Label(frame, text="                   Subject :   ", font='arial 12 bold',
      fg='#c4c4c4', bg='#17161b').grid(row='4', column='0', pady=(0, 10))

subject = Entry(frame, font='arial 12 bold', fg='#1df700',
                bg='#0f1012', width=16, textvariable=student_subject)
subject.grid(row='4', column='1', pady=(0, 10))

#Prelim Grade=======================================================
Label(frame, text="         Prelim Grade :   ", font='arial 12 bold',
      fg='#c4c4c4', bg='#17161b').grid(row='5', column='0', pady=(0, 10))

prelimG = Entry(frame, font='arial 12 bold', fg='#1df700',
                bg='#0f1012', width=16, textvariable=student_prelim_grade)
prelimG.grid(row='5', column='1', pady=(0, 10))

#Midterm Grade======================================================
Label(frame, text="       Midterm Grade :    ", font='arial 12 bold',
      fg='#c4c4c4', bg='#17161b').grid(row='6', column='0', pady=(0, 10))

midtermG = Entry(frame, font='arial 12 bold', fg='#1df700',
                 bg='#0f1012', width=16, textvariable=student_midterm_grade)
midtermG .grid(row='6', column='1', pady=(0, 10))

#Final Grade========================================================
Label(frame, text="         Final Grade : ", font='arial 12 bold',
      fg='#c4c4c4', bg='#17161b').grid(row='7', column='0', pady=(0, 10))

finalG = Entry(frame, font='arial 12 bold', fg='#1df700',
               bg='#0f1012', width=16, textvariable=student_finals_grade)
finalG.grid(row='7', column='1', pady=(0, 10))

#buttons============================================================

Button(frame, text='Submit', bg="orange", command=check, borderwidth=0,activebackground='black',activeforeground='#1df700',
       font='arial 12 bold', width=12, height=2).grid(row=8, column=1, columnspan=1, pady=(10, 0))

Button(frame, text='Exit', command=Exit, font='ArialNarrow 10 bold', fg='#ffa500', bg='#050505',activebackground='#17161b',activeforeground='#1df700',
       width=10, height=2).grid(row=8, column=0, columnspan=2, pady=(12, 0), padx=(0, 89))
#Error message================================================================
log_message = Label(frame,text='', font='arial 10 ',
      fg='#c4c4c4', bg='#17161b')
log_message.grid(row='15', column='0',columnspan=2,padx=(50,0),pady=(20,0))

#data table===================================================================

scrollbary = Scrollbar(Left, orient=VERTICAL)
scrollbarx = Scrollbar(Left, orient=HORIZONTAL)
scrollbarx.config(bg='red')
tree = ttk.Treeview(Left, columns=("Student ID", "Student Name", "Course", "Subject",
                                    "Prelim", "Midterm", "Final", "Average", "REMARKS", "GPE"),
                    selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)   
scrollbarx.pack(side=BOTTOM, fill=X)

tree.heading('Student ID', text="Student ID", anchor=W)
tree.heading('Student Name', text="Student Name", anchor=W)
tree.heading('Course', text="Course", anchor=W)
tree.heading('Subject', text="Subject", anchor=W)
tree.heading('Prelim', text="Prelim", anchor=W)
tree.heading('Midterm', text="Midterm", anchor=W)
tree.heading('Final', text="Final", anchor=W)
tree.heading('Average', text="Average", anchor=W)
tree.heading('REMARKS', text="REMARKS", anchor=W)
tree.heading('GPE', text="GPE", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=140)
tree.column('#2', stretch=NO, minwidth=0, width=180)
tree.column('#3', stretch=NO, minwidth=0, width=90)
tree.column('#4', stretch=NO, minwidth=0, width=100)
tree.column('#5', stretch=NO, minwidth=0, width=90)
tree.column('#6', stretch=NO, minwidth=0, width=90)
tree.column('#7', stretch=NO, minwidth=0, width=90)
tree.column('#8', stretch=NO, minwidth=0, width=90)
tree.column('#9', stretch=NO, minwidth=0, width=170)
tree.column('#10', stretch=NO, minwidth=0, width=60)
tree.pack()

root.mainloop()
