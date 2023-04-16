import tkinter as tk
from tkinter import ttk
from home_screen import Home
from element_screen import Element
from wifi_screen import Wifi


FULL_SCREEN = False             # (True/False) - (Full Screen/Fixed Size Screen)
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
        # self.sensor_name = tk.StringVar(value='TVOC')
        self.sensor_name = 'TVOC'
        container = ttk.Frame(self)
        container.grid(row=0, column=0, sticky="NEWS")
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        container.config(width=800, height=480)
        
        self.frames = dict()
        
        #### frames ####
        
        # For Home
        ############################################################################################################################################
        self.home_frame = Home(container, self, lambda: self.show_element_frame(Element), lambda: self.show_frame(Wifi))
        
        self.home_frame.grid(row=0, column=0, sticky="NESW")
        
        # For Element
        ############################################################################################################################################
        self.element_frame = Element(container, self, lambda: self.show_frame(Home), sensor=self.sensor_name)      # just for sample TVOC
        self.element_frame.grid(row=0, column=0, sticky="NESW")
        
        
        
        # For Wifi
        wifi_frame = Wifi(container, self, lambda: self.show_frame(Home))
        wifi_frame.grid(row=0, column=0, sticky="NEWS")
        
        self.frames[Home] = self.home_frame
        self.frames[Element] = self.element_frame
        self.frames[Wifi] = wifi_frame
        
        # First Screenu
        self.show_frame(Home)

    
    def show_frame(self, container):
        frame = self.frames[container]
        print('sensor name : ',self.sensor_name)
        frame.tkraise()
    
    def show_element_frame(self, container):            # 왜 한박자씩 느려... ㅠ
        print('###sensor name : ',self.sensor_name)
        # Element UI고치느라 주석
        # self.element_frame.change_image(self.sensor_name)          
        frame = self.frames[container]
        frame.tkraise()
        


if __name__== '__main__':
    # time_instance = Home()
    # time_instance.time_update()
    app = EnvSensor()
    app.home_frame.time_update()
    
    app.geometry("800x480")
    app.attributes('-fullscreen', FULL_SCREEN)
    app.mainloop()

# self.get_image(sensor_description_part, 'img/sensor/CH2O.png', 80, 80, 0, 0, 'NEWS', rowspan=2)
