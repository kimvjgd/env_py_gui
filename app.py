import tkinter as tk
from tkinter import ttk
from home import Home
from element import Element
from sample_grid import Sample
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
        element_frame = Element(container, self, lambda: self.show_frame(Home))
        element_frame.grid(row=0, column=0, sticky="NESW")
        
        # For Sample
        sample_frame = Sample(container, self, lambda: self.show_frame())
        sample_frame.grid(row=0, column=0, sticky="NESW")
        
        # For Wifi
        wifi_frame = Wifi(container, self, lambda: self.show_frame(Home))
        wifi_frame.grid(row=0, column=0, sticky="NEWS")
        
        self.frames[Home] = home_frame
        self.frames[Element] = element_frame
        self.frames[Sample] = sample_frame
        self.frames[Wifi] = wifi_frame
        
        self.show_frame(Home)

    
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
        print("클릭!!")
    
app = EnvSensor()
app.geometry("800x480")
app.mainloop()






# TVOC_frame = TVOC(container, self, lambda: self.show_frame(TVOC))
        # TVOC_frame.grid(row=0, column=0, columnspan=2, sticky="NESW")
        # CO2_frame = CO2(container, self, lambda: self.show_frame(CO2))
        # CO2_frame.grid(row=0, column=0, columnspan=2, sticky="NESW")
        # PM25_frame = PM25(container, self, lambda: self.show_frame(PM25))
        # PM25_frame.grid(row=0, column=0, columnspan=2, sticky="NESW")
        # PM10_frame = PM10(container, self, lambda: self.show_frame(PM10))
        # PM10_frame.grid(row=0, column=0, columnspan=2, sticky="NESW")
        # CH2O_frame = CH2O(container, self, lambda: self.show_frame(CH2O))
        # CH2O_frame.grid(row=0, column=0, columnspan=2, sticky="NESW")
        # SM_frame = SM(container, self, lambda: self.show_frame(SM))
        # SM_frame.grid(row=0, column=0, columnspan=2, sticky="NESW")
        # NH3_frame = NH3(container, self, lambda: self.show_frame(NH3))
        # NH3_frame.grid(row=0, column=0, columnspan=2, sticky="NESW")
        # CO_frame = CO(container, self, lambda: self.show_frame(CO))
        # CO_frame.grid(row=0, column=0, columnspan=2, sticky="NESW")
        # NO2_frame = NO2(container, self, lambda: self.show_frame(NO2))
        # NO2_frame.grid(row=0, column=0, columnspan=2, sticky="NESW")
        # H2S_frame = H2S(container, self, lambda: self.show_frame(H2S))
        # H2S_frame.grid(row=0, column=0, columnspan=2, sticky="NESW")
        # Light_frame = Light(container, self, lambda: self.show_frame(Light))
        # Light_frame.grid(row=0, column=0, columnspan=2, sticky="NESW")
        # Sound_frame = Sound(container, self, lambda: self.show_frame(Sound))
        # Sound_frame.grid(row=0, column=0, columnspan=2, sticky="NESW")
        # Rn_frame = RN(container, self, lambda: self.show_frame(RN))
        # Rn_frame.grid(row=0, column=0, columnspan=2, sticky="NESW")
        # O3_frame = O3(container, self, lambda: self.show_frame(O3))
        # O3_frame.grid(row=0, column=0, columnspan=2, sticky="NESW")
        ############################################################################################################################################
        # self.frames[TVOC_frame] = TVOC_frame
        # self.frames[CO2_frame] = CO2_frame
        # self.frames[PM25_frame] = PM25_frame
        # self.frames[PM10_frame] = PM10_frame
        # self.frames[CH2O_frame] = CH2O_frame
        # self.frames[SM_frame] = SM_frame
        # self.frames[NH3_frame] = NH3_frame
        # self.frames[CO_frame] = CO_frame
        # self.frames[NO2_frame] = NO2_frame
        # self.frames[H2S_frame] = H2S_frame
        # self.frames[Light_frame] = Light_frame
        # self.frames[Sound_frame] = Sound_frame
        # self.frames[Rn_frame] = Rn_frame
        # self.frames[O3_frame] = O3_frame