from tkinter import *
from PIL import ImageTk


window = Tk()
window.geometry('800x500')

window.configure(background='#31361b')

def show():
    hide_button = Button(window, image=hide_image, command=hide, relief=FLAT, activebackground='white', bd=0, background='white')
    hide_button.place(x=550, y=210)
    password_entry.config(show='')

def hide():
    show_button = Button(window, image=show_image, command=show, relief=FLAT, activebackground='white', bd=0, background='white')
    show_button.place(x=550, y=210)
    password_entry.config(show='*')

show_image = ImageTk.PhotoImage(file='img/wifi/info.png')
hide_image = ImageTk.PhotoImage(file='img/wifi/refresh_wifi.png')

show_button = Button(window, image=show_image, command=show, relief=FLAT, activebackground='white', bd=0, background='white')
show_button.place(x=550, y=210)



password_entry = Entry(window, highlightthickness=2.4, bd=2.4, bg='white', fg='black', relief=FLAT, show='*', font=('Arial', 16))
password_entry.pack(pady=200)

window.mainloop()