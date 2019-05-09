import sqlite3
from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import *
import admin_panel as ap
conn = sqlite3.connect("bibliothéque.db")
c=conn.cursor()

def addd():
    def quit():
        m.destroy()
        ap.admin()
        

    def add_book(text_Title,text_label_auteur,text_ID,text_DS,text_quantiter,text_Categorie):
        def insertion():
            c.execute("INSERT INTO Book('titre','auteur','ID','date_sortie','quantiter','genre') VALUES (?,?,?,?,?,?)",(text_Title.get(),text_label_auteur.get(),text_ID.get(), text_DS.get(), text_quantiter.get(), text_Categorie.get()))        
            conn.commit()

        def test():
            c.execute('SELECT ID FROM Book')
            t = False
            for i in c:
                if  text_ID.get() == i[0] :
                    t = True  
            return t
                    
        if(text_Title.get()=="" or text_label_auteur.get()=="" or text_ID.get()==""or text_DS.get()=="" or text_quantiter.get()=="" or text_Categorie.get()=="" ):
            showwarning('Error','Veuillez remplir tout les champs\nmerci !')
        
        # if (type( int(text_ID.get()) ) is int)==False or ( type(int(text_quantiter.get())) is int)==False :
        #     showwarning('Error','ID and Price must be an integer\nthanks !')
        else:
            if(test()==False):
                insertion()
                showinfo('Succés','Ajout de livre réaliser avec succées !')
                quit()
            else:
                showwarning('Error','ID déja utiliser!!!')

    #fenétre main d'enregistrement
    m = Tk()
    m.title("add book")
    m.geometry("350x330")
    m.resizable(False, False)
    m.configure(background='white')

    #label
    label_titre = Label(m,text='BiblioTaka',width=9,height=1,bg='white',fg='green',font=("Helvetica", 16))
    label_titre.place(x=100,y=10)
    label_Title = Label(m,text='Title',width=10,bg='white')
    label_Title.place(x=40,y=70)
    label_auteur = Label(m,text='Auteur',width=10,bg='white')
    label_auteur.place(x=40,y=100)
    label_ID = Label(m,text='ID',width=10,bg='white')
    label_ID.place(x=30,y=130)
    label_DS = Label(m,text='Out date',width=10,bg='white')
    label_DS.place(x=30,y=160)
    label_price = Label(m,text='Quantity',width=10,bg='white')
    label_price.place(x=30,y=190)
    label_genre = Label(m,text='Category',width=10,bg='white')
    label_genre.place(x=30,y=220)


    #champ de text
    text_Title = Entry(m)
    text_Title.place(x=130,y=70)

    text_label_auteur = Entry(m)
    text_label_auteur.place(x=130,y=100)
    
    text_ID = Entry(m)
    text_ID.place(x=130,y=130)

    text_DS = Entry(m)
    text_DS.place(x=130,y=160)
    
    text_quantiter = Entry(m)
    text_quantiter.place(x=130,y=190)
    
    text_Categorie = Entry(m)
    text_Categorie.place(x=130,y=220)
    
    #bouton
    login_btn = Button(m, text='Add book',width=8,bg='white',command = lambda:add_book(text_Title,text_label_auteur,text_ID,text_DS,text_quantiter,text_Categorie))
    login_btn.place(x=195,y=300)
    close_btn = Button(m, text='Close',width=8,bg='white',command = quit)
    close_btn.place(x=120,y=300)

    m.mainloop()

