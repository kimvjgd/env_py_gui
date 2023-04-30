import tkinter as tk
from tkinter import ttk
from home_screen import Home
from element_screen import Element
from wifi_screen import WifiScreen
from wifi_connection_screen import WifiConnectionScreen
# 나중에 링크 풀어줘야한다.
# from uart_data_thread import UartDataThread

FULL_SCREEN = False             # (True/False) - (Full Screen/Fixed Size Screen)
PRIMARY_COLOR = "#2e3f4f"
           

class EnvSensor(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TVOC = tk.StringVar(value=0)
        self.CO2 = tk.StringVar(value=0)
        self.PM25 = tk.StringVar(value=0)
        self.PM10 = tk.StringVar(value=0)
        self.CH2O = tk.StringVar(value=0)
        self.Sm = tk.StringVar(value=0)
        self.NH3 = tk.StringVar(value=0)
        self.CO = tk.StringVar(value=0)
        self.NO2 = tk.StringVar(value=0)
        self.H2S = tk.StringVar(value=0)
        self.LIGHT = tk.StringVar(value=0)
        self.SOUND = tk.StringVar(value=0)
        self.Rn = tk.StringVar(value=0)
        self.O3 = tk.StringVar(value=0)
        self.temperature = tk.StringVar(value=0)
        self.humidity = tk.StringVar(value=0)
        
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
        self.home_frame = Home(container, self, lambda: self.show_element_frame(Element), lambda: self.show_frame(WifiScreen))
        self.home_frame.grid(row=0, column=0, sticky="NESW")
        
        # For Element
        ############################################################################################################################################
        self.element_frame = Element(container, self, lambda: self.show_frame(Home), sensor=self.sensor_name)      # just for sample TVOC
        self.element_frame.grid(row=0, column=0, sticky="NESW")
        
        
                
        # For Wifi
        ############################################################################################################################################
        self.wifi_frame = WifiScreen(container, self, lambda: self.show_frame(Home))
        self.wifi_frame.grid(row=0, column=0, sticky="NEWS")
        
        # For Wifi Connection Screen
        ############################################################################################################################################
        self.wifi_connection_frame = WifiConnectionScreen(container, self, lambda: self.show_frame(WifiScreen))
        self.wifi_connection_frame.grid(row=0, column=0, sticky='NEWS')


        
        self.frames[Home] = self.home_frame
        self.frames[Element] = self.element_frame
        self.frames[WifiScreen] = self.wifi_frame
        
        # First Screenu
        self.show_frame(Home)

    
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
    
    def show_element_frame(self, container):
        # Element UI고치느라 주석
        self.element_frame.change_image(self.sensor_name)  
        frame = self.frames[container]
        frame.tkraise()
    
    def get_temp(self):
        print(self.TVOC)
        print(self.CO2)
        print(self.PM25)
        print(self.PM10)
        print(self.CH2O)
        print(self.Sm)
        print(self.NH3)
        print(self.CO)
        print(self.NO2)
        print(self.H2S)
        print(self.LIGHT)
        print(self.SOUND)
        print(self.Rn)
        print(self.O3)
        print(self.temperature)
        print(self.humidity)
        
        self.after(1000, self.get_temp)
        
import uart_data_thread

def pprint():
    print('일단 이거는 당연히 되는거지')




if __name__== '__main__':

    app = EnvSensor()
    # 나중에 주석을 풀어줘야 한다.
    # u = UartDataThread(app)
    # u.start()

    # home = app.home_frame
    # app.get_temp()
    app.home_frame.get_all_data()
    # app.home_frame.get_temperature(temperature=app.temperature.get())
    app.home_frame.time_update()
    
    # app.home_frame.data_get(u.TVOC,u.CO2,u.PM25,u.PM10,u.CH2O,u.Sm,u.NH3,u.CO,u.NO2,u.H2S,u.LIGHT,u.SOUND,u.Rn,u.O3,u.temperature,u.humidity)
    # temp_number = u.TVOC_VALUE
    # print('u.TVOC_VALUE : ', temp_number)
    # app.home_frame.get_one_data(temp_number)
    # app.wifi_frame.get_wifi_list()
    
    app.geometry("800x480")
    app.attributes('-fullscreen', FULL_SCREEN)
    app.mainloop()
# self.get_image(sensor_description_part, 'img/sensor/CH2O.png', 80, 80, 0, 0, 'NEWS', rowspan=2)
