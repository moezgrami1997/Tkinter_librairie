import sqlite3
from tkinter import * 
from tkinter.messagebox import *
#import admin_panel as ap
from admin_panel import *
import registration as re
import user_panel as up 
conn = sqlite3.connect("bibliothéque.db")
c=conn.cursor()

def start():
    def Verification():
        
        def test():
            l=[False,0]
            for i in c:
                if  Motdepasse.get() == i[1] and  Email.get() == i[0] :
                    l[0] = True
                    l[1] = i[2]
            return l  

        
        #if val.get()==1:
        c.execute('SELECT mail,password,role FROM User')
        #elif val.get()==2:
        #    c.execute('SELECT mail,password FROM User')
        #else:
        #    showwarning('Radio button error','Veuillez spécifier votre role !')
        #    return
        l=test()

        if l[0]==True:
            main.destroy()
            if l[1]==2:
                admin()                
            elif l[1]==1:
                up.user()
            elif l[1]==0:
                showwarning('Ban','You are Banned.\nCheck the root for more details !')
 
        else:
            showwarning('Résultat','Mot de passe incorrect.\nVeuillez recommencer !')
            Motdepasse.set('')


    def registration():
        main.destroy()
        re.reg()

    
    #fenétre main de login
    main = Tk()
    main.title("Authentification")
    main.geometry("300x250")
    main.resizable(False, False)
    main.configure(background='white')

    #label
    label_titre = Label(main,text='BiblioTaka',width=9,height=1,bg='white',fg='green',font=("Helvetica", 16))
    label_titre.place(x=100,y=10)
    label_login = Label(main,text='Email',width=10,bg='white')
    label_login.place(x=40,y=70)
    label_password = Label(main,text='Password',width=10,bg='white')
    label_password.place(x=30,y=100)
    #champ de text
    Email = StringVar()
    text_email = Entry(main,textvariable= Email)
    text_email.place(x=130,y=70)
    Motdepasse= StringVar()
    password = Entry(main,textvariable= Motdepasse,show='*')
    password.place(x=130,y=100)
    
    #Radiocheck
    # val=IntVar()
    # Radio1=Radiobutton(main,text="Root",value=1,variable=val)
    # Radio1.place(x=130,y=130)
    # Radio2=Radiobutton(main,text="User",value=2,variable=val)
    # Radio2.place(x=190,y=130)

    #bouton
    login_btn = Button(main, text='Login',width=8,bg='white',command = Verification)
    login_btn.place(x=180,y=170)
    register_btn = Button(main, text='Register',width=8,bg='white',command = registration)
    register_btn.place(x=105,y=170)

    main.mainloop()


start()
