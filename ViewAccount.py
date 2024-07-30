from tkinter import *
from tkinter.filedialog import asksaveasfile,askopenfile
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from tkinter import messagebox
import os
import sys
from tkinter.ttk import *


window=Tk()
window.title("View Account")
window.config(bg="skyblue")
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
w=sw-500
h=sh-200
wpos=(sw/2)-(w/2)
hpos=(sh/2)-(h/2)
window.geometry("%dx%d"%(sw,sh))

mydb=mysql.connector.connect(host='localhost',
                             database='bankdb',
                             user='root',
                             password='root',
                             charset='utf8')

mycursor=mydb.cursor()

def showall():
    class A(Frame):
        def __init__(self, parent):
            Frame.__init__(self, parent)
            self.CreateUI()
            self.LoadTable()
            self.grid(sticky=(N, S, W, E))
            parent.grid_rowconfigure(0, weight=1)
            parent.grid_columnconfigure(0, weight=1)
        def CreateUI(self):
            tv= Treeview(self)
            tv['columns']=('','Account_no','Account_holder','ifsc','Branch','Address','dob','Gender','email','Photo','Verify','Balance')
            tv.heading('#1',text='Account_no',anchor='center')
            tv.column('#1',anchor='center')
            tv.heading('#2', text='Account_holder', anchor='center')
            tv.column('#2', anchor='center')
            tv.heading('#3', text='ifsc', anchor='center')
            tv.column('#3', anchor='center')
            tv.heading('#4', text='Branch', anchor='center')
            tv.column('#4', anchor='center')
            tv.heading('#5', text='Address', anchor='center')
            tv.column('#5', anchor='center')
            tv.heading('#6', text='dob', anchor='center')
            tv.column('#6', anchor='center')
            tv.heading('#7', text='Gender', anchor='center')
            tv.column('#7', anchor='center')
            tv.heading('#8', text='email', anchor='center')
            tv.column('#8', anchor='center')
            tv.heading('#9', text='Photo', anchor='center')
            tv.column('#9', anchor='center')
            tv.heading('#10', text='Verify', anchor='center')
            tv.column('#10', anchor='center')
            tv.heading('#11', text='Balance', anchor='center')
            tv.column('#11', anchor='center')

            tv.grid(sticky=(N,S,W,E))
            self.treeview = tv
            self.grid_rowconfigure(0,weight=1)
            self.grid_columnconfigure(0,weight=1)
        def LoadTable(self):
            Select="Select * from banktb"
            mycursor.execute(Select)
            result=mycursor.fetchall()
            Account_no=""
            Account_holder=""
            ifsc=""
            Branch=""
            Address=""
            dob=""
            Gender=""
            email=""
            Photo=""
            Verify=""
            Balance=""
            for i in result:
                Account_no=i[0]
                Account_holder=i[1]
                ifsc=i[2]
                Branch=i[3]
                Address=i[4]
                dob=i[5]
                Gender=i[6]
                email=i[7]
                Photo=i[8]
                Verify=i[9]
                Balance=i[10]
                
                self.treeview.insert("",'end',values=(Account_no,Account_holder,ifsc,Branch,Address,dob,Gender,email,Photo,Verify,Balance))
    A(window)
          
#SHOW ALLDATA
new=Button(window,text="Show All Data",command=showall)
new.place(x=200,y=700)

window.mainloop()
