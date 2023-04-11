import tkinter as tk
from tkinter import ttk
from sensor_list import SENSOR_DICT
from tkinter import *

class Element(ttk.Frame):
    def __init__(self,parent, controller, show_home, sensor):
        super().__init__(parent)
        self.controller = controller
        self.sensor_name = sensor


        self.columnconfigure(0, weight=1)
        
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=3)
        self.rowconfigure(2,weight=2)
        self.rowconfigure(3,weight=1)
        self.rowconfigure(4,weight=1)
        
        
        # Frame and grid object to Win
        status_part = tk.Frame(self, bg="red")
        status_part.grid(row=0, column=0, sticky="NEWS")
        
        description_part = tk.Frame(self, bg="blue")
        description_part.grid(row=1, column=0, sticky="NEWS")
        description_part.rowconfigure(0, weight=0)
        description_part.columnconfigure(0, weight=1)
        description_part.columnconfigure(1, weight=1)
        
        
        current_value_part = tk.Frame(self, bg="green")
        current_value_part.grid(row=2, column=0, sticky="NEWS")
        
        color_gauge_part = tk.Frame(self, bg="yellow")
        color_gauge_part.grid(row=3, column=0, sticky="NEWS")
        
        num_value_part = tk.Frame(self, bg="grey")
        num_value_part.grid(row=4, column=0, sticky="NEWS")


###########################################################################################        
        # put product in frame  

        # Status Part
        left_part = tk.Frame(status_part)
        left_part.grid(sticky="W")
        left_part.columnconfigure(0, weight=1)
        left_part.columnconfigure(1, weight=1)
        
        left_part.rowconfigure(0, weight=1)
        back_button = ttk.Button(left_part, text="Back", command=show_home, cursor="hand2",width=5)
        back_button.grid(row=0, column=0)
        
        to_main_label = tk.Label(left_part, text="MAIN")
        to_main_label.grid(row=0, column=1)
        
        #### Description Part
        description_left_part = tk.Frame(description_part)
        description_left_part.rowconfigure(0, weight=1)
        description_left_part.columnconfigure(0, weight=1)
        description_left_part.columnconfigure(1, weight=6)
        description_left_part.grid(row=0, column=0, sticky="NEWS")
        
        #sample photo code
        img = PhotoImage(file=SENSOR_DICT[sensor][1])
        self.img_label = Label(description_part, image=img, bg='black')
        self.img_label.image = img
        # img_label.configure(image=PhotoImage(file=SENSOR_DICT[sensor][1]))
        # img_label.image = PhotoImage(file=SENSOR_DICT[sensor][1])
        self.img_label.grid(row=0, column=0, sticky="NEWS")
        
        
        #### Current Value Part
        
        #### Color Gauge Part
        
        #### Num Value Part


    def change_image(self,sensor_name):
        img = PhotoImage(file=SENSOR_DICT[sensor_name][1])
        self.img_label.configure(image=img)
        self.img_label.image = img
        print('######################################')
        print(sensor_name)
        print('######################################')
        