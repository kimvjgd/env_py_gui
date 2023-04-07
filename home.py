import tkinter as tk
from tkinter import ttk
from tkinter import *

class Home(ttk.Frame):
    def __init__(self, parent, controller, show_element, show_wifi):
        super().__init__(parent)
        
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=6)
        
        
        # status (upper)
        status_part = tk.Frame(self, bg="red")
        status_part.grid(row=0, column=0, sticky="NEWS")
        status_part.columnconfigure(0, weight=1)
        status_part.columnconfigure(1, weight=1)
        status_part.rowconfigure(0, weight=1)
        
        
        # temperature & humidity (middle)
        temp_hum_part = tk.Frame(self, bg="blue")
        temp_hum_part.grid(row=1, column=0, sticky="NEWS")
        
        # sensor values (lower)
        sensor_part = tk.Frame(self, bg="green")
        sensor_part.grid(row=2, column=0, sticky="NEWS")
        
        
        ##### put modules in frames #####
################################################################################################################################################################

        #status
        time_label = tk.Label(status_part, text="status")
        time_label.grid(column=0, row=0)
        
        wifi_image = tk.PhotoImage(file="image.png")
        wifi_button = tk.Button(status_part, image=wifi_image, command=show_wifi)
        wifi_button.image = wifi_image                  # to keep a ref
        wifi_button.grid(column=1,row=0)
        
        
        # temperature & humidity
        temp_hum_label = tk.Label(temp_hum_part, text="temp_hum")
        temp_hum_label.pack()
        
        # sensor values
        sensor_label = tk.Label(sensor_part, text="sensor values")
        sensor_label.pack()
        
        
        
        
        
        
        
        
        # element_button = ttk.Button(
        #     self,
        #     text="to Element",
        #     command=show_element,
        #     cursor="hand2"
        # )
        # element_button.grid(row=0, column=1, sticky="NEWS", pady = (10,0))
        
        
        