from tkinter import *
import tkinter as tk
import os
from tkinter import messagebox
from PIL import ImageTk, Image

window=Tk()
window.title("Dashboard")
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
w=sw-500
h=sh-200
wpos=(sw/2)-(w/2)
hpos=(sh/2)-(h/2)
window.geometry("%dx%d"%(sw,sh))

#bgimage
bg=ImageTk.PhotoImage(file="Image\\dash.jpg")
back=Label(image=bg)
back.place(x=-2,y=-2)

#heading
l1=Label(window,text="   DASHBOARD   ",font=("comic sans ms",28,"bold"))    
l1.config(bg="white",fg="red")
l1.place(x=610,y=25)


def addacc():
    window.destroy()
    os.system('AddAccount.py')

def viewacc():
    window.destroy()
    os.system('ViewAccount.py')
   
def deposit():
    window.destroy()
    os.system('deposit.py')

def withdrawal():
    window.destroy()
    os.system('withdrawal.py')

def closeacc():
    window.destroy()
    os.system('CloseAccount.py')

def close():
    window.destroy()


#add Account
img1=ImageTk.PhotoImage(file="Image\\add_user.png")
add=Label(image=img1)
add.place(x=260,y=190)
b1=Button(window,text="Add Account",width=0,height=0,font=("comic sans ms",14,"bold"),command=addacc)
b1.config(bg="white",fg="black")
b1.place(x=258,y=330)

#view Account
img2=ImageTk.PhotoImage(file="Image\\view_cust.png")
add1=Label(image=img2)
add1.place(x=710,y=190)
b2=Button(window,text="View Account",width=0,height=0,font=("comic sans ms",14,"bold"),command=viewacc)
b2.config(bg="white",fg="black")
b2.place(x=706,y=330)

#Deposit
img3=ImageTk.PhotoImage(file="Image\\deposit (1).png")
add2=Label(image=img3)
add2.place(x=1150,y=190)
b3=Button(window,text="Deposit",width=0,height=0,font=("comic sans ms",14,"bold"),command=deposit)
b3.config(bg="white",fg="black")
b3.place(x=1170,y=330)

#withdrawal
img4=ImageTk.PhotoImage(file="Image\\cash-withdrawal.png")
add3=Label(image=img4)
add3.place(x=260,y=450)
b4=Button(window,text="Withdrawal",width=0,height=0,font=("comic sans ms",14,"bold"),command=withdrawal)
b4.config(bg="white",fg="black")
b4.place(x=267,y=590)

#close account
img5=ImageTk.PhotoImage(file="Image\\closeaccount.png")
add4=Label(image=img5)
add4.place(x=710,y=450)
b5=Button(window,text="Close Account",width=0,height=0,font=("comic sans ms",14,"bold"),command=closeacc)
b5.config(bg="white",fg="black")
b5.place(x=703,y=590)

#close
img6=ImageTk.PhotoImage(file="Image\\close.png")
add5=Label(image=img6)
add5.place(x=1150,y=450)
b6=Button(window,text="Close",width=0,height=0,font=("comic sans ms",14,"bold"),command=close)
b6.config(bg="white",fg="black")
b6.place(x=1185,y=590)

window.mainloop()
