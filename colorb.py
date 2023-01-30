import tkinter as tk

def change_bg(color):
    frame.config(bg=color)

root = tk.Tk()
frame = tk.Frame(root, bg="white", width=1280, height=720)
frame.pack()

red_button = tk.Button(root, text="Red", command=lambda: change_bg("red"))
red_button.pack(pady=5)

green_button = tk.Button(root, text="Green", command=lambda: change_bg("green"))
green_button.pack(pady=5)

blue_button = tk.Button(root, text="Blue", command=lambda: change_bg("blue"))
blue_button.pack(pady=5)

root.mainloop()




















#mport tkinter as tk


#def change_bg(widget):
#    widget['bg'] = 'medium sea green'


#if __name__ == '__main__':
#    root = tk.Tk()

#    frame = tk.Frame(root, height=720, width=1280)
#    button = tk.Button(root, text="Paint")
#    button['command'] = lambda wgt=frame : change_bg(wgt)

#    frame.pack()
#    button.pack()
#
#    root.mainloop()


























#from tkinter import *

#Import the required libraries
#from tkinter import *

#def change_bg(widget):
#    widget['bg'] = 'cyan'

#Create an instance of tkinter frame
#win= Tk()

#Set the geometry of frame
#win.geometry("1366x768")
#win.configure(bg='yellow')
#win.resizable(False, False)

#Button(win, text="cyan",height= 15, width=30,fg='orange',bg='cyan').pack()
#Button(win, text="green",height=15, width=30,fg='red',bg='green').pack()
#Button(win, text= "purple",height=15, width=30,fg='blue',bg='purple').pack()

#win.mainloop()




#parent = Tk()
#parent.configure(bg='yellow')
#parent.geometry('1366x768')
#button1 = Button(parent, text = 'Hello There', fg='red', bg='cyan' )
#button1(parent,text="General kenobi",height=15.width=30).pack()
#parent.mainloop()