from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Lesson two")

photo = PhotoImage(file="C:\\Users\\DELL\\Pictures\\person.png")

label = Label(window, text="Hello world",
              font=("Arial",40,"bold"),
              fg='green',
              bg='black',
              relief=RAISED,
              bd= 10,
              padx=10,
              pady=10,
              image=photo,
              compound='bottom')

#place at cordinate
#label.place(x=100,y=100)
# places at the center
label.pack()

window.mainloop()