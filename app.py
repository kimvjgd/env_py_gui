import tkinter as tk
from tkinter import ttk
from home import Home
from element import Element
from wifi import Wifi


PRIMARY_COLOR = "#2e3f4f"

class EnvSensor(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        style = ttk.Style(self)
        style.theme_use("clam")
        
        style.configure("Home.TFrame", background=PRIMARY_COLOR)
        
        self["background"] = PRIMARY_COLOR
        
        self.title("Env LAB")
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight=1)
        self.resizable(False, False)
        container = ttk.Frame(self)
        container.grid(row=0, column=0, sticky="NEWS")
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        container.config(width=800, height=480)
        
        self.frames = dict()
        
        #### frames ####
        
        # For Home
        ############################################################################################################################################
        home_frame = Home(container, self, lambda: self.show_frame(Element), lambda: self.show_frame(Wifi))
        home_frame.grid(row=0, column=0, sticky="NESW")
        
        # For Element
        ############################################################################################################################################
        element_frame = Element(container, self, lambda: self.show_frame(Home), sensor='TVOC')      # just for sample TVOC
        element_frame.grid(row=0, column=0, sticky="NESW")
        
        
        # For Wifi
        wifi_frame = Wifi(container, self, lambda: self.show_frame(Home))
        wifi_frame.grid(row=0, column=0, sticky="NEWS")
        
        self.frames[Home] = home_frame
        self.frames[Element] = element_frame
        self.frames[Wifi] = wifi_frame
        
        # First Screen
        self.show_frame(Home)

    
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
        print("클릭!!")


if __name__== '__main__':
    app = EnvSensor()
    app.geometry("800x480")
    app.mainloop()

