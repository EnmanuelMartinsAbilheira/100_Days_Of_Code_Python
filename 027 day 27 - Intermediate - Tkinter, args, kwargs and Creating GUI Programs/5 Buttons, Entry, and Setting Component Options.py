from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="i am a label", font=("arial", 24,"bold"))
my_label.pack()
#my_label.pack(side="left")

#my_label.pack(expand=True)
my_label["text"] = "New Text"
my_label.config(text="New Text")


#Button

def button_clicked():
    print("i got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()



#Entry

input = Entry(width=10)
input.pack()
print(input.get())



window.mainloop()