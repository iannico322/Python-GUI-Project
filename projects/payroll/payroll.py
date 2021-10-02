from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import os
import tkinter.messagebox as tkMessageBox

#DEVELOPED by: Ian Nico M. Caulin
#COURSE : BSIT-1R5

root = Tk()
root.title("Payroll Summary Report")
root.iconbitmap('images/logo.ico')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1501
height = 600
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(False, False)

#program functions==============================
#Database=======================================
def Database():
      global conn, cursor
      conn = sqlite3.connect('projects/payroll/Payroll.db')
      cursor = conn.cursor()
      cursor.execute("CREATE TABLE IF NOT EXISTS 'Employee' (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, empno INTEGER,empname INTEGER, rpd INTEGER,empnow INTEGER,empgp INTEGER,ssscon INTEGER,philhealth INTEGER,cpera INTEGER ,TotalDeductions INTEGER,NetPay INTEGER)")
#===============================================

def calculate():
      if emp_No.get()=='' or emp_N =='' or rpd.get() == '' or no_work_d.get() == '' or SSS.get() =='' or PHIL_HEALTH.get() == '' or CPA.get() == '':
            log_message.configure(text="Please fill all the Filled",fg="#ff1100")
            log_message.grid(row='15', column='0', pady=(0, 0),columnspan=2,padx=(50,0))
      else:
            global GP
            global TD
            global NP,np,td,g2
                        
            g2 = float(rpd.get()) * float(no_work_d.get())
            g2 = round(g2,3)
            GP.set(g2)

            td = (float(SSS.get()) + float(PHIL_HEALTH.get()) + float(CPA.get()))
            TD.set(td)

            np = g2 - td
            np = round(np,3)
            NP.set(np)
            

            log_message.configure(text="Successfully Calculated", fg="#1df700")
            log_message.grid(row='15', column='0', pady=(0,0),columnspan=2,padx=(50,0))
               
            
def saveInfo():
    if TD.get()=='' or GP.get() =='' or NP.get() == ''or emp_No.get()=='' or emp_N =='' or rpd.get() == '' or no_work_d.get() == '' or SSS.get() =='' or PHIL_HEALTH.get() == '' or CPA.get() == '' :
            log_message.configure(text="Please Calculate First", fg="#ff1100")
            log_message.grid(row='15', column='0', pady=(0, 0),columnspan=2,padx=(50,0))
            tkMessageBox.showerror ('Invalid Process','Action require\'s to calculate', icon="warning")
    else:
         result = tkMessageBox.askquestion('P A H I M A N G N O !','Are you sure you want to add this Information?', icon="warning")
         if result =='yes':
            Database()
            cursor.execute("INSERT INTO Employee (empno,empname, rpd,empnow,empgp,ssscon,philhealth,cpera ,TotalDeductions,NetPay) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(str(EMP_NUM.get()),str(EMP_NAME.get()),str(RPD.get()),str(WORK_DAY.get()),str(GP.get()), str(SSS.get()),str(PHIL_HEALTH.get()),str(CPA.get()),str(TD.get()), str(NP.get())))
            tree.delete(*tree.get_children())
            cursor.execute("SELECT * FROM Employee ORDER BY `empname` ")
            fetch = cursor.fetchall()
            for data in fetch:
              tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7],data[8], data[9], data[10]))
            conn.commit()
            log_message.configure(text="Successfully Saved", fg="#1df700")
            log_message.grid(row='15', column='0', pady=(0,0),columnspan=2,padx=(50,0))    
            EMP_NUM.set("")
            EMP_NAME.set("")
            RPD.set("")
            WORK_DAY.set("")
            GP.set("")
            SSS.set("")
            PHIL_HEALTH.set("")
            CPA.set("")
            TD.set("")
            NP.set("")

def OnSelected(event):
      
      global mem_id
      curItem = tree.focus()
      contents =(tree.item(curItem))
      selecteditem = contents['values']
      mem_id = selecteditem[0]
      log_message.config(text=f"ID {mem_id} is Selected ",fg="#1df700")
      EMP_NUM.set(selecteditem[1])
      EMP_NAME.set(selecteditem[2])
      RPD.set(selecteditem[3]) 
      WORK_DAY.set(selecteditem[4])
      GP.set(selecteditem[5])
      SSS.set(selecteditem[6])
      PHIL_HEALTH.set(selecteditem[7])
      CPA.set(selecteditem[8])
      TD.set(selecteditem[9])
      NP.set(selecteditem[10])
      
def delete():
      if tree.selection():
            if EMP_NUM.get()=='' or EMP_NAME =='' or RPD.get() == '' or WORK_DAY.get() == '' or SSS.get() =='' or PHIL_HEALTH.get() == '' or CPA.get() == '':
                  log_message.config(text="Invalid Process", fg="#ff1100")
                  log_message.grid(row='15', column='0', pady=(0,0),columnspan=2,padx=(50,0))
                  tkMessageBox.showerror ('Invalid Process','Action require\'s Filled entries, Kindly click again the DataTable to proceed', icon="warning")   
            else:
                  result = tkMessageBox.askquestion('P A H I M A N G N O !','Are you sure you want to Delete this?', icon="warning")
                  if result == 'yes':
                        curItem = tree.focus()
                        contents = (tree.item(curItem))
                        selecteditem = contents['values']
                        tree.delete(curItem)
                        Database()
                        cursor.execute("DELETE FROM `Employee` WHERE `mem_id` = %d" % selecteditem[0])
                        conn.commit()
                        cursor.close()
                        conn.close()
                        EMP_NUM.set("")
                        EMP_NAME.set("")
                        RPD.set("")
                        WORK_DAY.set("")
                        GP.set("")
                        SSS.set("")
                        PHIL_HEALTH.set("")
                        CPA.set("")
                        TD.set("")
                        NP.set("")
                        log_message.config(text="Successfully deleted the data", fg="#1df700")
      else:
            log_message.config(text="Invalid Process", fg="#ff1100")
            log_message.grid(row='15', column='0', pady=(0,0),columnspan=2,padx=(50,0))
            tkMessageBox.showerror ('Invalid Process ','Action require\'s selecting of DataTable', icon="warning")    
         

def update():
      if tree.selection():
            if EMP_NUM.get()=='' or EMP_NAME =='' or RPD.get() == '' or WORK_DAY.get() == '' or SSS.get() =='' or PHIL_HEALTH.get() == '' or CPA.get() == '':
                  
                  log_message.config(text="Invalid Process", fg="#ff1100")
                  log_message.grid(row='15', column='0', pady=(0,0),columnspan=2,padx=(50,0))
                  tkMessageBox.showerror ('Invalid Process ','Action require\'s Filled all entries', icon="warning")    
            
            else:
                  result = tkMessageBox.askquestion('P A H I M A N G N O !',
                  'Are you sure you to change this field?', icon="warning")
                  if result == 'yes':
                        Database()
                        tree.delete(*tree.get_children())
                        cursor.execute("UPDATE 'Employee' SET empno = ?, empname = ?, rpd =?,empnow = ?, empgp = ?, ssscon = ?,  philhealth = ?, cpera = ?, TotalDeductions = ?, NetPay = ? WHERE mem_id = ?",(str(emp_No.get()), str(emp_N.get()), str(rpd.get()), str(no_work_d.get()), str(g2), str(sssc.get()), str(ph.get()), str(cpa.get()), str(td), str(np),int(mem_id)))
                        conn.commit()
                        cursor.execute("SELECT * FROM 'Employee' ORDER BY empname ASC")
                        fetch = cursor.fetchall()
                        for data in fetch:
                              tree.insert('', 'end', values=(data))
                        cursor.close()
                        conn.close()
                        EMP_NUM.set("")
                        EMP_NAME.set("")
                        RPD.set("")
                        WORK_DAY.set("")
                        GP.set("")
                        SSS.set("")
                        PHIL_HEALTH.set("")
                        CPA.set("")
                        TD.set("")
                        NP.set("")
                        log_message.config(text="Successfully updated the data",fg="#1df700")
      else:
            log_message.config(text="Invalid Process", fg="#ff1100")
            log_message.grid(row='15', column='0', pady=(0,0),columnspan=2,padx=(50,0))
            tkMessageBox.showerror ('Invalid Process ','Action require\'s selecting of DataTable', icon="warning")    
def Exit():
        result = tkMessageBox.askquestion('P A H I M A N G N O !', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            root.withdraw()
            os.system('main.py')          




#Variables=====================================================
header = PhotoImage(file='images/header2.png')

EMP_NUM = StringVar()
EMP_NAME = StringVar()
RPD = StringVar()
WORK_DAY = StringVar()

GP =StringVar()

SSS = StringVar()
PHIL_HEALTH = StringVar()
CPA = StringVar()

TD = StringVar()
NP = StringVar()


#frames==========================================================
Right = Frame(root, width=600, height=500, bd=8, bg='orange')
Top = Frame(root, relief=RAISED, bg='#050505')
Top.pack(fill=X)
frame = Frame(root)
Right.pack(side=RIGHT)
frame.pack(side=LEFT)
root.config(bg='#17161b')
frame.config(bg='#17161b')

#MainWindow========================================================

#TITLe=============================================================
Label(Top, image=header, fg='#ffa500', bg='#050505',bd=0).grid(row=0, column=0, padx=(0, 0))

#Employees No.======================================================
Label(frame, text="          Employee’s No :", font='arial 11 bold',
      fg='#c4c4c4', bg='#17161b').grid(row=1, column=0, pady=(0, 10))

emp_No = Entry(frame, font='arial 12 bold', fg='#1df700',
               bg='#0f1012', width=16, textvariable=EMP_NUM)
emp_No.grid(row='1', column='1', pady=(0, 10))

#Employees Name=====================================================
Label(frame, text="        Employee’s Name :   ", font='arial 11 bold',
      fg='#c4c4c4', bg='#17161b').grid(row='2', column='0', pady=(0, 10))
emp_N = Entry(frame, font='arial 12 bold', fg='#1df700',
              bg='#0f1012', width=16, textvariable=EMP_NAME)
emp_N.grid(row='2', column='1', pady=(0, 10))


#Rate/Day============================================================
Label(frame, text="                    Rate/Day :", font='arial 11 bold',
      fg='#c4c4c4', bg='#17161b').grid(row='4', column='0', pady=(0, 10))

rpd = Entry(frame, font='arial 12 bold', fg='#1df700',
            bg='#0f1012', width=16, textvariable=RPD)         
rpd.grid(row='4', column='1', pady=(0, 10))

#No. of days worked===================================================
Label(frame, text="         No. of days worked :       ", font='arial 11 bold',
      fg='#c4c4c4', bg='#17161b').grid(row='5', column='0', pady=(0, 10))

no_work_d = Entry(frame, font='arial 12 bold', fg='#1df700',
                  bg='#0f1012', width=16, textvariable=WORK_DAY)
no_work_d.grid(row='5', column='1', pady=(0, 10))

#Gross Pay=============================================================
Label(frame, text="            Gross Pay   ", font='arial 14 bold',
      fg='orange', bg='#17161b').grid(row='6', column='0', pady=(0, 10),padx=(0,50),columnspan=2)

gp = Label(frame, font='arial 15 bold underline', fg='#1df700', textvariable=GP,
                                            bg='#0f1012', width=9, underline=True)
gp.grid(row='6', column='1', pady=(0, 10),padx=(20,0),columnspan=2)


#Deduction Label========================================================
Label(frame, text="         Deductions        ", font='arial 15 bold',
      fg='#c4c4c4', bg='#17161b').grid(row='7', column='0', pady=(0, 10))


#SSS Con’t =============================================================
Label(frame, text="                   SSS Con’t :   ", font='arial 11 bold',
      fg='#c4c4c4', bg='#17161b').grid(row='8', column='0', pady=(0, 10))

sssc = Entry(frame, font='arial 12 bold', fg='#1df700',
             bg='#0f1012', width=16, textvariable=SSS)
sssc .grid(row='8', column='1', pady=(0, 10))

#Phil Health=============================================================
Label(frame, text="              Phil Health :", font='arial 11 bold',
      fg='#c4c4c4', bg='#17161b').grid(row='9', column='0', pady=(0, 10))

ph = Entry(frame, font='arial 12 bold', fg='#1df700',
           bg='#0f1012', width=16, textvariable=PHIL_HEALTH)
ph.grid(row='9', column='1', pady=(0, 10))

#C/A======================================================================
Label(frame, text="                           C/A :", font='arial 11 bold',
      fg='#c4c4c4', bg='#17161b').grid(row='10', column='0', pady=(0, 10))

cpa = Entry(frame, font='arial 12 bold', fg='#1df700',
            bg='#0f1012', width=16, textvariable=CPA)
cpa.grid(row='10', column='1', pady=(0, 10))

#Total Deduction===========================================================
Label(frame, text="        TOTAL DEDUCTION         ", font='arial 12 bold',
      fg='orange', bg='#17161b').grid(row='11', column='0', pady=(0, 10),padx=(0,70),columnspan=2)

td = Label(frame, font='arial 15 bold underline', fg='#ff1100', textvariable=TD,
                                            bg='#0f1012', width=9, underline=True)
td.grid(row='11', column='1', pady=(0, 10),padx=(20,0),columnspan=2)

#Net Pay====================================================================
Label(frame, text="               NET PAY ", font='arial 14 bold',
      fg='orange', bg='#17161b').grid(row='12', column='0', pady=(0, 10),padx=(0,70),columnspan=2)

np = Label(frame, font='arial 15 bold underline', fg='#1df700', textvariable=NP,
                                            bg='#0f1012', width=9 )
np.grid(row='12', column='1', pady=(0, 10),padx=(20,0),columnspan=2)

#buttons=====================================================================
btn_exit = Button(root, text='EXIT', command=Exit, font='ArialNarrow 10 bold', fg='gray', bg='#050505',
       width=10, height=2,activebackground='#17161b',activeforeground='red')
btn_exit.place(x=0,y=17)
btn_cal = Button(frame, text='Calculate', command=calculate, font='ArialNarrow 10 bold', fg='#ffa500', bg='#050505',
       width=10, height=2).grid(row=13, column=0, columnspan=2, pady=(2, 2),  padx=(0, 89))

btn_save = Button(frame, text='Save Info.', command=saveInfo, font='ArialNarrow 10 bold', fg='#ffa500', bg='#050505',
       width=10, height=2).grid(row=13, column=1, columnspan=1, pady=(2, 2))

btn_delete = Button(frame, text='Delete', command=delete, font='ArialNarrow 10 bold', fg='#ffa500', bg='#050505',
       width=10, height=2).grid(row=14, column=0, columnspan=2, pady=(2, 2), padx=(0, 89))

btn_update = Button(frame, text='Update', command=update, font='ArialNarrow 10 bold', fg='#ffa500', bg='#050505',
       width=10, height=2).grid(row=14, column=1, columnspan=1, pady=(2,2))


#Error message================================================================
log_message = Label(frame,text='', font='arial 9',
      fg='#c4c4c4', bg='#17161b')
#data table===================================================================

scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("ID","Employee’s No", "Employee’s Name", "Rate/Day", "No. of days worked",
                                    "Gross Pay",'SSS Con’t','Phil Health','C/A ','Total Deductions','Net Pay'),
                    height=700, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
tree.pack(ipadx=0)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('ID', text="ID", anchor=N)
tree.heading('Employee’s No', text="Employee’s No", anchor=N)
tree.heading('Employee’s Name', text="Employee’s Name", anchor=N)
tree.heading('Rate/Day', text="Rate/Day", anchor=N)
tree.heading('No. of days worked', text="No. of days worked", anchor=N)
tree.heading('Gross Pay', text="Gross Pay", anchor=N)
tree.heading('SSS Con’t', text="SSS Con’t", anchor=N)
tree.heading('Phil Health', text="Phil Health", anchor=N)
tree.heading('C/A ', text="C/A ", anchor=N)
tree.heading('Total Deductions', text="Total Deductions", anchor=N)
tree.heading('Net Pay', text="Net Pay", anchor=N)
tree.column('#0', stretch=YES, minwidth=0, width=0, anchor=CENTER)
tree.column('#1', stretch=YES, minwidth=0, width=60, anchor=CENTER)
tree.column('#2', stretch=YES, minwidth=0, width=140, anchor=CENTER)
tree.column('#3', stretch=YES, minwidth=0, width=140, anchor=CENTER)
tree.column('#4', stretch=YES, minwidth=0, width=110, anchor=CENTER)
tree.column('#5', stretch=YES, minwidth=0, width=130, anchor=CENTER)
tree.column('#6', stretch=YES, minwidth=0, width=90, anchor=CENTER)
tree.column('#7', stretch=YES, minwidth=0, width=70, anchor=CENTER)
tree.column('#8', stretch=YES, minwidth=0, width=70, anchor=CENTER)
tree.column('#9', stretch=YES, minwidth=0, width=70, anchor=CENTER)
tree.column('#10', stretch=YES, minwidth=0, width=101, anchor=CENTER)
tree.column('#11', stretch=YES, minwidth=0, width=100, anchor=CENTER)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

root.mainloop()
