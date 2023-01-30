from tkinter import *

#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Set the geometry of frame
win.geometry("1366x768")
win.configure(bg='yellow')
win.resizable(False, False)

Button(win, text="cyan",height= 15, width=30,fg='orange',bg='cyan').pack()
Button(win, text="green",height=15, width=30,fg='red',bg='green').pack()
Button(win, text= "purple",height=15, width=30,fg='blue',bg='purple').pack()

win.mainloop()




#parent = Tk()
#parent.configure(bg='yellow')
#parent.geometry('1366x768')
#button1 = Button(parent, text = 'Hello There', fg='red', bg='cyan' )
#button1(parent,text="General kenobi",height=15.width=30).pack()
#parent.mainloop()