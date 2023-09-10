import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I am Label", font=("Arial", 24, "italic"))
#my_label.pack(expand=True)
my_label.pack(side="left")

import turtle

tim = turtle.Turtle()
tim.write("some text", font=("Time New Roma", 80, "bold"))








window.mainloop()