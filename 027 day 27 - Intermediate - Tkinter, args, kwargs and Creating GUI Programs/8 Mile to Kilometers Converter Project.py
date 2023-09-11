#teacher answer

from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to kilometer converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column= 1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column= 2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column= 0,row=1)

kilometer_result_label = Label(text='0')
kilometer_result_label.grid(column= 1,row=1)

kilometer_label = Label(text='km')
kilometer_label.grid(column=2,row=1)

calculate_button = Button(text='Calculate', command=miles_to_km)
calculate_button.grid(column= 1,row=2)


window.mainloop()




# my answer
"""
from tkinter import *


def button_clicked():
    print("I got clicked")
    miles_convert = 0.62137119
    new_text = input.get()
    new_text = int(new_text)/miles_convert
    results.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=200, height=150)
window.config(padx=10, pady=10)

#Label
my_label = Label(text="is equal to")
my_label.grid(column=0, row=1)

results = Label(text="0")
results.grid(column=1, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)


#Button
button = Button(text="calculate", command=button_clicked)
button.grid(column=1, row=2)


#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)






window.mainloop()
"""