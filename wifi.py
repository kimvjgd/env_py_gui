import tkinter as tk
from tkinter import ttk
# from wifi import Cell, Scheme

class Wifi(ttk.Frame):
    def __init__(self, parent, controller, show_home):
        super().__init__(parent)
        
        # cells = Cell.all('wlan0')
        # for cell in cells:
        #     print(cell.ssid)
        
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        status_part = tk.Frame(self, bg="red")
        status_part.grid(row=0, column=0, sticky="NEWS")

        add_network_part = tk.Frame(self, bg="blue")
        add_network_part.grid(row=1, column=0, sticky="NEWS")

        current_network_part = tk.Frame(self, bg="green")
        current_network_part.grid(row=2, column=0, sticky="NEWS")

        available_network_part = tk.Frame(self, bg="yellow")
        available_network_part.grid(row=3, column=0, sticky="NEWS")

        # Status Part
        back_button = ttk.Button(status_part, text="Back", command=show_home, cursor="hand2")
        back_button.grid(sticky="W")

        # Add Network Part
        wifi_label = tk.Label(add_network_part, text="Wi-Fi")
        wifi_label.grid(sticky="W")
        

        # Current Network Part
        current_wifi_label = tk.Label(current_network_part, text="현재 네트워크")
        current_wifi_label.grid(sticky="W")
        

        # Available Network Part
        available_wifi_label = tk.Label(available_network_part, text="현재 네트워크")
        available_wifi_label.grid(sticky="W")


        
        # tk.Label(self, text="Wifi Screen").pack()
        
        # home_button = ttk.Button(self, text="Wifi Screen", command= show_home, cursor="hand2")
        # home_button.grid(row=0, column=0, sticky="NEWS")

        
