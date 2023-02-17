from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk()  #สร้างหน้าจอ
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')

#B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
#B1.pack(ipadx=20,ipady=20)

L1 = Label(GUI,text='KM Program',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

#######################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู๋ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)


FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท2',command=Button2)
B2.pack(ipadx=20,ipady=20)

#######################
def Button3():
    text = 'Python 101'
    messagebox.showinfo('เงินในบัญชี',text)


FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=50,y=180)
B3 = ttk.Button(FB1,text='สัปห์ดานี้เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)



GUI.mainloop()

