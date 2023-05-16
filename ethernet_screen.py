import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class EthernetScreen(ttk.Frame):
    def __init__(self, parent, controller, show_home):
        super().__init__(parent)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=6)
        self.columnconfigure(0, weight=1)
        status_part = tk.Frame(self, bg='red')
        status_part.grid(row=0, column=0, sticky='NEWS')

        status_part.rowconfigure(0, weight=1)
        status_part.columnconfigure(0, weight=1)
        status_part.columnconfigure(1, weight=10)
        status_part.columnconfigure(2, weight=1)

        back_button_part = tk.Frame(status_part, bg='black')
        back_button_part.grid(row=0, column=0, sticky="NEWS", pady=0,ipadx=0, ipady=0)
        back_button_part.place(relx=0.1, rely=0.5, anchor='c')          # 안맞으면...그냥 해야함... 나도 이유 모름... 그냥.... 그냥 함...  아니면 골 때려짐
        back_button_part.rowconfigure(0, weight=1)
        back_button_part.columnconfigure(0, weight=1)
        back_button_part.columnconfigure(1, weight=1)
        back_button_part.bind("<Button-1>", show_home)
        self.get_image(back_button_part, "img/parts/back_button.png", 30, 30,0, 0, 'E', command=show_home)
        back_label = Label(back_button_part, text='BACK', font=('Arial', 30), fg='white', bg='black', pady=3)
        back_label.grid(row=0, column=1, sticky='NW')
        # 나중에 정리....
        def back_click(event):
            show_home()
        back_label.bind("<Button-1>", back_click)