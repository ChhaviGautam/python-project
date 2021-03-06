import mysql.connector                                     #to view saved data
from tkinter import *                                      #for creating GUI application
from tkinter import messagebox                             #for showing message after insertion 
db=mysql.connector.connect(host='localhost',
                           user='root',                    #for creating connectivity
                           password='root',
                           database='hospital'
                           )
my_cur=db.cursor()                                          #for creating changes one row at a time

def entry():
    root=Tk()
    root.title('covid patient management')
    root.geometry('250x300')
    Label(root,text="Patient detail Form",font='arial 14 bold',bg="yellow").grid(row=0,columnspan=2)
    Label(root,text="").grid(row=1,column=0)
    Label(root,text="serialno",bg="pink").grid(row=2,column=0)
    Label(root,text="").grid(row=3,column=0)
    Label(root,text="name",bg="yellow").grid(row=4,column=0)
    Label(root,text="").grid(row=5,column=0)
    Label(root,text="age",bg="pink").grid(row=6,column=0)
    Label(root,text="").grid(row=7,column=0)
    Label(root,text="doctor",bg="pink").grid(row=8,column=0)
    Label(root,text="").grid(row=9,column=0)
    Label(root,text="address",bg="yellow").grid(row=10,column=0)                        #function about hows the form looks like
    Label(root,text="").grid(row=11,column=0)
    Label(root,text="mob",bg="pink").grid(row=12,column=0)                              #using label for making line widget
    Label(root,text="").grid(row=13,column=0)                                           #using root for adding object
    Label(root,text="testreport",bg="red").grid(row=14,column=0)
    Label(root,text="").grid(row=15,column=0)
    Label(root,text="admitteddays",bg="yellow").grid(row=16,column=0)
    Label(root,text="").grid(row=17,column=0)
    Label(root,text="amount",bg="pink").grid(row=19,column=0)
    Label(root,text="").grid(row=19,column=0)
    v1=StringVar()
    v2=StringVar()
    v3=StringVar()
    v4=StringVar()
    v5=StringVar()                                                                  #entries for filling this later
    v6=StringVar()
    v7=StringVar()
    v8=StringVar()
    v9=StringVar()
    e1=Entry(root,textvariable=v1).grid(row=2,column=1)
    e2=Entry(root,textvariable=v2).grid(row=4,column=1)
    e3=Entry(root,textvariable=v3).grid(row=6,column=1)
    e4=Entry(root,textvariable=v4).grid(row=8,column=1)                             #entry widget is used to create input field
    e5=Entry(root,textvariable=v5).grid(row=10,column=1)
    e6=Entry(root,textvariable=v6).grid(row=12,column=1)
    e7=Entry(root,textvariable=v7).grid(row=14,column=1)
    e8=Entry(root,textvariable=v8).grid(row=16,column=1)
    e9=Entry(root,textvariable=v9).grid(row=18,column=1)
    Label(root,text="").grid(row=20,column=0)

    def insert():
        serialno=v1.get()
        name=v2.get()
        age=v3.get()
        doctor=v4.get()
        address=v5.get()                                                          #function for inserting all entries
        mob=v6.get()
        testreport=v7.get()
        admitteddays=v8.get()
        amount=v9.get()
        
        my_cur=db.cursor()                                                #creating database
        my_cur.execute('insert into reports values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(serialno,name,age,doctor,address,mob,testreport,admitteddays,amount))     #showing the final database
        db.commit()                                                         #it execute many entries at one time
        messagebox.showinfo('Wow','1 record inserted')                      #message shows after insertion
        v1.set('')
        v2.set('')
        v3.set('')
        v4.set('')
        v5.set('')
        v6.set('')
        v7.set('')
        v8.set('')
        v9.set('')

    def clear():
        v1.set('')
        v2.set('')
        v3.set('')                                                       #for reseting clear all entries
        v4.set('')
        v5.set('')
        v6.set('')
        v7.set('')
        v8.set('')
        v9.set('')

    def close():
        root.destroy()                                                        #for exit
    Button(root,text='SUBMIT',command=insert).grid(row=21,column=0)
    Button(root,text='RESET',command=clear).grid(row=21,column=1)               #creating buttons
    Button(root,text='EXIT',command=close).grid(row=21,column=2)
    root.mainloop()

entry()

