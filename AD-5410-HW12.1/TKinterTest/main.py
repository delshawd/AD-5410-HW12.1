
#!/usr/bin/python3
from tkinter import *

canvas = None

def redBG():
    global canvas
    canvas.configure(bg="red")

def drawShape():
    global canvas
    canvas.create_oval(10,10,100,100, fill='blue')

def clear():
    global canvas
    canvas.delete("all")
    canvas.configure(bg="white")

def main():
    global canvas
    parent = Tk()
    canvas = Canvas(parent, bg='white')
    canvas.pack(side=TOP)
    redbutton = Button(parent, text="Red", fg="red", command=redBG)
    redbutton.pack(side=LEFT)
    greenbutton = Button(parent, text="Black", fg="black")
    greenbutton.pack(side=RIGHT)
    bluebutton = Button(parent, text="Blue", fg="blue", command=drawShape)
    bluebutton.pack(side=TOP)
    blackbutton = Button(parent, text="Green", fg="green", command=clear)
    blackbutton.pack(side=BOTTOM)
    parent.mainloop()


if __name__ == "__main__":
    main()
