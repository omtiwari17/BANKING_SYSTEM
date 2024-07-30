from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkcalendar import Calendar
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime
from tkinter import Entry, Tk
from tkinter import messagebox
import os
import tkinter.messagebox as m
import datetime
import time
from tkinter import ttk

window=Tk()
window.title("Deposit")
window.config(bg="skyblue")
w=window.winfo_screenwidth()-700
h=window.winfo_screenheight()-450
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
wpos=(sw/2)-(w/2)
hpos=(sh/2)-(h/2)
window.geometry("%dx%d+%d+%d"%(w,h,wpos,hpos))
window.maxsize(1000,800)
window.minsize(400,200)

mydb=mysql.connector.connect(host='localhost',
                             database='bankdb',
                             user='root',
                             password='root',
                             charset='utf8')

mycursor=mydb.cursor()

accno1=''
abc=StringVar()

def saveindb():
    new["state"]=NORMAL
    save["state"]=NORMAL
    Balancevar=rupe.get()
    query = "update banktb set Balance=Balance+%s WHERE Account_no=%s"
    print(Balancevar,accno1)
    args = (Balancevar,accno1)

    try:
        mycursor.execute(query,args)
        mydb.commit()
        messagebox.showinfo("SUCCESSFULLY DEPOSIT", "Deposit successfully")

    except Error as error:
        print("Failed to insert record into table {}".format(error))#print(error)
        messagebox.showinfo("ERROR",format(error))
    
    finally:
        print('Done')


def fetchacno():
    M=[]
    query1 = "select distinct Account_no from banktb"
    try:
        mycursor = mydb.cursor()
        mycursor.execute(query1)
        records = mycursor.fetchall()
        for i in range(0, mycursor.rowcount):
            M.append(records[i][0])
            acc=M[i]
        
        # print(acc)
        selected_month = StringVar()
        month_cb = ttk.Combobox(window, textvariable=abc)
        month_cb['values'] = tuple(M)
        month_cb['state'] = 'normal'
        month_cb.place(x=415,y=120)

    except Error as error:
        print("Failed to select record from table {}".format(error))#print(error)
        messagebox.showinfo("SQL ERROR",error)
    finally:
        print("Done")


def showacc():
    global accno1
    accno1=abc.get()
    query = "select  * from banktb  where Account_no = %s"
    args = (accno1,)

    #Acc holder name
    l2=Label(window,text="Account Holder Name:-",font=("comic sans ms",14,"bold"))    
    l2.config(bg="white",fg="red")
    l2.place(x=605,y=130)
    
    accholder=StringVar()    
    rupe=Entry(window,textvariable=accholder,width=15,font=("comic sans ms",14,"bold"))
    rupe.config(bg="white",fg="black")
    rupe.place(x=615,y=170)       
    
    #Balance
    l3=Label(window,text="Balance:-",font=("comic sans ms",14,"bold"))    
    l3.config(bg="white",fg="red")
    l3.place(x=645,y=230)

    balance=StringVar()
    bla=Entry(window,textvariable=balance,width=15,font=("comic sans ms",14,"bold"))
    bla.config(bg="white",fg="black")
    bla.place(x=615,y=270)
            
    try:
        mycursor.execute(query,args)
        res=mycursor.fetchall()
        messagebox.showinfo("RECORD FOUND", "Record founded successfully")
        accholder.set(str(res[0][1]))
        balance.set(res[0][10])
        
    except Error as error:
        print("Failed to fetch record into table {}".format(error))#print(error)
        messagebox.showinfo("ERROR",format(error))
    
    finally:
        print('Done')
        
    
down=True
def down():
    global down
    if down:
        var.set(str(cal.get_date()))
        cal.place(x=394,y=205,height=200,width=200)
        down=False
    else:
        var.set(str(cal.get_date()))
        cal.place(x=0,y=0,height=0,width=0)
        down=True

def new():
    new["state"]=DISABLED
    save["state"]=NORMAL
    
    var1.set("")
    var2.set("")
    var.set("")
    rup.focus()

def exi():
    window.destroy()
    os.system('DashBoard.py')

#heading
l1=Label(window,text="   DEPOSIT   ",font=("comic sans ms",28,"bold"))    
l1.config(bg="white",fg="red")
l1.place(x=280,y=20)

#Acc no.
l2=Label(window,text="Account Number",font=("comic sans ms",16,"bold"))    
l2.config(bg="white",fg="red")
l2.place(x=70,y=120)
fetchacno()


#Rupees In Word
l3=Label(window,text="Rupees In Word",font=("comic sans ms",16,"bold"))    
l3.config(bg="white",fg="red")
l3.place(x=70,y=220)

var1=StringVar()
rup=Entry(window,textvariable=var1,width=15,font=("comic sans ms",14,"bold"))
rup.config(bg="white",fg="black")
rup.place(x=400,y=220)


#Rupees
l4=Label(window,text="Rupees",font=("comic sans ms",16,"bold"))    
l4.config(bg="white",fg="red")
l4.place(x=70,y=270)

var2=StringVar()
rupe=Entry(window,textvariable=var2,width=15,font=("comic sans ms",14,"bold"))
rupe.config(bg="white",fg="black")
rupe.place(x=400,y=270)


#button
#new
new=Button(window,text="New",width=0,height=0,font=("comic sans ms",12,"bold"),command=new)
new.config(bg="white",fg="black")
new.place(x=170,y=340)

#save
save=Button(window,text="Save",width=0,height=0,font=("comic sans ms",12,"bold"),command=saveindb,state=DISABLED)
save.config(bg="white",fg="black")
save.place(x=340,y=340)

#exit
exi=Button(window,text="Exit",width=0,height=0,font=("comic sans ms",12,"bold"),command=exi)
exi.config(bg="white",fg="black")
exi.place(x=500,y=340)

#Show Detail
exi=Button(window,text="Show Detail",width=0,height=0,font=("comic sans ms",8,"bold"),command=showacc)
exi.config(bg="white",fg="black")
exi.place(x=435,y=140)

#calendar
l11=Label(window,text="Date Of Deposit",width=0,height=0,font=("comic sans ms",14,"bold"))
l11.config(bg="white",fg="red")
l11.place(x=70,y=170)

var=StringVar()
l12=Label(window,textvariable=var,width=15,height=0,font=("comic sans ms",14,"bold"))
l12.config(bg="white")
l12.place(x=400,y=170)

cal=Calendar(window,selectmode="day",year=2022,month=1,day=6)
bc1=Button(window,text="⏬",width=0,height=0,command=down)
bc1.config(bg="white")
bc1.place(x=555,y=175) 

window.mainloop()

