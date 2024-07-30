from tkinter import *
from tkinter.filedialog import asksaveasfile,askopenfile
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

window=Tk()
window.title("Add Account")
window.config(bg="skyblue")
w=window.winfo_screenwidth()-700
h=window.winfo_screenheight()-180
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

imgpath=""
def saveindb():
    new["state"]=NORMAL
    save["state"]=NORMAL
    update["state"]=NORMAL
    delete["state"]=NORMAL
    search["state"]=NORMAL
    Account_novar=accno.get()
    Account_holdervar=accholder.get()
    ifscvar=ifsc.get()
    Branchvar=branch.get()
    Addressvar=address.get()
    dobvar=var.get()
    Gendervar=var7.get()
    emailvar=email.get()
    Verifyvar=verify.get()
    Balancevar=balance.get()
    query = "INSERT INTO banktb(Account_no,Account_holder,ifsc,Branch,Address,dob,Gender,email,Verify,Balance,Photo) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    args = (Account_novar,Account_holdervar,ifscvar,Branchvar,Addressvar,dobvar,Gendervar,emailvar,Verifyvar,Balancevar,imgpath)
    
    try:
        mycursor.execute(query,args)
        mydb.commit()
        messagebox.showinfo("SUCCESSFULLY INSERTED", "Record inserted successfully")

    except Error as error:
        print("Failed to insert record into table {}".format(error))#print(error)
        messagebox.showinfo("ERROR",format(error))
    finally:
        print('Done')
 
def acc():
    l=[]
    mycursor.execute("select * from banktb")
    print(type(Mydata))
    for i in range(0,mycursor.rowcount):
        l.append(r[i][0])
    return l[len(l)-1]

acc()

#dropdown
def gender(event):
    option=var7.get()
    Gender= Label(window,text=option)

def saver():
    files = [('All Files', '*.jpg'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = askopenfile(filetypes = files, defaultextension = files)
    image=Image.open(file.name)
    img2=image
    image=image.resize((100, 100), Image.ANTIALIAS)
    img2.save("dbphoto\\" + str(var1)+ ".jpg")

def photo():
    files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = askopenfile(filetypes = files, defaultextension = files)
    m.showinfo("file path",file.name)
    image2 =Image.open(file.name)
    img2=image2
    image2 = image2.resize((130, 150), Image.ANTIALIAS)
    im = ImageTk.PhotoImage(image2)
    panel = Label(window, image = im)
    panel.image = im
    panel.place(x=642,y=140)
    stt=var1.get()
    #print(stt)
    global imgpath
    imgpath="dbphoto\\" + stt+ ".png"
    img2.save(imgpath)
    

down=True
def down():
    global down
    if down:
        
        var.set(str(cal.get_date()))
        cal.place(x=370,y=405,height=245,width=245)
        down=False
            
    else:
        var.set(str(cal.get_date()))
        cal.place(x=0,y=0,height=0,width=0)
        down=True

    
def new():
    new["state"]=DISABLED
    save["state"]=NORMAL
    var.set("")
    var1.set("")
    var2.set("")
    var3.set("")
    var4.set("")
    var5.set("")
    var7.set("Gender")
    var8.set("")
    var9.set("")
    var10.set("")
    accno.focus()
    
    
def search():
    search["state"]=DISABLED
    delete["state"]=NORMAL
    update["state"]=NORMAL
    Account_novar=accno.get()
    
    query = "SELECT * from banktb WHERE Account_no='%s' "  % (Account_novar,)
    
    try:
        mycursor.execute(query)
        result=mycursor.fetchall()
        var2.set(result[0][1])
        var3.set(result[0][2])
        var4.set(result[0][3])
        var5.set(result[0][4])
        var.set(result[0][5])
        var7.set(result[0][6])
        var8.set(result[0][7])
        var10.set(result[0][10])
        var9.set(result[0][9])

    except Error as error:
        print("Failed to found record {}".format(error))#print(error)
        messagebox.showinfo("ERROR",format(error))
    finally:
        print('Done')

    
def update():
    update["state"]=NORMAL
    Account_novar=accno.get()
    Account_holdervar=accholder.get()
    ifscvar=ifsc.get()
    Branchvar=branch.get()
    Addressvar=address.get()
    dobvar=var.get()
    Gendervar=var7.get()
    emailvar=email.get()
    Verifyvar=verify.get()
    Balancevar=balance.get()
    
    query = "update banktb set Account_holder=%s,ifsc=%s,Branch=%s,Address=%s,dob=%s,Gender=%s,email=%s,Verify=%s,Balance=%s where Account_no=%s"
    args = (Account_holdervar,ifscvar,Branchvar,Addressvar,dobvar,Gendervar,emailvar,Verifyvar,Balancevar,Account_novar)

    try:
        mycursor.execute(query,args)
        mydb.commit()
        messagebox.showinfo("SUCCESSFULLY UPDATED", "Record updated successfully")

    except Error as error:
        print("Failed to insert record into table {}".format(error))#print(error)
        messagebox.showinfo("ERROR",format(error))
    
    finally:
        print('Done')

    
def delete():
    delete["state"]=NORMAL
    Account_novar=accno.get()
    Account_holdervar=accholder.get()
    ifscvar=ifsc.get()
    Branchvar=branch.get()
    Addressvar=address.get()
    dobvar=var.get()
    Gendervar=var7.get()
    emailvar=email.get()
    Verifyvar=verify.get()
    Balancevar=balance.get()
    
    query = "delete from banktb where Account_no='%s' "
    args = (Account_holdervar,ifscvar,Branchvar,Addressvar,dobvar,Gendervar,emailvar,Verifyvar,Balancevar,Account_novar)

    try:
        mycursor.execute(query,args)
        mydb.commit()
        messagebox.showinfo("SUCCESSFULLY UPDATED", "Record updated successfully")

    except Error as error:
        print("Failed to insert record into table {}".format(error))#print(error)
        messagebox.showinfo("ERROR",format(error))
    finally:
        print('Done')


def exi():
    window.destroy()
    os.system('DashBoard.py')

#heading
l1=Label(window,text="   ADD ACCOUNT   ",font=("comic sans ms",28,"bold"))    
l1.config(bg="white",fg="red")
l1.place(x=250,y=10)


#acc number
l2=Label(window,text="Account Number",font=("comic sans ms",16,"bold"))    
l2.config(bg="white",fg="red")
l2.place(x=70,y=120)

var1=StringVar()
accno=Entry(window,textvariable=var1,width=15,font=("comic sans ms",14,"bold"))
accno.config(bg="white",fg="black")
accno.place(x=400,y=120)

#acc holder name
l3=Label(window,text="Account Holder Name",font=("comic sans ms",16,"bold"))    
l3.config(bg="white",fg="red")
l3.place(x=70,y=170)

var2=StringVar()
accholder=Entry(window,textvariable=var2,width=15,font=("comic sans ms",14,"bold"))
accholder.config(bg="white",fg="black")
accholder.place(x=400,y=170)

#ifsc
l4=Label(window,text="IFSC Code",font=("comic sans ms",16,"bold"))    
l4.config(bg="white",fg="red")
l4.place(x=70,y=220)

var3=StringVar()
ifsc=Entry(window,textvariable=var3,width=15,font=("comic sans ms",14,"bold"))
ifsc.config(bg="white",fg="black")
ifsc.place(x=400,y=220)

#Branch
l5=Label(window,text="Branch",font=("comic sans ms",16,"bold"))    
l5.config(bg="white",fg="red")
l5.place(x=70,y=270)

var4=StringVar()
branch=Entry(window,textvariable=var4,width=15,font=("comic sans ms",14,"bold"))
branch.config(bg="white",fg="black")
branch.place(x=400,y=270)

#address
l6=Label(window,text="Address",font=("comic sans ms",16,"bold"))    
l6.config(bg="white",fg="red")
l6.place(x=70,y=320)

var5=StringVar()
address=Entry(window,textvariable=var5,width=15,font=("comic sans ms",14,"bold"))
address.config(bg="white",fg="black")
address.place(x=400,y=320)

#Gender
l8=Label(window,text="Gender",font=("comic sans ms",16,"bold"))    
l8.config(bg="white",fg="red")
l8.place(x=70,y=420)

var7=StringVar(window)
var7.set("Gender")
drop=OptionMenu(window,var7,"Male","Female","Other",command=gender)
drop.place(x=400,y=420)

#email
l9=Label(window,text="E-Mail",font=("comic sans ms",16,"bold"))    
l9.config(bg="white",fg="red")
l9.place(x=70,y=470)

var8=StringVar()
email=Entry(window,textvariable=var8,width=15,font=("comic sans ms",14,"bold"))
email.config(bg="white",fg="black")
email.place(x=400,y=470)

#Verify
l10=Label(window,text="Verify",font=("comic sans ms",16,"bold"))    
l10.config(bg="white",fg="red")
l10.place(x=70,y=520)

var9=StringVar()
verify=Entry(window,textvariable=var9,width=15,font=("comic sans ms",14,"bold"))
verify.config(bg="white",fg="black")
verify.place(x=400,y=520)

#Balance
l13=Label(window,text="Balance",font=("comic sans ms",16,"bold"))    
l13.config(bg="white",fg="red")
l13.place(x=70,y=570)

var10=StringVar()
balance=Entry(window,textvariable=var10,width=15,font=("comic sans ms",14,"bold"))
balance.config(bg="white",fg="black")
balance.place(x=400,y=570)


#button
#Photo
btn = Button(window, text = 'Select Photo', command =photo)
btn.config(bg="white",fg="black")
btn.place(x=670,y=300)

#new
new=Button(window,text="New",width=0,height=0,font=("comic sans ms",12,"bold"),command=new)
new.config(bg="white",fg="black")
new.place(x=100,y=630)

#save
save=Button(window,text="Save",width=0,height=0,font=("comic sans ms",12,"bold"),command=saveindb,state=DISABLED)
save.config(bg="white",fg="black")
save.place(x=190,y=630)

#search
search=Button(window,text="SEARCH",width=0,height=0,font=("comic sans ms",12,"bold"),command=search)
search.config(bg="white",fg="black")
search.place(x=280,y=630)

#update
update=Button(window,text="Update",width=0,height=0,font=("comic sans ms",12,"bold"),command=update,state=DISABLED)
update.config(bg="white",fg="black")
update.place(x=400,y=630)

#delete
delete=Button(window,text="Delete",width=0,height=0,font=("comic sans ms",12,"bold"),command=delete,state=DISABLED)
delete.config(bg="white",fg="black")
delete.place(x=515,y=630)

#exit
exi=Button(window,text="Exit",width=0,height=0,font=("comic sans ms",12,"bold"),command=exi)
exi.config(bg="white",fg="black")
exi.place(x=620,y=630)

#calendar
l11=Label(window,text="Date Of Birth",width=0,height=0,font=("comic sans ms",16,"bold"))
l11.config(bg="white",fg="red")
l11.place(x=70,y=370)
       
var=StringVar()
l12=Label(window,textvariable=var,width=15,height=0,font=("comic sans ms",14,"bold"))
l12.config(bg="white")
l12.place(x=400,y=370)

cal=Calendar(window,selectmode="day",year=2021,month=10,day=21)
bc1=Button(window,text="⏬",width=0,height=0,command=down)
bc1.config(bg="white")
bc1.place(x=556,y=373) 

window.mainloop()

