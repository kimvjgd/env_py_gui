import tkinter as tk
from tkinter import ttk
from tkinter import *

class WifiDetailScreen(ttk.Frame):
    def __init__(self, parent, controller, show_wifi_list_screen, wifi_name='temp_wifi_name'):
        super().__init__(parent)
        self.controller = controller
        self.wifi_name = wifi_name
        self.rowconfigure(0,weight=3)
        self.rowconfigure(1,weight=2)
        self.rowconfigure(2,weight=4)
        self.rowconfigure(3,weight=2)
        self.rowconfigure(4,weight=4)
        self.rowconfigure(5,weight=4)
        
        status_part = tk.Frame(self, bg='blue')
        
        
        self.get_image(status_part, "img/parts/back_button.png", 30, 30,0, 0, 'E', command=show_wifi_list_screen)
        back_label = Label(status_part, text='BACK', font=('Arial', 30), fg='white', bg='black', pady=3)
        back_label.grid(row=0, column=1, sticky='NW')
        
        
        
        
        