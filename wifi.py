import tkinter as tk
from tkinter import ttk

class Wifi(ttk.Frame):
    def __init__(self, parent, controller, show_home):
        super().__init__(parent)
        
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        # tk.Label(self, text="Wifi Screen").pack()
        
        home_button = ttk.Button(self, text="Wifi Screen", command= show_home, cursor="hand2")
        home_button.grid(row=0, column=0, sticky="NEWS")