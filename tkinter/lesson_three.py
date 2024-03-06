from tkinter import *

# button = you click it, then it does stuff

window = Tk()

def click():
    print("You clicked the button")

button = Button(window,
                text="click me!",
                command=click,
                font=("comic sans", 15),
                fg="white",
                bg='blue',
                activeforeground='white',
                activebackground="blue",
                state=DISABLED
                )

button.pack()

window.mainloop()