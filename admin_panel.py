import sqlite3
from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import *
from add_book import *
import Authentification as at
import registration as re


conn = sqlite3.connect("bibliothéque.db")
c=conn.cursor()

def admin():              

    def promote():
        curr = tree_user.focus()
        L=tree_user.item(curr)
        cinn=L['values'][2]
        role = L['values'][3]
        if(role==1):
            c.execute("""Update User SET role=? WHERE cin=?""",(2,cinn))
        elif(role==0):
            c.execute("""Update User SET role=? WHERE cin=?""",(1,cinn))
        conn.commit()
        main_admin.destroy()
        admin()

    def demote():
        curr = tree_user.focus()
        L=tree_user.item(curr)
        cinn=L['values'][2]
        role = L['values'][3]
        if(role==1):
            c.execute("""Update User SET role=? WHERE cin=?""",(0,cinn))
        elif(role==2):
            c.execute("""Update User SET role=? WHERE cin=?""",(1,cinn))
        conn.commit()
        main_admin.destroy()
        admin()

    def registration():
        main_admin.destroy()
        re.reg()


    def quitter():
        main_admin.destroy()
        at.start()

    #Interface===========================================================
    main_admin = Tk()
    main_admin.geometry("550x600")
    main_admin.title("BiblioTaka Admin_panel")
    main_admin.configure(background='white')

    #menu bar ==================================================================================
    menu = Menu(main_admin)
    sousmenu1 = Menu(menu, tearoff = 0)
    menu.add_cascade(label="Livre", menu=sousmenu1)
    #sousmenu1.add_command(label="ajouter",command=quitter)
    #sousmenu1.add_command(label="supprimer",command=quitter)

    sousmenu2 = Menu(menu, tearoff = 0)
    menu.add_cascade(label="étudiant", menu=sousmenu2)
    #sousmenu2.add_command(label="recruter",command=registration)
    #sousmenu2.add_command(label="virer",command=quitter)

    sousmenu3 = Menu(menu, tearoff = 0)
    menu.add_cascade(label="Emprunts", menu=sousmenu3)
    #sousmenu3.add_command(label="add",command=quitter)
    #sousmenu3.add_command(label="remove",command=quitter)
    
    
    menu.add_command(label="Quitter",command=quitter)
    main_admin.config(menu = menu)

    #User===========================================================================
    def clear(event):
        if se == main_admin.focus_get() and ser.get() == 'Search by cin':
            se.delete(0, END)
    def ret(event):
        if se != main_admin.focus_get() and ser.get() == '':
            ser.set("Search by cin")
    
    label_titre = Label(main_admin,text="User's",width=9,height=1,bg='white',fg='green',font=("Helvetica", 16))
    label_titre.place(x=10,y=10)

    tree_user=ttk.Treeview(main_admin,columns=("a","b","c","d"))
    tree_user.heading('#0', text="Nom")
    tree_user.heading('#1', text="prenom")
    tree_user.heading('#2', text="mail")
    tree_user.heading('#3',text="cin")
    tree_user.heading('#4',text="role")
    
    tree_user.column("#0", width=120)
    tree_user.column("#1", width=120)
    tree_user.column("#2", width=120)
    tree_user.column("#3", width=120) 
    tree_user.column("#4", width=40) 
    tree_user.place(x=10,y=40)

    users = c.execute("""SELECT * FROM User""")

    for elem in users:
        tree_user.insert("","end",text=elem[0],values=(elem[1],elem[2],elem[5],elem[7]))
    
    ser=StringVar()
    se=Entry(main_admin,textvariable= ser)
    se.place(x=240,y=13)
    ser.set("Search by cin")
    se.bind("<FocusIn>",clear)
    se.bind("<FocusOut>",ret)

    demote_btn = Button(main_admin, text='Demote',width=8,bg='white',command = demote)
    demote_btn.place(x=380,y=8)

    promote_btn = Button(main_admin, text='Promote',width=8,bg='white',command = promote)
    promote_btn.place(x=450,y=8)

    #Book===========================================================================
    def clearr(event):
        if see == main_admin.focus_get() and serr.get() == 'Search by ID':
            see.delete(0, END)
    def rett(event):
        if see != main_admin.focus_get() and serr.get() == '':
            serr.set("Search by ID")
    def add():
        main_admin.destroy()
        addd()   
        main_admin.destroy()
        admin()    
    
    def remove():
        a = tree_book.focus()
        L=tree_book.item(a)
        c.execute("""DELETE from book where ID=?""",(L['values'][1],))
        conn.commit()
        main_admin.destroy()
        admin()
        
    
    label_titre = Label(main_admin,text="Book's",width=9,height=1,bg='white',fg='green',font=("Helvetica", 16))
    label_titre.place(x=10,y=280)

    tree_book=ttk.Treeview(main_admin,columns=("a","b","c","d","e"))
    tree_book.heading('#0', text="Title")
    tree_book.heading('#1', text="Author")
    tree_book.heading('#2', text="ID")
    tree_book.heading('#3',text="date of birth")
    tree_book.heading('#4',text="Quantiter")
    tree_book.heading('#5',text="category")
    

    tree_book.column("#0", width=120)
    tree_book.column("#1", width=100)
    tree_book.column("#2", width=30)
    tree_book.column("#3", width=90)
    tree_book.column("#4", width=80)
    tree_book.column("#5", width=100) 
    tree_book.place(x=10,y=310)

   
    users = c.execute("""SELECT * FROM Book""")

    for elem in users:
        tree_book.insert("","end",text=elem[0],values=(elem[1],elem[2],elem[3],elem[4],elem[5]))
    
    serr=StringVar()
    see=Entry(main_admin,textvariable= serr)
    see.place(x=240,y=285)
    serr.set("Search by ID")
    see.bind("<FocusIn>",clearr)
    see.bind("<FocusOut>",rett)

    remove_btn = Button(main_admin, text='Remove',width=8,bg='white',command = remove)
    remove_btn.place(x=380,y=280)

    add_btn = Button(main_admin, text='Add',width=8,bg='white',command = add)
    add_btn.place(x=450,y=280)


    main_admin.mainloop()



