import sys
from tkinter import *

#def clear():
    	#txtDisplay.delete(0,END)
		#return






#create a window
window=Tk()
window.title("calculator")
#window.geometry('400x200')


#for textbox
num1=StringVar()
frame0=Frame(window)
frame0.pack(side=TOP)
txtDisplay=Entry(frame0,textvariable=num1, bd=1, font=10)
txtDisplay.pack(side=TOP)

#buttons
frame1=Frame(window)
frame1.pack(side=TOP)

btn1=Button(frame1,text="1",padx=20,pady=16,bd=1,)
btn1.pack(side=LEFT)

def clicked():
    	txtDisplay.configure(text="manish")
	
	
btn2=Button(frame1,text="click me",padx=20,pady=16,bd=1,command=clicked)
btn2.pack(side=LEFT)
btn3=Button(frame1,text="3",padx=20,pady=16,bd=1)
btn3.pack(side=LEFT)
btn4=Button(frame1,text="4",padx=20,pady=16,bd=1)
btn4.pack(side=LEFT)

frame2=Frame(window)
frame2.pack(side=TOP)


btn5=Button(frame2,text="5",padx=20,pady=16,bd=1)
btn5.pack(side=LEFT)
btn6=Button(frame2,text="6",padx=20,pady=16,bd=1)
btn6.pack(side=LEFT)
btn7=Button(frame2,text="7",padx=20,pady=16,bd=1)
btn7.pack(side=LEFT)
btn8=Button(frame2,text="8",padx=20,pady=16,bd=1)
btn8.pack(side=LEFT)

frame3=Frame(window)
frame3.pack(side=TOP)

btn9=Button(frame3,text="9",padx=20,pady=16,bd=1)
btn9.pack(side=LEFT)
btn9=Button(frame3,text="0",padx=20,pady=16,bd=1)
btn9.pack(side=LEFT)


btn9=Button(frame3,text="c",padx=20,pady=16,bd=1)
btn9.pack(side=LEFT)
btn9=Button(frame3,text="=",padx=20,pady=16,bd=1)
btn9.pack(side=LEFT)

frame4=Frame(window)
frame4.pack(side=TOP)

btn9=Button(frame4,text="*",padx=20,pady=16,bd=1)
btn9.pack(side=LEFT)
btn9=Button(frame4,text="/",padx=20,pady=16,bd=1)
btn9.pack(side=LEFT)
btn9=Button(frame4,text="-",padx=20,pady=16,bd=1)
btn9.pack(side=LEFT)
btn9=Button(frame4,text="+",padx=20,pady=16,bd=1)
btn9.pack(side=LEFT)

window.mainloop()