from tkinter import *
root=Tk()
root.title("Simple Calculator")

#building the display
e=Entry(root,width=47,borderwidth=10)
e.grid(row=0,column=0,columnspan=4,ipadx=10,ipady=10)

#defining the functions
def click_button(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def reset():
    e.delete(0,END)

def button_add():
    num=e.get()
    global x
    global math
    math="add"
    x=int(num)
    e.delete(0,END)

def button_sub():
    num=e.get()
    global x
    global math
    math="sub"
    x=int(num)
    e.delete(0,END)

def button_mul():
    num=e.get()
    global x
    global math
    math="mul"
    x=int(num)
    e.delete(0,END)

def button_div():
    num=e.get()
    global x
    global math
    math="div"
    x=int(num)
    e.delete(0,END)

def button_equals():
    y=e.get()
    e.delete(0,END)
    if math == "add":
        e.insert(0,x+int(y))
    if math == "sub":
        e.insert(0,x+int(y))
    if math == "mul":
        e.insert(0,x*int(y))
    if math == "div":
        e.insert(0,x/int(y))


#defining the buttons

button1=Button(root,text="1",padx=30,pady=15,command=lambda: click_button(1))
button2=Button(root,text="2",padx=30,pady=15,command=lambda: click_button(2))
button3=Button(root,text="3",padx=30,pady=15,command=lambda: click_button(3))
button4=Button(root,text="4",padx=30,pady=15,command=lambda: click_button(4))
button5=Button(root,text="5",padx=30,pady=15,command=lambda: click_button(5))
button6=Button(root,text="6",padx=30,pady=15,command=lambda: click_button(6))
button7=Button(root,text="7",padx=30,pady=15,command=lambda: click_button(7))
button8=Button(root,text="8",padx=30,pady=15,command=lambda: click_button(8))
button9=Button(root,text="9",padx=30,pady=15,command=lambda: click_button(9))
button_add=Button(root,text="+",padx=30,pady=15,bg="cyan",command=button_add)
button_sub=Button(root,text="-",padx=30,pady=15,bg="cyan",command=button_sub)
button_mul=Button(root,text="*",padx=30,pady=15,bg="cyan",command=button_mul)
button_div=Button(root,text="/",padx=30,pady=15,bg="cyan",command=button_div)
button_equals=Button(root,text="=",padx=30,pady=15,bg="cyan",command=button_equals)
button_reset=Button(root,text="Reset",padx=19,pady=15,bg="cyan",command=reset)
button0=Button(root,text="0",padx=30,pady=15,command=lambda: click_button(0))




#building the buttons on screen

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_add.grid(row=1,column=3)
button_sub.grid(row=2,column=3)
button_mul.grid(row=3,column=3)
button_div.grid(row=4,column=3)
button_equals.grid(row=4,column=2)
button_reset.grid(row=4,column=1)
button0.grid(row=4,column=0)






root.mainloop()