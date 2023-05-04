from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Day/Night window")

state = True

def switch():
    global state
    if state:
        lab.config(text='Night Mode')
        btn.config(image=off)
        lab.config(fg='black')
        state = False
    else:
        lab.config(text='Day Mode')
        btn.config(image=on)
        lab.config(fg='green')
        state = True


lab = Label(root, text='Day mode', font=('Arial', 20), fg='green')
lab.pack(pady=20)

on = PhotoImage(file='img/wifi/on.png')
off = PhotoImage(file='img/wifi/off.png')


btn = Button(root, text='Click Me', image=on, bd=0, command=switch)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
mainloop()