import tkinter as tk
from tkinter import ttk
from tkinter import *
from datetime import datetime
from time import strftime
class Home(ttk.Frame):
    def __init__(self, parent, controller, show_element, show_wifi):
        super().__init__(parent)
        # time_update()
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=5)
        
        
        # status (upper)
        status_part = tk.Frame(self, bg="black")
        status_part.grid(row=0, column=0, sticky="NEWS")
        status_part.columnconfigure(0, weight=10)
        status_part.columnconfigure(1, weight=1)
        status_part.rowconfigure(0, weight=1)
        
        
        # temperature & humidity (middle)
        temp_hum_part = tk.Frame(self, bg="black")
        temp_hum_part.grid(row=1, column=0, sticky="NEWS")
        temp_hum_part.rowconfigure(0, weight=1)
        temp_hum_part.columnconfigure(0, weight=2)
        temp_hum_part.columnconfigure(1, weight=3)
        temp_hum_part.columnconfigure(2, weight=8)
        temp_hum_part.columnconfigure(3, weight=2)
        temp_hum_part.columnconfigure(4, weight=3)
        temp_hum_part.columnconfigure(5, weight=8)
        
        # sensor values (lower)
        sensor_part = tk.Frame(self, bg="black")
        sensor_part.grid(row=2, column=0, sticky="NEWS")
        # row configure
        sensor_part.rowconfigure(0, weight=10)      # first row
        sensor_part.rowconfigure(1, weight=1)       # separator
        sensor_part.rowconfigure(2, weight=10)      # second row
        # column configure
        sensor_part.columnconfigure(0,weight=9)     # tvoc  &   co
        sensor_part.columnconfigure(1,weight=1)
        sensor_part.columnconfigure(2,weight=9)     # co2   &   no2
        sensor_part.columnconfigure(3,weight=1)
        sensor_part.columnconfigure(4,weight=9)     # pm2.5 &   h2s
        sensor_part.columnconfigure(5,weight=1)
        sensor_part.columnconfigure(6,weight=9)     # pm10  &   light
        sensor_part.columnconfigure(7,weight=1)
        sensor_part.columnconfigure(8,weight=9)     # ch2o  &   sound
        sensor_part.columnconfigure(9,weight=1)
        sensor_part.columnconfigure(10,weight=9)    # sm    &   rn
        sensor_part.columnconfigure(11,weight=1)
        sensor_part.columnconfigure(12,weight=9)    # nh3   &   o3
        
        
        
        
        
        ##### put modules in frames #####
################################################################################################################################################################
        from PIL import Image, ImageTk
        #status
        self.time_label = tk.Label(status_part,bg='black',text='', fg='white', font=('Arial', 20))
        self.time_label.grid(column=0, row=0,sticky="W")
        
        
        wifi_image = tk.PhotoImage(file='img/wifi/wifi.png')
        
        wifi_button = tk.Button(status_part, image=wifi_image, command=show_wifi, height=20, width=20)
        wifi_button.image = wifi_image                  # to keep a ref
        wifi_button.grid(column=1,row=0)
        
        
        
        # temperature & humidity
        
        # temperature
        self.set_image(temp_hum_part, 'img/temperature/temp_img.png', row=0, column=0, height=40)
        self.set_label(temp_hum_part, '36.7°C', row=0, column=1)
        self.set_image(temp_hum_part, 'img/temperature/temp5.png', row=0, column=2, height=20)

        # humidity
        self.set_image(temp_hum_part, 'img/humidity/humidity_img.png', row=0, column=3, height=40)
        self.set_label(temp_hum_part, '53%', row=0, column=4)
        self.set_image(temp_hum_part, 'img/humidity/humidity5.png', row=0, column=5, height=20)
        
        
        
        
        # sensor values
        tvoc_part = tk.Frame(sensor_part,bg="black")
        tvoc_part.grid(row=0,column=0,sticky='NEWS')
        self.set_frame_configure(tvoc_part)
        
        co_part = tk.Frame(sensor_part, bg='black')
        co_part.grid(row=2,column=0,sticky='NEWS')
        self.set_frame_configure(co_part)
        
        

        co2_part = tk.Frame(sensor_part, bg='black')
        co2_part.grid(row=0,column=2,sticky='NEWS')
        self.set_frame_configure(co2_part)


        no2_part = tk.Frame(sensor_part, bg='black')
        no2_part.grid(row=2,column=2,sticky='NEWS')
        self.set_frame_configure(no2_part)


        pm25_part = tk.Frame(sensor_part, bg='black')
        pm25_part.grid(row=0,column=4,sticky='NEWS')
        self.set_frame_configure(pm25_part)


        h2s_part = tk.Frame(sensor_part, bg='black')
        h2s_part.grid(row=2,column=4,sticky='NEWS')
        self.set_frame_configure(h2s_part)


        pm10_part = tk.Frame(sensor_part, bg='black')
        pm10_part.grid(row=0,column=6,sticky='NEWS')
        self.set_frame_configure(pm10_part)


        light_part = tk.Frame(sensor_part, bg='black')
        light_part.grid(row=2,column=6,sticky='NEWS')
        self.set_frame_configure(light_part)


        ch2o_part = tk.Frame(sensor_part, bg='black')
        ch2o_part.grid(row=0,column=8,sticky='NEWS')
        self.set_frame_configure(ch2o_part)


        sound_part = tk.Frame(sensor_part, bg='black')
        sound_part.grid(row=2,column=8,sticky='NEWS')
        self.set_frame_configure(sound_part)


        sm_part = tk.Frame(sensor_part, bg='black')
        sm_part.grid(row=0,column=10,sticky='NEWS')
        self.set_frame_configure(sm_part)


        rn_part = tk.Frame(sensor_part, bg='black')
        rn_part.grid(row=2,column=10,sticky='NEWS')
        self.set_frame_configure(rn_part)


        nh3_part = tk.Frame(sensor_part, bg='black')
        nh3_part.grid(row=0,column=12,sticky='NEWS')
        self.set_frame_configure(nh3_part)


        o3_part = tk.Frame(sensor_part, bg='black')
        o3_part.grid(row=2,column=12,sticky='NEWS')
        self.set_frame_configure(o3_part)
        
        


        
        # element_button = ttk.Button(
        #     self,
        #     text="to Element",
        #     command=show_element,
        #     cursor="hand2"
        # )
        # element_button.grid(row=0, column=1, sticky="NEWS", pady = (10,0))

        
        def event_func(event, sensor_name):
            show_element()
            controller.sensor_name = sensor_name
            print(sensor_name)
        
        
            
            
        #tvoc_part - contents
        tvoc_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='TVOC'))
        self.set_image(tvoc_part, 'img/sensor/Main-TVOC.png')
        self.set_label(tvoc_part, 'TVOC')

        #co_part - contents
        co_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO'))
        self.set_image(co_part, 'img/sensor/Main-CO.png')
        self.set_label(co_part, 'CO')

        #co2_part - contents
        co2_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO2'))
        self.set_image(co2_part, 'img/sensor/Main-CO2.png')
        self.set_label(co2_part, 'CO2')

        #no2_part - contents
        no2_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='NO2'))
        self.set_image(no2_part, 'img/sensor/Main-NO2.png')
        self.set_label(no2_part, 'NO2')

        #pm25_part - contents
        pm25_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM25'))
        self.set_image(pm25_part, 'img/sensor/Main-PM2.5.png')
        self.set_label(pm25_part, 'PM2.5')

        #h2s_part - contents
        h2s_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='H2S'))
        self.set_image(h2s_part, 'img/sensor/Main-H2S.png')
        self.set_label(h2s_part, 'H2S')

        #pm10_part - contents
        pm10_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM10'))
        self.set_image(pm10_part, 'img/sensor/Main-PM10.png')
        self.set_label(pm10_part, 'PM10')

        #light_part - contents
        light_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='LIGHT'))
        self.set_image(light_part, 'img/sensor/Main-Light.png')
        self.set_label(light_part, 'Light')

        #ch2o_part - contents
        ch2o_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='CH2O'))
        self.set_image(ch2o_part, 'img/sensor/Main-CH2O.png')
        self.set_label(ch2o_part, 'CH2O')

        #sound_part - contents
        sound_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='SOUND'))
        self.set_image(sound_part, 'img/sensor/Main-Sound.png')
        self.set_label(sound_part, 'Sound')

        #sm_part - contents
        sm_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='SM'))
        self.set_image(sm_part, 'img/sensor/Main-Sm.png')
        self.set_label(sm_part, 'Sm')

        #rn_part - contents
        rn_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='RN'))
        self.set_image(rn_part, 'img/sensor/Main-Rn.png')
        self.set_label(rn_part, 'Rn')

        #nh3_part - contents
        nh3_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='NH3'))
        self.set_image(nh3_part, 'img/sensor/Main-NH3.png')
        self.set_label(nh3_part, 'NH3')

        #o3_part - contents
        o3_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='O3'))
        self.set_image(o3_part, 'img/sensor/Main-O3.png')
        self.set_label(o3_part, 'O3')
        
        ########################################### Separator ###########################################
        # horizontal
        self.set_horizontal_separator_image(sensor_part, 0)
        self.set_horizontal_separator_image(sensor_part, 2)
        self.set_horizontal_separator_image(sensor_part, 4)
        self.set_horizontal_separator_image(sensor_part, 6)
        self.set_horizontal_separator_image(sensor_part, 8)
        self.set_horizontal_separator_image(sensor_part, 10)
        self.set_horizontal_separator_image(sensor_part, 12)
        # vertical
        self.set_vertical_separator_image(sensor_part, 1)
        self.set_vertical_separator_image(sensor_part, 3)
        self.set_vertical_separator_image(sensor_part, 5)
        self.set_vertical_separator_image(sensor_part, 7)
        self.set_vertical_separator_image(sensor_part, 9)
        self.set_vertical_separator_image(sensor_part, 11)
        
        
        
        # temp_img = PhotoImage(file='img/parts/Main_V_separator.png')
        # temp_img_label = Label(sensor_part, image=temp_img, bg='black')
        # temp_img_label.image = temp_img
        # temp_img_label.grid(row=1, column=0)


    def set_horizontal_separator_image(self, frame, column):
        sep_h_img = PhotoImage(file='img/parts/Main_H_separator.png')
        sep_h_img_label = Label(frame, image=sep_h_img, bg='black')
        sep_h_img_label.image = sep_h_img
        sep_h_img_label.grid(row=1, column=column, padx=12)
    
    def set_vertical_separator_image(self, frame, column):
        sep_v_img = PhotoImage(file='img/parts/Main_V_separator.png',height=300)
        sep_v_img_label = Label(frame, image=sep_v_img, bg='black')
        sep_v_img_label.image = sep_v_img
        sep_v_img_label.grid(row=0, column=column, rowspan=3)
    
    
    def set_image(self, frame, img_path, row=0, column=0, height=80):
        img = PhotoImage(file=img_path)
        img_label = Label(frame, image=img, bg='black',height=height)
        img_label.image = img
        img_label.grid(row=row, column=column)
        
        
    def set_frame_configure(self, frame):
            frame.columnconfigure(0, weight=1)
            frame.rowconfigure(0,weight=2)
            frame.rowconfigure(1,weight=2)
            frame.rowconfigure(2,weight=1)

    def set_label(self, frame, title,row=2, column=0, font_size=15):
        common_label = Label(frame, text=title, bg='black', fg='white', font=('Arial',font_size))
        common_label.grid(row=row, column=column, sticky="NEWS")

    def time_update(self):
        time_string = strftime('%Y %m %D %H:%M:%S %p')
        self.time_label.config(text=time_string)
        self.time_label.after(1000, self.time_update)