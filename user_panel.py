import sqlite3
from tkinter import * 
# from Authentification import *
from tkinter import ttk

import Authentification as at
conn = sqlite3.connect("bibliothéque.db")
c=conn.cursor()

def user():

    #Book's ====================================================================
    def clearr(event):
        if see == main_user.focus_get() and serr.get() == 'Search by ID':
            see.delete(0, END)
    def rett(event):
        if see != main_user.focus_get() and serr.get() == '':
            serr.set("Search by ID")
    def quitter():
        main_user.destroy()
        at.start()
    #interface ==============================================================
    main_user = Tk()
    main_user.geometry("550x600")
    main_user.title("BiblioTaka")
    main_user.configure(background='white')

    label_titre = Label(main_user,text="Book's",width=9,height=1,bg='white',fg='green',font=("Helvetica", 16))
    label_titre.place(x=10,y=10)

    tree_book=ttk.Treeview(main_user,columns=("a","b","c","d","e"))
    tree_book.heading('#0', text="Title")
    tree_book.heading('#1', text="Author")
    tree_book.heading('#2', text="ID")
    tree_book.heading('#3',text="date of birth")
    tree_book.heading('#4',text="price")
    tree_book.heading('#5',text="category")
    

    tree_book.column("#0", width=160)
    tree_book.column("#1", width=100)
    tree_book.column("#2", width=30)
    tree_book.column("#3", width=90)
    tree_book.column("#4", width=40)
    tree_book.column("#5", width=100) 
    tree_book.place(x=10,y=40)

   
    users = c.execute("""SELECT * FROM Book""")

    for elem in users:
        tree_book.insert("","end",text=elem[0],values=(elem[1],elem[2],elem[3],elem[4],elem[5]))
    
    serr=StringVar()
    see=Entry(main_user,textvariable= serr)
    see.place(x=240,y=13)
    serr.set("Search by ID")
    see.bind("<FocusIn>",clearr)
    see.bind("<FocusOut>",rett)

    #Emprunt =============================================================================================
    
    label_titre = Label(main_user,text="Borrowed",width=9,height=1,bg='white',fg='green',font=("Helvetica", 16))
    label_titre.place(x=10,y=280)

    tree_borow=ttk.Treeview(main_user,columns=("a","b","c","d","e"))
    tree_borow.heading('#0', text="CIN")
    tree_borow.heading('#1', text="ID")
    tree_borow.heading('#2',text="take date")
    tree_borow.heading('#3',text="dead line")
    tree_borow.heading('#4',text="etat")
    

    tree_borow.column("#0", width=160)
    tree_borow.column("#1", width=100)
    tree_borow.column("#2", width=30)
    tree_borow.column("#3", width=90)
    tree_borow.column("#4", width=40)
    tree_borow.place(x=10,y=310)

   
    emp = c.execute("""SELECT * FROM emprunt""")

    for elem in emp:
        tree_borow.insert("","end",text=elem[0],values=(elem[1],elem[2],elem[3],elem[4]))
    
    serrr=StringVar()
    seee=Entry(main_user,textvariable= serrr)
    seee.place(x=240,y=285)
    serrr.set("Search by ID")
    seee.bind("<FocusIn>",clearr)
    seee.bind("<FocusOut>",rett)


    main_user.mainloop()