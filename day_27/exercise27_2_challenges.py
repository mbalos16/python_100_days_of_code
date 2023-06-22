# Exercise27.2 Challenges

# Instructions:
# Show "button got clicked" on my_label when the button get's clicked.
# Show imput on my_label when the button get's clicked.

import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=600, height=400)


def click():
    # my_label.config(text="Button got clicked")
    my_label.config(text=input.get())
    

# label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column = 0, row = 0)


# button
my_button = tkinter.Button(text="Click me", command=click)
my_button.grid(column = 1, row = 1)


# button TWO
my_new_button = tkinter.Button(text="New button", command=click)
my_new_button.grid(column = 2, row = 0)


# entry
# Just allows one line of text
input = tkinter.Entry(width=10)
input.grid(column = 3, row = 2)







window.mainloop()