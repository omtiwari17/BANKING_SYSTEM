from  tkinter import *
import time
import os
from tkinter.ttk import Progressbar
from PIL import ImageTk, Image

window=Tk()
window.title("Bank")
window.config(bg='Skyblue')
rw=630
rh=390
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
wpos=(sw/2)-(rw/2)
hpos=(sh/2)-(rh/2)
window.geometry("%dx%d+%d+%d"%(rw,rh,wpos,hpos))
window.maxsize(1000,800)
window.minsize(400,200)

bg=ImageTk.PhotoImage(file="Image\\Bank1.jpg")
bgl=Label(window,image=bg)
bgl.place(x=0,y=0)

p=Progressbar(window,orient=HORIZONTAL,length=100,mode='determinate',value=0)
p.place(x=240,y=360)

def display():
    for i in range(1,11):
        window.update_idletasks()
        p['value']+=10
        time.sleep(0.5)
        L['text']=p['value'],'%'
    window.destroy()
    os.system("Login.py")

l1=Label(window,text="Bank",width=0,height=0,font=('Comic Sans Ms',10,"bold"))
l1.config(bg="white",fg="red")
l1.place(x=300,y=125)

L=Label(window,width=0,height=0,font=('Comic Sans Ms',10,"bold"))
L.config(bg="white",fg="black")
L.place(x=350,y=360)

display()

window.mainloop()

