import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from wifi import Cell, Scheme
import wifi
import subprocess
import wifi_func as wf

# class name을 Wifi로 지으면 안된다.
class WifiScreen(ttk.Frame):
    def __init__(self, parent, controller, show_home, show_wifi_detail):
        super().__init__(parent)
        
        self.show_home = show_home
        self.show_wifi_detail = show_wifi_detail
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=6)
        
        self.available_wifi_list = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff', 'gggg', 'hhhh', 'iiii', 'jjjj', 'kkkk']
        self.showing_wifi_list = self.available_wifi_list[0:3]
        self.last_num = len(self.available_wifi_list) - 1
        self.current_start_num = 0
        self.current_end_num = 2
        
        
        status_part = tk.Frame(self, bg="black")
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
        back_button_part.bind("<Button-1>", show_home)
        
        # self.get_button(back_button_part, show_home, "img/parts/back_button.png", 25, 25,0, 0, 'NE')
        self.get_image(back_button_part, "img/parts/back_button.png", 30, 30,0, 0, 'E', command=show_home)
        back_label = Label(back_button_part, text='BACK', font=('Arial', 30), fg='white', bg='black', pady=3)
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
        
        wifi_title_label = Label(wifi_title_part, text='Wi-Fi', font=('Arial',22), fg='blue', bg='black')
        wifi_title_label.grid(row=0, column=0,sticky="W", padx=20)
        
        current_wifi_title_part = tk.Frame(main_part, bg='black')
        current_wifi_title_part.grid(row=1, column=0,sticky='NEWS')
        
        current_wifi_title_label = Label(current_wifi_title_part, text='현재 네트워크',fg='white', bg='black', font=('Arial',18), padx=30)
        current_wifi_title_label.grid(row=0, column=0)

        current_wifi_part = tk.Frame(main_part, bg='black')
        current_wifi_part.grid(row=2, column=0,sticky='NEWS')
        current_wifi_part.rowconfigure(0,weight=1)
        current_wifi_part.columnconfigure(0, weight=1)
        current_wifi_part.columnconfigure(1, weight=12)
        
        def nothing_func():
            pass
        
        self.get_image(current_wifi_part, 'img/wifi/Wi-Fi-01.png', 40, 40, 0 ,0, 'E', command=nothing_func)
        
        self.current_wifi_label = Label(current_wifi_part, text= 'Sangsanglab 5G', font=('Arial', 18), padx=14, fg='white', bg='black')
        self.current_wifi_label.grid(row=0, column=1, sticky='W')

        available_wifi_title_part = tk.Frame(main_part, bg='black')
        available_wifi_title_part.grid(row=3, column=0,sticky='NEWS')
        available_wifi_title_part.rowconfigure(0, weight=1)
        available_wifi_title_part.columnconfigure(0, weight=10)
        available_wifi_title_part.columnconfigure(1, weight=1)

        available_wifi_title_label = Label(available_wifi_title_part, text='사용 가능한 네트워크',fg='white', bg='black', font=('Arial',20), padx=30)
        available_wifi_title_label.grid(row=0, column=0, sticky='W')
        
        self.get_image(available_wifi_title_part, 'img/wifi/refresh_wifi.png', 25, 25, 0, 1, "NEWS",self.get_wifi_list)
        
        
        # available_wifi_title_label = Label(available_wifi_title_part, text='available_wifi_title_part')
        # available_wifi_title_label.grid(row=0, column=0)

        available_wifi_part = tk.Frame(main_part, bg='black')
        available_wifi_part.grid(row=4, column=0,sticky='NEWS')
        available_wifi_part.rowconfigure(0, weight=1)
        available_wifi_part.rowconfigure(1, weight=1)
        available_wifi_part.columnconfigure(0, weight=1)
        available_wifi_part.columnconfigure(1, weight=11)
        available_wifi_part.columnconfigure(2, weight=1)
        
        up_button = Button(available_wifi_part, bg='red', command=self.press_up_button)
        up_button.grid(row=0, column=2,sticky='NEWS')

        down_button = Button(available_wifi_part, bg='blue', command=self.press_down_button)
        down_button.grid(row=1, column=2, sticky='NEWS')
        
        available_wifi_list_part = tk.Frame(available_wifi_part, bg='black')
        # available_wifi_list_part.grid(row=0, column=1, rowspan=2, sticky='NEWS')
        available_wifi_list_part.grid(row=0, column=1, rowspan=2, sticky='NEWS')
        available_wifi_list_part.columnconfigure(0, weight=1)
        available_wifi_list_part.columnconfigure(1, weight=15)
        available_wifi_list_part.rowconfigure(0, weight=1)
        available_wifi_list_part.rowconfigure(1, weight=1)
        available_wifi_list_part.rowconfigure(2, weight=1)
        available_wifi_list_part.rowconfigure(3, weight=1)
        
        # first_label = Label(available_wifi_list_part, text='first!!', font=('Arial', 20))
        # second_label = Label(available_wifi_list_part, text='first!!', font=('Arial', 20))
        # third_label = Label(available_wifi_list_part, text='first!!', font=('Arial', 20))
        # first_label.grid(row=0)
        # second_label.grid(row=1)
        # third_label.grid(row=2)
        
        self.get_image(available_wifi_list_part, 'img/wifi/Wi-Fi-01.png', 40, 40, 0 ,0, 'E', command=self.show_wifi_detail)
        self.first_label = Label(available_wifi_list_part, text=self.showing_wifi_list[0], font=('Arial', 20), padx=14, fg='white', bg='black')
        self.first_label.grid(row=0, column=1, sticky='W')
        
        self.get_image(available_wifi_list_part, 'img/wifi/Wi-Fi-01.png', 40, 40, 1 ,0, 'E', command=self.show_wifi_detail)
        self.second_label = Label(available_wifi_list_part, text=self.showing_wifi_list[1], font=('Arial', 20), padx=14, fg='white', bg='black')
        self.second_label.grid(row=1, column=1, sticky='W')
        
        self.get_image(available_wifi_list_part, 'img/wifi/Wi-Fi-01.png', 40, 40, 2 ,0, 'E', command=self.show_wifi_detail)
        self.third_label = Label(available_wifi_list_part, text=self.showing_wifi_list[2], font=('Arial', 20), padx=14, fg='white', bg='black')
        self.third_label.grid(row=2, column=1, sticky='W')
        
                
        available_wifi_label = Label(available_wifi_part, text=' ', bg='black')
        available_wifi_label.grid(row=0, column=0)

    def open(self):
        top = Toplevel(self)
        top.geometry("800x480")
        top.attributes('-fullscreen', False)
        top.title('My Second Window')
        connecting_frame = tk.Frame(top, bg='black')
        connecting_frame.grid(row=0, column=0, sticky='NEWS')
        connecting_frame.rowconfigure(0, weight=1)
        connecting_frame.columnconfigure(0, weight=1)
        
        my_label = Label(connecting_frame, text='Second Window')
        my_label.grid(row=0, column=0, sticky='NEWS')

    def press_up_button(self):
        if self.current_start_num>0:
            self.current_start_num -= 1
            self.current_end_num -= 1
            
            self.showing_wifi_list = self.available_wifi_list[self.current_start_num:self.current_end_num+1]
            self.first_label.config(text=self.showing_wifi_list[0])
            self.second_label.config(text=self.showing_wifi_list[1])
            self.third_label.config(text=self.showing_wifi_list[2])
            
    
    def press_down_button(self):
        if self.current_end_num < len(self.available_wifi_list)-1:
            self.current_start_num += 1
            self.current_end_num += 1
            
            self.showing_wifi_list = self.available_wifi_list[self.current_start_num:self.current_end_num+1]
            self.first_label.config(text=self.showing_wifi_list[0])
            self.second_label.config(text=self.showing_wifi_list[1])
            self.third_label.config(text=self.showing_wifi_list[2])
            
        
    # def time_update(self):
    #     time_string = strftime('%Y-%m-%d %H:%M:%S')
    #     self.time_label.config(text=time_string)
    #     self.time_label.after(1000, self.time_update)
    #     # print(uart_data_thread.TVOC)

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
        self.available_wifi_list = wf.wifi_Search()
        self.available_wifi_list.sort(key = lambda x:x[1])
        self.showing_wifi_list = self.available_wifi_list[0:3]
        self.last_num = len(self.available_wifi_list) -1
        self.current_start_num = 0
        self.current_end_num = 2
        
        
        self.first_label.config(text=self.available_wifi_list[0])
        self.second_label.config(text=self.available_wifi_list[1])
        self.third_label.config(text=self.available_wifi_list[2])
        
        

