from tkinter import  *
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import os
root=Tk()
root.iconbitmap('images/logo.ico')
#=======================================Variables=======================================
first_name, last_name = " Ian Nico ", "Caulin "
fullName = first_name + last_name  
age = edad = "     18 yrs old     "                  
date_of_birth = "  April 21 , 2002 " 
gender = "         Male         "
address = " Zone 1 Villa de Oro Kauswagan CDOC"

CivilStatus = "        Single        "  
heightMe = "           5'9\"          "
weightMe = "        73.8 KG       "
skillS= """     Photo/Video Editing,
        Digital Painting,
           Swimming"""
bloodType = "          AB          "       
nationality = "       Filipino      "
religion = "Roman Catholic " 
contact_number = ["0995-996-9621", "0977-156-1230"]  
contact_number1, contact_number2 = contact_number 
email = "iannicocaulin@gmail.com"
sayings = "     \"Kung di mo kaya \n     pagawa mo sa akin.\"" 
hobbies = """               Editing
              Singing
          Programming,
        Playing Guitar
        Playing DotA/ML   """  

fav_color = "Red and Orange"
EducationalBackground = ["         Bonbon Elementary School     ", "  Cagayan de Oro National High School",
                         "        Bonbon National High School     ", "          Liceo de Cagayan University     "]  
elemantary, high_school1, high_school2, senior_high_school = EducationalBackground

#===============================Variables==============================
style = ttk.Style()
style.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': '#0f1012',
                                       'fieldforebackground': '#1df700',
                                       'fieldbackground': '#0f1012',
                                       'foreground':'#1df700',
                                       'background': '#0f1012',
                                       'bd':1, 
                                       'relief':SUNKEN,
                                       'width':14,
                                       }}}
                         )
style.theme_use('combostyle') 
next = PhotoImage(file='images/next.png')
prev = PhotoImage(file = 'images/prev.png')
exit = PhotoImage(file='images/exit.png')
title = PhotoImage(file='images/title.png')
def page1():
    frame = Frame(root)
    frame.tkraise()
    Top = Frame(root,bg='#050505')
    Top.pack(fill=X)
    Bottom = Frame(root,bg='black',pady=5)
    Bottom.pack(fill=X,side=BOTTOM)
    root.title('BIODATA: Ian Nico M. Caulin')

    width = 830
    height = 550
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(False,False)

    root.configure(bg="#17161b")
    frame.configure(bg="#17161b")
    
    Label(Top,image=title,bg='#050505',borderwidth=0).grid(row='0',column='0',columnspan=3)
    Label(Bottom,text = "______________________________________________________________________",font='ArialNarrow 20 bold',fg='#ffa500',bg='#050505',borderwidth=0).grid(row='0',column='0',padx=(0,0))

    Label(frame,text= "         N A M E:",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='2',column='1',pady=(30,0))
    Efname = Entry(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=14)
    Efname.insert(END,fullName)
    Efname.grid(row='2',column='2',pady=(30,0))

    Label(frame,text= "             A G E: ",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='3',column='1')
    Eage= Entry(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=14)
    Eage.insert(END,age)
    Eage.grid(row='3',column='2')

    Label(frame,text= "DATE OF BIRTH :         ",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='4',column='1',padx=(2,0))
    Ebirthday= Entry(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=14)
    Ebirthday.insert(END,date_of_birth)
    Ebirthday.grid(row='4',column='2')

    Label(frame,text= "     GENDER :",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='5',column='1',padx=(2,0))
    Egender = Entry(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=14)
    Egender.insert(END,gender)
    Egender.grid(row='5',column='2')

    Label(frame,text= "   ADDRESS :",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='6',column='1',pady=(1,20))
    Eaddress = Text(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=14,height=3)
    Eaddress.insert(END,address)
    Eaddress.grid(row='6',column='2',pady=(10,30))

    Label(frame,text= "NATIONALITY :     ",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='8',column='1',padx=(2,0))
    Enationality = Entry(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=14)
    Enationality.insert(END,nationality)
    Enationality.grid(row='8',column='2',padx=(2,0))

    Label(frame,text= "   RELIGION :",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='9',column='1',padx=(2,0))
    Ereligion = Entry(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=14)
    Ereligion.insert(END,religion)
    Ereligion.grid(row='9',column='2',padx=(2,0))

    Label(frame,text= "CIVIL STATUS :     ",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='10',column='1',padx=(2,0))
    ECivilStatus = Entry(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=14)
    ECivilStatus.insert(END,CivilStatus)
    ECivilStatus.grid(row='10',column='2')

    Button(frame,image=exit,activebackground='#17161b',bg="#17161b",command=Exit,borderwidth=0,cursor= "circle").grid(row=11,column=1,pady=(35,0))
    Button(frame,image=next,activebackground='#17161b',bg="#17161b",command=page2,borderwidth=0,cursor= "circle").grid(row=11,column=2,pady=(35,0))
    frame.pack()

    root.mainloop()

def page2():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title('BIODATA: Ian Nico M. Caulin')
    frame = Frame(Home)
    Top = Frame(Home, bd=2, relief=RAISED,bg='#050505')
    Top.pack(fill=X)
    Bottom = Frame(Home, bd=2,bg='black')
    Bottom.pack(fill=X,side=BOTTOM)
    Home.title('BIODATA: Ian Nico M. Caulin')


    width = 830
    height = 620
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(True,False)
    

    Home.configure(bg="#17161b")
    frame.configure(bg="#17161b")
    Label(Top,text = "______________________________________________________________________________________________",font='ArialNarrow 20 bold',fg='#ffa500',bg='#050505').grid(row='0',column='0',padx=(0,0))
    Label(Bottom,text = "______________________________________________________________________________________________",font='ArialNarrow 20 bold',fg='#ffa500',bg='#050505').grid(row='0',column='0',padx=(0,0))
    Label(frame,text= "Contact Details          ",font='ArialNarrow 15 bold',fg='orange',bg='#17161b').grid(row='1',column='1',pady=(10,0))



    Label(frame,text= "     CONTACT #:     ",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='2',column='1',pady=(20,0))
    Econtact_number1= ttk.Combobox(frame,values=[contact_number1,contact_number2],font='arial 13 bold')
    Econtact_number1.current(1)
    Econtact_number1['state'] = 'readonly'
    Econtact_number1.grid(row='2',column='2',pady=(20,0))


    Label(frame,text= "      EMAIL ID: ",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='4',column='1')
    Eemail = Entry(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=22)
    Eemail.insert(END,email)
    Eemail.grid(row='4',column='2')

    Label(frame,text= "Personal Description",font='arial 15 bold',fg='orange',bg='#17161b').grid(row='5',column='1',pady=(20,20),ipadx=20)


    Label(frame,text= "     SAYINGS :",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='6',column='1',padx=(2,0))
    Esayings = Text(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=22,height=2)
    Esayings.insert(END,sayings)
    Esayings.grid(row='6',column='2')

    Label(frame,text= "     HOBBIES :",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='7',column='1',pady=(20,18))
    Ehobbies = Text(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=22,height=2)
    Ehobbies.insert(END,hobbies)
    Ehobbies.grid(row='7',column='2',pady=(10,3))

    Label(frame,text= "     FAVORITE COLOR :                 ",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='8',column='1',pady=(1,2))
    Label(frame,text= fav_color,font='arial 11 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN).grid(row='8',column='2',pady=(1,2))
    Efav_color = Entry(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=14)
    Efav_color.insert(END,fav_color)
    Efav_color.grid(row='8',column='2',pady=(1,2))

    Label(frame,text= "        HEIGHT :",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='9',column='1',pady=(1,2))
    EheightMe = Entry(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=14)
    EheightMe.insert(END,heightMe)
    EheightMe.grid(row='9',column='2',pady=(1,2))

    Label(frame,text= "        WEIGHT :",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='10',column='1',pady=(1,2))
    EweightMe = Entry(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=14)
    EweightMe.insert(END,weightMe)
    EweightMe.grid(row='10',column='2',pady=(1,2))

    Label(frame,text= "         SKILLS :",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='11',column='1',pady=(1,2))
    EskillS = Text(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=22,height=2)
    EskillS.insert(END,skillS)
    EskillS.grid(row='11',column='2',pady=(1,6))

    Label(frame,text= "     BLOOD TYPE :        ",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='12',column='1',pady=(1,2))
    EbloodType = Entry(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=14)
    EbloodType.insert(END,bloodType)
    EbloodType.grid(row='12',column='2',pady=(1,6))

    



  
    Button(frame,image=prev,activebackground='#17161b',bg="#17161b",command=Back,borderwidth=0,cursor= "circle").grid(row=20,column=1,padx=(100,20),pady=(20,0))
    Button(frame,image=next,activebackground='#17161b',bg="#17161b",command=page3,borderwidth=0,cursor= "circle").grid(row=20,column=2,pady=(20,0))
    
    frame.pack()
    Home.mainloop()

def page3():
    global Home1
    root.withdraw()
    Home.withdraw()
    
    Home1 = Toplevel()
    Home1.title('BIODATA: Ian Nico M. Caulin')
    
  
    frame = Frame(Home1)
    Top = Frame(Home1, bd=2, relief=RAISED,bg='#050505')
    Top.pack(fill=X)
    Bottom = Frame(Home1, bd=2,bg='black')
    Bottom.pack(fill=X,side=BOTTOM)
    Home1.title('BIODATA: Ian Nico M. Caulin')


    width = 830
    height = 550
    screen_width = Home1.winfo_screenwidth()
    screen_height = Home1.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home1.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home1.resizable(True,False)
    

    Home1.configure(bg="#17161b")
    frame.configure(bg="#17161b")

    Label(Top,text= "EDUCATIONAL BACKGROUND________________________________________________",font='ArialNarrow 20 bold',fg='#ffa500',bg='#050505').grid(row='0',column='0',columnspan=3,padx=(15,0))
    Label(Bottom,text = "______________________________________________________________________________________________",font='ArialNarrow 20 bold',fg='#ffa500',bg='#050505').grid(row='0',column='0',padx=(0,0))
    Label(frame,text= "  ELEMENTARY         ",font='ArialNarrow 15 bold',fg='orange',bg='#17161b').grid(row='1',column='1',pady=(30,10))

    Label(frame,text= "        GRADE 1-6:       ",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='2',column='1',pady=(3,3))
    Eelemantary = Entry(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=35)
    Eelemantary.insert(END,elemantary)
    Eelemantary.grid(row='2',column='2',pady=(3,3))

    Label(frame,text= "  HIGH SCHOOL         ",font='ArialNarrow 15 bold',fg='orange',bg='#17161b').grid(row='3',column='1',pady=(30,10))

    Label(frame,text= "          GRADE 7:     ",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='4',column='1',pady=(3,3))
    Ehigh_school1 = Entry(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=35)
    Ehigh_school1.insert(END,high_school1)
    Ehigh_school1.grid(row='4',column='2',pady=(3,3))

    Label(frame,text= "     GRADE 8-10:     ",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='5',column='1',pady=(10,0))
    Ehigh_school2 = Entry(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=35)
    Ehigh_school2.insert(END,high_school2)
    Ehigh_school2.grid(row='5',column='2',pady=(10,0))

    Label(frame,text= "        SENIOR HIGH SCHOOL ",font='ArialNarrow 15 bold',fg='orange',bg='#17161b').grid(row='6',column='1',pady=(30,10))

    Label(frame,text= "        GRADE 11-12:          ",font='arial 12 bold',fg='#c4c4c4',bg='#17161b').grid(row='7',column='1',pady=(3,3))
    Esenior_high_school = Entry(frame,font='arial 13 bold',fg='#1df700',bg='#0f1012',bd=1,relief=SUNKEN,width=35)
    Esenior_high_school.insert(END,senior_high_school)
    Esenior_high_school.grid(row='7',column='2',pady=(3,3))

    #Button(frame,text="< Preactivebackground='#17161b',v",fg='#050505',bg='orange',font='arial 10 bold',padx=10,pady=6,border=0,command=Back1).grid(row=11,column=1,padx=(0,20),pady=(40,0))
    Button(frame,image=prev,activebackground='#17161b',bg="#17161b",command=Back1,borderwidth=0,cursor= "circle").grid(row=11,column=1,padx=(70,20),pady=(40,0))
    Label(frame,text= "© N I C O 2 0 2 1",font='arial 13 ',fg='gray',bg='#17161b').grid(row='12',column='2',pady=(20,3))
    frame.pack()
    Home1.mainloop()
def Exit():
    result = tkMessageBox.askquestion('P A H I M A N G N O !', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.withdraw()
        os.system('main.py')
        exit()
def Back():
    Home.destroy()
    root.deiconify()
def Back1():
    Home.deiconify()
    Home1.destroy()  

page1()