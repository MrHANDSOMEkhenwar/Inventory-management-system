import tkinter
from tkinter import *
import pymysql
from tkinter  import messagebox
from tkinter import ttk
def upd1():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title("STORE")
    am=[]
    def filldata():
        dc=pymysql.connect(host='localhost',user='root',password='root',database='store')
        cur = dc.cursor()
        sql="select storeid from storeinfo"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            am.append(res[0])
        dc.close() 
    def updatedata():
        dc=pymysql.connect(host='localhost',user='root',password='root',database='store')
        cur = dc.cursor()
        xa=int(en.get())
        xb=f.get()
        xc=g.get()
        xd=h.get()
        xe=la.get()
        xf=int(he.get())
        sql="insert into storeinfo values (%d,'%s','%s','%s','%s',%d)"%(xa,xb,xc,xd,xe,xf)
        cur.execute(sql)
        dc.commit()
        messagebox.showinfo('hi','DATA SAVED')
        dc.close()
        en.delete(0,100)
        f.delete(0,100)
        g.delete(0,100)
        h.delete(0,100)
        la.delete(0,100)
        he.delete(0,100)
    kl=Label(t,text='Storeid')
    kl.place(x=50,y=50)
    en=Entry(t,width=30)
    en.place(x=200,y=50)
    b=Label(t,text='Name')
    b.place (x=50,y=100)
    f=Entry(t,width=30)
    f.place(x=200,y=100)
    c=Label(t,text='Address')
    c.place(x=50,y=150)
    g=Entry(t,width=30)
    g.place(x=200,y=150)
    d=Label(t,text='phone')
    d.place(x=50,y=200)
    h=Entry(t,width=30)
    h.place(x=200,y=200)
    j=Label(t,text='email')
    j.place(x=50,y=250)
    la=Entry(t,width=30)
    la.place(x=200,y=250)
    k=Label(t,text='Regno')
    k.place(x=50,y=300)
    he=Entry(t,width=30)
    he.place(x=200,y=300)
    bt=Button(t,text='Update',command=updatedata)
    bt.place(x=100,y=350)
    t.mainloop()