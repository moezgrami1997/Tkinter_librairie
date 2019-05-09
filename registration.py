import sqlite3
from tkinter import * 
from tkinter.messagebox import *
import Authentification as at
conn = sqlite3.connect("bibliothéque.db")
c=conn.cursor()

def reg():
    def insertion():
        c.execute("INSERT INTO User VALUES (?,?,?,?,?,?,?,?)",(Nom.get(), Prenom.get(), Mail.get(), Tel.get(), Password.get(), Cin.get(), Adresse.get(),1 ))        
        conn.commit()
        

    def test(Mail,Cin):
        c.execute('SELECT mail,cin FROM User')
        t = False
        for i in c:
            if  Mail.get() == i[0] or Cin.get() == i[1] :
                t = True  
        return t

    def quitter():
        main_enr.destroy()
        at.start()

    def verif_vide():
        if(Nom.get()=="" or Prenom.get()=="" or Mail.get()==""or Tel.get()=="" or Password.get()=="" or Cin.get()=="" or Adresse.get()==""):
            showwarning('Error','Veuillez remplir tout les champs\nmerci !')
        else:
            if(test(Mail,Cin)==False):
                insertion()
                showinfo('Succés','Enregistrement réaliser avec succées !')
                quitter()
            else:
                showwarning('Error','Email ou Cin déja utiliser essayer de vous connecter\nmerci !')

    #fenétre main d'enregistrement
    main_enr = Tk()
    main_enr.title("Register")
    main_enr.geometry("400x420")
    main_enr.resizable(False, False)
    main_enr.configure(background='white')

    #label
    label_titre = Label(main_enr,text='BiblioTaka',width=9,height=1,bg='white',fg='green',font=("Helvetica", 16))
    label_titre.place(x=100,y=10)
    label_Nom = Label(main_enr,text='Nom',width=10,bg='white')
    label_Nom.place(x=40,y=70)
    label_Prenom = Label(main_enr,text='Prenom',width=10,bg='white')
    label_Prenom.place(x=40,y=100)
    label_Mail = Label(main_enr,text='Mail',width=10,bg='white')
    label_Mail.place(x=30,y=130)
    label_Tel = Label(main_enr,text='Tel',width=10,bg='white')
    label_Tel.place(x=30,y=160)
    label_Password = Label(main_enr,text='Password',width=10,bg='white')
    label_Password.place(x=30,y=190)
    label_Cin = Label(main_enr,text='Cin',width=10,bg='white')
    label_Cin.place(x=30,y=220)
    label_Adresse = Label(main_enr,text='Adresse',width=10,bg='white')
    label_Adresse.place(x=30,y=250)


    #champ de text
    Nom = StringVar()
    text_Nom = Entry(main_enr,textvariable= Nom)
    text_Nom.place(x=130,y=70)
    Prenom = StringVar()
    text_Prenom = Entry(main_enr,textvariable= Prenom)
    text_Prenom.place(x=130,y=100)
    Mail= StringVar()
    text_Mail = Entry(main_enr,textvariable= Mail)
    text_Mail.place(x=130,y=130)
    Tel= StringVar()
    text_Tel = Entry(main_enr,textvariable= Tel)
    text_Tel.place(x=130,y=160)
    Password= StringVar()
    text_Password = Entry(main_enr,textvariable= Password)
    text_Password.place(x=130,y=190)
    Cin= StringVar()
    text_Cin = Entry(main_enr,textvariable= Cin)
    text_Cin.place(x=130,y=220)
    Adresse= StringVar()
    text_Adresse = Entry(main_enr,textvariable= Adresse)
    text_Adresse.place(x=130,y=250)

    #bouton
    login_btn = Button(main_enr, text='Register',width=8,bg='white',command = verif_vide)
    login_btn.place(x=195,y=300)
    close_btn = Button(main_enr, text='Close',width=8,bg='white',command = quitter)
    close_btn.place(x=120,y=300)
    
    main_enr.mainloop()
 