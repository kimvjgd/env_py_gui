import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

class WifiDetailScreen(ttk.Frame):
    def __init__(self, parent, controller, show_wifi_list_screen, wifi_name='temp_wifi_name'):
        super().__init__(parent)
        self.controller = controller
        self.wifi_name = wifi_name
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0,weight=2)   # status
        self.rowconfigure(1,weight=2)   # 비밀번호
        self.rowconfigure(2,weight=4)   # type PW
        self.rowconfigure(3,weight=4)   # auto connection
        self.rowconfigure(4,weight=2)   # connect
        
        
        status_part = tk.Frame(self, bg='blue')
        status_part.grid(row=0, column=0, sticky="NEWS")
        
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
        back_button_part.bind("<Button-1>", show_wifi_list_screen)
        self.get_image(back_button_part, "img/parts/back_button.png", 30, 30,0, 0, 'E', command=show_wifi_list_screen)
        back_label = Label(back_button_part, text='BACK', font=('Arial', 30), fg='white', bg='black', pady=3)
        back_label.grid(row=0, column=1, sticky='NW')
        # 나중에 정리....
        def back_click(event):
            show_wifi_list_screen()
        back_label.bind("<Button-1>", back_click)
        pw_label = Label(self, text='비밀번호', font=('Arial', 10))
        pw_label.grid(row=1, column=0, sticky="W")
        
        
        
        

        
        
        
        
    def get_image(self, frame, path, width, height, row, column,sticky, command=None):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Label(frame, image=photo_img, bg='black')
        img_label.image = photo_img
        img_label.grid(row=row, column=column, sticky=sticky)
        def local_click(event):
            command()
        img_label.bind("<Button-1>", local_click)