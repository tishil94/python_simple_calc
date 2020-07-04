from tkinter import *

window=Tk()
window.title("Calculator")
window.configure(bg="#777")
e=Entry(window,width=33,borderwidth=5,font=5)
e.grid(row=0,column=0,columnspan=4,padx=8,pady=10,ipady=2)

def button_Click(number):
    text=e.get()
    e.delete(0,END)
    val=str(text)+str(number)
    e.insert(0,val)
def equal_Click():
    exp=e.get()
    res=eval(str(exp))
    e.delete(0,END)
    e.insert(0,res)

def clear_screen():
    e.delete(0,END)

def delete_fun():
    exp=str(e.get())
    val=exp[0:-1]
    e.delete(0,END)
    e.insert(0,val)



button1=Button(window,text="1",padx=28,pady=10,bg='#575050',fg='#E8E2E2',command=lambda: button_Click(1))
button2=Button(window,text="2",padx=28,pady=10,bg='#575050',fg='#E8E2E2',command=lambda: button_Click(2))
button3=Button(window,text="3",padx=28,pady=10,bg='#575050',fg='#E8E2E2',command=lambda: button_Click(3))
button4=Button(window,text="4",padx=28,pady=10,bg='#575050',fg='#E8E2E2',command=lambda: button_Click(4))
button5=Button(window,text="5",padx=28,pady=10,bg='#575050',fg='#E8E2E2',command=lambda: button_Click(5))
button6=Button(window,text="6",padx=28,pady=10,bg='#575050',fg='#E8E2E2',command=lambda: button_Click(6))
button7=Button(window,text="7",padx=28,pady=10,bg='#575050',fg='#E8E2E2',command=lambda: button_Click(7))
button8=Button(window,text="8",padx=28,pady=10,bg='#575050',fg='#E8E2E2',command=lambda: button_Click(8))
button9=Button(window,text="9",padx=28,pady=10,bg='#575050',fg='#E8E2E2',command=lambda: button_Click(9))
button0=Button(window,text="0",padx=28,pady=10,bg='#575050',fg='#E8E2E2',command=lambda: button_Click(0))
button_plus=Button(window,text="+",padx=24,pady=10,bg='#575050',fg='#E8E2E2',command=lambda: button_Click("+"))
button_min=Button(window,text="-",padx=25,pady=10,bg='#575050',fg='#E8E2E2',command=lambda: button_Click("-"))
button_mul=Button(window,text="x",padx=25,pady=10,bg='#575050',fg='#E8E2E2',command=lambda: button_Click("*"))
button_div=Button(window,text="/",padx=25,pady=10,bg='#575050',fg='#E8E2E2',command=lambda: button_Click("/"))
button_dot=Button(window,text=".",padx=29,pady=10,bg='#575050',fg='#E8E2E2',command=lambda: button_Click("."))
button_eq=Button(window,text="=",padx=27,pady=10,bg='#575050',fg='#E8E2E2',command=equal_Click)
button_C=Button(window,text="C",padx=24,pady=10,bg='#575050',fg='#E8E2E2',command=clear_screen)
button_del=Button(window,text="del",padx=23,pady=10,bg='#575050',fg='#E8E2E2',command=delete_fun)



button7.grid(row=2,column=0,pady=2)
button8.grid(row=2,column=1,pady=2)
button9.grid(row=2,column=2,pady=2)
button_div.grid(row=2,column=3,pady=2)



button4.grid(row=3,column=0,pady=2)
button5.grid(row=3,column=1,pady=2)
button6.grid(row=3,column=2,pady=2)
button_plus.grid(row=3,column=3,pady=2)


button1.grid(row=4,column=0,pady=2)
button2.grid(row=4,column=1,pady=2)
button3.grid(row=4,column=2,pady=2)
button_min.grid(row=4,column=3,pady=2)


button_dot.grid(row=5,column=0,pady=(2,30))
button0.grid(row=5,column=1,pady=(2,30))
button_eq.grid(row=5,column=2,pady=(2,30))
button_mul.grid(row=5,column=3,pady=(2,30))


button_del.grid(row=1,column=2,pady=2)
button_C.grid(row=1,column=3,pady=2)





window.mainloop()