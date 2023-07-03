from tkinter import *

def click(num):
    global eq
    eq = eq + str(num)
    equation.set(eq)
def clear():
    global eq
    eq = "0"
    equation.set("0")

def equals():
    global eq
    try:
        equation.set(eval(eq))
        eq = str(eval(eq))

    except ZeroDivisionError:
        equation.set("ERROR")
        eq = ""

    except SyntaxError:
        equation.set("ERROR")
        eq = ""

window = Tk()

window.title("Calculator")
window.geometry("500x500")
icon = PhotoImage(file = 'logo.png')
window.iconphoto(True,icon)
window.config(background="#ebc5bc")

eq = ""
equation = StringVar()

label = Label(window,textvariable = equation , font = ('Arial' , 20) , bg = "#ebc5bc" , width = 32 , height = 2)
label.pack()

frame = Frame(window)
frame.pack()

#Number Buttons:
btn9 = Button(frame,text="9" ,activebackground="green" ,  command = lambda: click(9) , height = 4 , width = 8 , font = 20,background ="grey")
btn8 = Button(frame,text="8" ,activebackground="green" , command = lambda: click(8), height = 4 , width = 8, font = 20,background ="grey")
btn7 = Button(frame,text="7" ,activebackground="green" , command = lambda: click(7), height = 4 , width = 8, font = 20,background ="grey")
btn6 = Button(frame,text="6" ,activebackground="green" , command = lambda: click(6), height = 4 , width = 8, font = 20,background ="grey")
btn5 = Button(frame,text="5",activebackground="green" , command = lambda: click(5), height = 4 , width = 8, font = 20,background ="grey")
btn4 = Button(frame,text="4",activebackground="green" , command = lambda: click(4), height = 4 , width = 8, font = 20,background ="grey")
btn3 = Button(frame,text="3",activebackground="green" , command = lambda: click(3), height = 4 , width = 8, font = 20,background ="grey")
btn2 = Button(frame,text="2",activebackground="green" , command = lambda: click(2), height = 4 , width = 8, font = 20,background ="grey")
btn1 = Button(frame,text="1" ,activebackground="green", command = lambda: click(1), height = 4 , width = 8, font = 20,background ="grey")
btn0 = Button(frame,text="0" ,activebackground="green", command = lambda: click(0), height = 4 , width = 8, font = 20,background ="grey")

#Operation Buttons:
plus = Button(frame,text = "+",activebackground="green" , command = lambda: click("+"), height = 4 , width = 8, font = 20,background = "orange")
minus = Button(frame , text ="-" ,activebackground="green", command = lambda: click("-"), height = 4 , width = 8, font = 20,background = "orange")
multiply = Button(frame , text ="*" ,activebackground="green", command = lambda: click("*"), height = 4 , width = 8, font = 20,background = "orange")
divide = Button(frame , text ="/" ,activebackground="green", command = lambda: click("/"), height = 4 , width = 8, font = 20,background = "orange")
clear = Button(window , text="CE" ,activebackground="red", command =  clear, height = 4 , width = 8, font = 20,background = "orange")
equal = Button(frame , text = "=" ,activebackground="green", command =  equals, height = 4 , width = 8, font = 20,background = "orange")
comma = Button(frame,text = "." ,activebackground="green", command = lambda: click(".") , height = 4 , width = 8, font = 20,background = "orange")

btn9.grid(row = 0,column=0)
btn8.grid(row = 0,column=1)
btn7.grid(row = 0,column=2)
plus.grid(row = 0,column=3)

btn6.grid(row = 1,column=0)
btn5.grid(row = 1,column=1)
btn4.grid(row = 1,column=2)
minus.grid(row = 1,column=3)

btn3.grid(row = 2,column=0)
btn2.grid(row = 2,column=1)
btn1.grid(row = 2,column=2)
multiply.grid(row = 2,column=3)

comma.grid(row = 3,column=0)
btn0.grid(row = 3,column=1)
divide.grid(row = 3,column=3)
equal.grid(row = 3,column=2)

clear.pack()

window.mainloop()