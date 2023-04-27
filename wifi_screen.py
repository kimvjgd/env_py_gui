import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from wifi import Cell, Scheme
import wifi
import subprocess

# class name을 Wifi로 지으면 안된다.
class WifiScreen(ttk.Frame):
    def __init__(self, parent, controller, show_home):
        super().__init__(parent)
        
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
        
        
        
        
        
        ##################################################################
        # main part
        main_part = tk.Frame(self, bg='black')
        main_part.grid(row=1, column=0, sticky="NEWS")
        # main_part - column configure
        main_part.columnconfigure(0, weight=1)
        # main_part - row configure
        main_part.rowconfigure(0,weight=8)      # 2     6
        main_part.rowconfigure(1,weight=1)      # 1     3
        main_part.rowconfigure(2,weight=4)      # 1     3
        main_part.rowconfigure(3,weight=4)      # 1     3
        main_part.rowconfigure(4,weight=48)     # 12    36
        
        
        wifi_title_part = tk.Frame(main_part, bg='black')
        wifi_title_part.grid(row=0, column=0,sticky='NEWS')
        wifi_title_part.columnconfigure(0, weight=1)
        wifi_title_part.columnconfigure(1, weight=5)
        wifi_title_part.columnconfigure(2, weight=2)
        
        wifi_title_part.rowconfigure(0, weight=1)
        
        # add_wifi_title_part.place(relx=0.1, rely=0.5, anchor='c')
        
        wifi_title_label = Label(wifi_title_part, text='Wi-Fi', font=('Arial',20), fg='blue', bg='black')
        wifi_title_label.grid(row=0, column=0,sticky="W", padx=20)
        
        
        
        current_wifi_title_part = tk.Frame(main_part, bg='black')
        current_wifi_title_part.grid(row=1, column=0,sticky='NEWS')
        
        current_wifi_title_label = Label(current_wifi_title_part, text='현재 네트워크',fg='white', bg='black', font=('Arial',15), padx=30)
        current_wifi_title_label.grid(row=0, column=0)

        current_wifi_part = tk.Frame(main_part, bg='black')
        current_wifi_part.grid(row=2, column=0,sticky='NEWS')
        current_wifi_part.rowconfigure(0,weight=1)
        current_wifi_part.columnconfigure(0, weight=1)
        current_wifi_part.columnconfigure(1, weight=12)
        
        def nothing_func():
            pass
        
        self.get_image(current_wifi_part, 'img/wifi/Wi-Fi-01.png', 25, 25, 0 ,0, 'E', command=nothing_func)
        
        self.current_wifi_label = Label(current_wifi_part, font=('Arial', 15), padx=14, fg='white', bg='black')
        self.current_wifi_label.grid(row=0, column=1, sticky='W')

        available_wifi_title_part = tk.Frame(main_part, bg='black')
        available_wifi_title_part.grid(row=3, column=0,sticky='NEWS')
        available_wifi_title_part.rowconfigure(0, weight=1)
        available_wifi_title_part.columnconfigure(0, weight=10)
        available_wifi_title_part.columnconfigure(1, weight=1)

        available_wifi_title_label = Label(available_wifi_title_part, text='사용 가능한 네트워크',fg='white', bg='black', font=('Arial',15), padx=30)
        available_wifi_title_label.grid(row=0, column=0)
        
        self.get_image(available_wifi_title_part, 'img/wifi/refresh_wifi.png', 25, 25, 0, 0, "NEWS")
        
        
        
        
        # available_wifi_title_label = Label(available_wifi_title_part, text='available_wifi_title_part')
        # available_wifi_title_label.grid(row=0, column=0)

        available_wifi_part = tk.Frame(main_part, bg='purple')
        available_wifi_part.grid(row=4, column=0,sticky='NEWS')
        available_wifi_part.rowconfigure(0, weight=1)
        available_wifi_part.rowconfigure(1, weight=1)
        available_wifi_part.columnconfigure(0, weight=1)
        available_wifi_part.columnconfigure(1, weight=11)
        available_wifi_part.columnconfigure(2, weight=1)
        
        up_button = Button(available_wifi_part, bg='red')
        up_button.grid(row=0, column=2,sticky='NEWS')

        down_button = Button(available_wifi_part, bg='blue')
        down_button.grid(row=1, column=2, sticky='NEWS')
        
        available_wifi_list_part = tk.Frame(available_wifi_part, bg='yellow')
        available_wifi_list_part.grid(row=0, column=1, rowspan=2, sticky='NEWS')
        
        
        
        
        # available_wifi_label = Label(available_wifi_part, text='available_wifi_part')
        # available_wifi_label.grid(row=0, column=0)
        # for i in range(5):
        #     self.get_image(available_wifi_part, 'img/wifi/Wi-Fi-01.png', 25, 25, i ,0, 'E', command=nothing_func)
        #     available_wifi_label = Label(available_wifi_part, text='sangsanglab 5G', font=('Arial', 15), padx=14, fg='white', bg='black')
        #     available_wifi_label.grid(row=i, column=1, sticky='W')


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
        
    def get_wifi_list(self):
        cells = Cell.all('wlan0')
        for cell in cells:
            print(cell.ssid)
            
        try:
            result = subprocess.check_output(["iwgetid", "-r"])
            # print("현재 연결된 WiFi의 SSID:", result.decode().strip())
            self.current_wifi_label.config(text=result.decode().strip())
            # for cell in cells:
            #     print(cell.ssid)
            # 여기서 gui update해줘야한다.
        except:
            result = ''
            
        self.current_wifi_label.after(1000, self.get_wifi_list)
    
    
        
        