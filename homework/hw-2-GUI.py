from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

GUI = Tk()
GUI.title('โปรแกรมช่วยเลือกเมนูอาหาร')
GUI.geometry('500x400')

menu = ['ผัดกระเพรา','สุกี้','ข้าวผัด','พริกเผาหมูกรอบ','ขนมจีนน้ำเงี้ยว','ต้มยำ','ส้มตำ','ลดความอ้วน']


L1 = Label(GUI,text='วันนี้กินอะไรดี',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)
###############
def Button1():
    ans = random.choice(menu)
    messagebox.showinfo('มื้อนี้ขอแนะนำ :',ans)
    
FB1 = Frame(GUI)
FB1.place(x=100,y=80)
B1 = ttk.Button(FB1,text='สุ่มเมนู',command=Button1)
B1.pack(ipadx=20,ipady=20)


GUI.mainloop()
