import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# from wifi import Cell, Scheme

class Wifi(ttk.Frame):
    def __init__(self, parent, controller, show_home):
        super().__init__(parent)
        
        # cells = Cell.all('wlan0')
        # for cell in cells:
        #     print(cell.ssid)
        self.show_home = show_home
        
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=6)
        
        

        status_part = tk.Frame(self, bg="black")
        status_part.grid(row=0, column=0, sticky="NEWS")
        
        
        status_part.rowconfigure(0, weight=1)

        status_part.columnconfigure(0, weight=1)
        status_part.columnconfigure(1, weight=10)
        status_part.columnconfigure(2, weight=1)
        
        back_button_part = tk.Frame(status_part, bg='black')
        back_button_part.grid(row=0, column=0, sticky="NEWS", pady=10,ipadx=0, ipady=0)
        back_button_part.place(relx=0.1, rely=0.5, anchor='c')          # 안맞으면...그냥 해야함... 나도 이유 모름... 그냥.... 그냥 함...  아니면 골 때려짐
        back_button_part.rowconfigure(0, weight=1)
        back_button_part.columnconfigure(0, weight=1)
        back_button_part.columnconfigure(1, weight=1)
        back_button_part.bind("<Button-1>", show_home)
        
        # self.get_button(back_button_part, show_home, "img/parts/back_button.png", 25, 25,0, 0, 'NE')
        self.get_image(back_button_part, "img/parts/back_button.png", 25, 25,0, 0, 'NE', command=show_home)
        back_label = Label(back_button_part, text='BACK', font=('Arial', 20), fg='white', bg='black')
        back_label.grid(row=0, column=1, sticky='NW')
        
        # 나중에 정리....
        def back_click(event):
            show_home()
        
        back_label.bind("<Button-1>", back_click)
        
        
        
        
        
        
        # 위의 status bar
        main_part = tk.Frame(self, bg='black')
        main_part.grid(row=1, column=0, sticky="NEWS")
        # main_part - column configure
        main_part.columnconfigure(0, weight=1)
        # main_part - row configure
        main_part.rowconfigure(0,weight=4)
        main_part.rowconfigure(1,weight=3)
        main_part.rowconfigure(2,weight=3)
        main_part.rowconfigure(3,weight=3)
        main_part.rowconfigure(4,weight=12)
        
        
        add_wifi_title_part = tk.Frame(main_part, bg='red')
        add_wifi_title_part.grid(row=0, column=0,sticky='NEWS')
        add_wifi_title_part.columnconfigure(0, weight=1)
        add_wifi_title_part.columnconfigure(1, weight=5)
        add_wifi_title_part.columnconfigure(2, weight=2)
        
        add_wifi_title_part.rowconfigure(0, weight=1)
        
        # add_wifi_title_part.place(relx=0.1, rely=0.5, anchor='c')
        
        wifi_title_label = Label(add_wifi_title_part, text='Wi-Fi')
        wifi_title_label.grid(row=0, column=0)
        
        current_wifi_title_part = tk.Frame(main_part, bg='blue')
        current_wifi_title_part.grid(row=1, column=0,sticky='NEWS')
        
        current_wifi_title_label = Label(current_wifi_title_part, text='current_wifi_title_part')
        current_wifi_title_label.grid(row=0, column=0)

        current_wifi_part = tk.Frame(main_part, bg='green')
        current_wifi_part.grid(row=2, column=0,sticky='NEWS')
        
        current_wifi_label = Label(current_wifi_part, text='current_wifi_part')
        current_wifi_label.grid(row=0, column=0)

        available_wifi_title_part = tk.Frame(main_part, bg='yellow')
        available_wifi_title_part.grid(row=3, column=0,sticky='NEWS')
        
        available_wifi_title_label = Label(available_wifi_title_part, text='available_wifi_title_part')
        available_wifi_title_label.grid(row=0, column=0)

        available_wifi_part = tk.Frame(main_part, bg='purple')
        available_wifi_part.grid(row=4, column=0,sticky='NEWS')
        
        available_wifi_label = Label(available_wifi_part, text='available_wifi_part')
        available_wifi_label.grid(row=0, column=0)


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

    def get_button(self, frame,command, path, width, height, row, column,sticky):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Button(frame, image=photo_img, bg='black', command=command,bd=0)        # bd = border
        img_label.image = photo_img
        img_label.grid(row=row, column=column, sticky=sticky)