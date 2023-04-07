import tkinter as tk
from tkinter import ttk

class Element(ttk.Frame):
    def __init__(self,parent, controller, show_home):
        super().__init__(parent)
        
        self.controller = controller
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight = 1)
        self.controller = controller
        element_container = ttk.Frame(
            self,
            padding = "30 15 30 15",
            style = "Background.TFrame"
        )
        
        # home_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)
        
        # home_container.columnconfigure((0,1,2), weight=1)
        # home_container.rowconfigure(1, weight=1)
        
        # home_label = ttk.Label(
        #     home_container,
        #     text="Home",
            
        # )
        # home_label.grid(column=0, row=0, sticky="W")
        
        home_button = ttk.Button(
            self,
            text="to Home",
            command=show_home,
            cursor="hand2"
        )
        home_button.grid(row=0, column=1, sticky="E", pady = (10,0))