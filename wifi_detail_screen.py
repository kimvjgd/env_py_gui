import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

class WifiDetailScreen(ttk.Frame):
    def __init__(self, parent, controller, show_wifi_list_screen, show_keyboard_screen, wifi_name='temp_wifi_name'):
        super().__init__(parent)
        
        self.controller = controller
        self.wifi_name = wifi_name
        self.show_keyboard_screen = show_keyboard_screen
        self.pw_visible_state = False            # True - Visible

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0,weight=1)   # status
        self.rowconfigure(1,weight=1)   # 비밀번호
        self.rowconfigure(2,weight=2)   # type PW
        self.rowconfigure(3,weight=2)   # auto connection
        self.rowconfigure(4,weight=1)   # connect
        
        
        status_part = tk.Frame(self, bg='black')
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
        pw_label = Label(self, text='비밀번호', font=('Arial', 30))
        pw_label.grid(row=1, column=0, sticky="W")

        self.pw_core_frame = Frame(self, bg='black')
        self.pw_core_frame.grid(row=2, column=0)
        self.pw_core_frame.rowconfigure(0, weight=1)
        self.pw_core_frame.columnconfigure(0, weight=10)
        self.pw_core_frame.columnconfigure(1, weight=1)
        

        def entry_click(event):
            show_keyboard_screen()

        self.password_entry = Entry(self.pw_core_frame, highlightthickness=2.4, bd=2.4, bg='white', fg='black', relief=FLAT, show='*', font=('Arial', 16))
        self.password_entry.grid(row=0, column=0)
        self.password_entry.config(show='*')
        self.password_entry.bind('<Button-1>', entry_click)

        self.show_image = ImageTk.PhotoImage(file='img/wifi/info.png')
        self.hide_image = ImageTk.PhotoImage(file='img/wifi/refresh_wifi.png')
        
        self.show_button = Button(self.pw_core_frame, image=self.show_image, command=self.show, relief=FLAT, activebackground='white', bd=0, background='white')
        self.show_button.grid(row=0, column=1)
        
        self.auto_connection_frame = Frame(self, bg='blue')
        self.auto_connection_frame.grid(row=3, column=0)
        self.auto_connection_frame.rowconfigure(0, weight=1)
        self.auto_connection_frame.columnconfigure(0, weight=6)
        self.auto_connection_frame.columnconfigure(1, weight=1)

        Label(self.auto_connection_frame, text='자동으로 연결', font=('Arial',30)).grid(row=0, column=0)
            
        
        self.on = PhotoImage(file='img/wifi/on.png')
        self.off = PhotoImage(file='img/wifi/off.png')
        self.auto_btn = Button(self.auto_connection_frame, image=self.on, bd=0, command=self.switch)
        self.auto_btn.grid(row=0, column=1)
        
    def switch(self):
        if self.pw_visible_state:
            self.auto_btn.config(image=self.off)
            self.pw_visible_state = False
        else:
            self.auto_btn.config(image=self.on)
            self.pw_visible_state = True
            
        
    def show(self):
        print(self.pw_visible_state)
        if self.pw_visible_state:
            self.show_button.config(image=self.hide_image)
            self.password_entry.config(show='*')
            self.pw_visible_state = not self.pw_visible_state
            
        else:
            self.show_button.config(image=self.show_image)
            self.password_entry.config(show='')
            self.pw_visible_state = not self.pw_visible_state
    
        
        
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