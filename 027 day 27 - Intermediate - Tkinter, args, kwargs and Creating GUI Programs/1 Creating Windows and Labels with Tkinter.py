import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I am Label", font=("Arial", 24, "italic"))
#my_label.pack(expand=True)
my_label.pack()

import turtle

tim = turtle.Turtle()
tim.write()


window.mainloop()