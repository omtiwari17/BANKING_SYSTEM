from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import sys
from tkinter import ttk

window=Tk()
window.title("CLOSE ACCOUNT")
window.config(bg="skyblue")
w=window.winfo_screenwidth()-800
h=window.winfo_screenheight()-450
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
wpos=(sw/2)-(w/2)
hpos=(sh/2)-(h/2)
window.geometry("%dx%d+%d+%d"%(w,h,wpos,hpos))
window.maxsize(1000,800)
window.minsize(400,200)

py=sys.executable
mydb = mysql.connector.connect(host='localhost',
                                         database='bankdb',
                                         user='root',
                                         password='root',
                                         charset='utf8')
mycursor=mydb.cursor()

accno1=''
abc=StringVar()

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
        month_cb.place(x=435,y=150)
     
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
    accholder=StringVar()
    l2=Label(window,text="Account Holder Name:-",font=("comic sans ms",14,"bold"))    
    l2.config(bg="white",fg="red")
    l2.place(x=115,y=230)
    
    rupe=Entry(window,textvariable=accholder,width=15,font=("comic sans ms",14,"bold"))
    rupe.config(bg="white",fg="black")
    rupe.place(x=130,y=270)       
    
    #Balance
    l3=Label(window,text="Balance:-",font=("comic sans ms",14,"bold"))    
    l3.config(bg="white",fg="red")
    l3.place(x=470,y=230)

    balance=StringVar()
    bla=Entry(window,textvariable=balance,width=15,font=("comic sans ms",14,"bold"))
    bla.config(bg="white",fg="black")
    bla.place(x=435,y=270)
        
    
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

def Delete():
    Accno=abc.get()
    Delete="delete from banktb where Account_no='%s'" %(Accno)
    mycursor.execute(Delete)
    mydb.commit()
    messagebox.showinfo("Information","ACCOUNT CLOSED")
   
def exi():
    window.destroy()
    os.system('DashBoard.py')

#heading
l1=Label(window,text="   CLOSE ACCOUNT   ",font=("comic sans ms",28,"bold"))    
l1.config(bg="white",fg="red")
l1.place(x=160,y=10)

#account no
l1=Label(window,text="Enter Your Account Number",font=("comic sans ms",16,"bold"))    
l1.config(bg="white",fg="red")
l1.place(x=85,y=140)

fetchacno()

#button
#Show Detail
exi=Button(window,text="Show Detail",width=0,height=0,font=("comic sans ms",8,"bold"),command=showacc)
exi.config(bg="white",fg="black")
exi.place(x=455,y=175)

#close
close=Button(window,text="Close Account",width=0,height=0,font=("comic sans ms",12,"bold"),command=Delete)
close.config(bg="white",fg="black")
close.place(x=210,y=340)

#Exit
exi=Button(window,text="Exit",width=0,height=0,font=("comic sans ms",12,"bold"),command=exi)
exi.config(bg="white",fg="black")
exi.place(x=449,y=340)

window.mainloop()
