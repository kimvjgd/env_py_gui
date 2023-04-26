import tkinter as tk
from tkinter import ttk
from tkinter import *
from datetime import datetime
from time import strftime
import uart_data_thread



class Home(ttk.Frame):
    def __init__(self, parent, controller, show_element, show_wifi, temperature):
        super().__init__(parent)
        
        self.TVOC = 0.0
        # self.TVOC = tk.StringVar(value=123)
        self.CO2 = 0.0
        self.PM25 = 0.0
        self.PM10 = 0.0
        self.CH2O = 0.0
        self.Sm = 0.0
        self.NH3 = 0.0
        self.CO = 0.0
        self.NO2 = 0.0
        self.H2S = 0.0
        self.LIGHT = 0.0
        self.SOUND = 0.0
        self.Rn = 0.0
        self.O3 = 0.0
        self.temperature = temperature
        # self.temperature = tk.StringVar(value=37.5)
        self.humidity = 0.0
        
        
        # self.time_update()
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
        # self.set_label(temp_hum_part, self.temperature, row=0, column=1)
        self.temp_label = Label(temp_hum_part, text=self.temperature, bg='black', fg='white', font=('Arial', 15))
        self.temp_label.grid(row=0, column=1, sticky='NEWS')
        self.set_image(temp_hum_part, 'img/temperature/temp5.png', row=0, column=2, height=20)

        # humidity
        self.set_image(temp_hum_part, 'img/humidity/humidity_img.png', row=0, column=3, height=40)
        # self.set_label(temp_hum_part, '53%', row=0, column=4)
        self.humidity_label = Label(temp_hum_part, text=self.humidity, bg='black', fg='white', font=('Arial', 15))
        self.humidity_label.grid(row=0, column=4, sticky='NEWS')
        self.set_image(temp_hum_part, 'img/humidity/humidity5.png', row=0, column=5, height=20)
        
        
        
        
        # sensor values
        tvoc_part = tk.Frame(sensor_part,bg="black")
        tvoc_part.grid(row=0,column=0,sticky='NEWS')
        self.set_frame_configure(tvoc_part)
        self.TVOC_label = Label(tvoc_part, text=self.TVOC, bg='black', fg='white', font=('Arial', 15))
        self.TVOC_label.grid(row=1, column=0, sticky='NEWS')
        
        
        co_part = tk.Frame(sensor_part, bg='black')
        co_part.grid(row=2,column=0,sticky='NEWS')
        self.set_frame_configure(co_part)
        self.CO_label = Label(co_part, text=self.CO, bg='black', fg='white', font=('Arial', 15))
        self.CO_label.grid(row=1, column=0, sticky='NEWS')
        

        co2_part = tk.Frame(sensor_part, bg='black')
        co2_part.grid(row=0,column=2,sticky='NEWS')
        self.set_frame_configure(co2_part)
        self.CO2_label = Label(co2_part, text=self.CO2, bg='black', fg='white', font=('Arial', 15))
        self.CO2_label.grid(row=1, column=0, sticky='NEWS')

        no2_part = tk.Frame(sensor_part, bg='black')
        no2_part.grid(row=2,column=2,sticky='NEWS')
        self.set_frame_configure(no2_part)
        self.NO2_label = Label(no2_part, text=self.NO2, bg='black', fg='white', font=('Arial', 15))
        self.NO2_label.grid(row=1, column=0, sticky='NEWS')

        pm25_part = tk.Frame(sensor_part, bg='black')
        pm25_part.grid(row=0,column=4,sticky='NEWS')
        self.set_frame_configure(pm25_part)
        self.PM25_label = Label(pm25_part, text=self.PM25, bg='black', fg='white', font=('Arial', 15))
        self.PM25_label.grid(row=1, column=0, sticky='NEWS')

        h2s_part = tk.Frame(sensor_part, bg='black')
        h2s_part.grid(row=2,column=4,sticky='NEWS')
        self.set_frame_configure(h2s_part)
        self.H2S_label = Label(h2s_part, text=self.H2S, bg='black', fg='white', font=('Arial', 15))
        self.H2S_label.grid(row=1, column=0, sticky='NEWS')

        pm10_part = tk.Frame(sensor_part, bg='black')
        pm10_part.grid(row=0,column=6,sticky='NEWS')
        self.set_frame_configure(pm10_part)
        self.PM10_label = Label(pm10_part, text=self.PM10, bg='black', fg='white', font=('Arial', 15))
        self.PM10_label.grid(row=1, column=0, sticky='NEWS')

        light_part = tk.Frame(sensor_part, bg='black')
        light_part.grid(row=2,column=6,sticky='NEWS')
        self.set_frame_configure(light_part)
        self.Light_label = Label(light_part, text=self.LIGHT, bg='black', fg='white', font=('Arial', 15))
        self.Light_label.grid(row=1, column=0, sticky='NEWS')

        ch2o_part = tk.Frame(sensor_part, bg='black')
        ch2o_part.grid(row=0,column=8,sticky='NEWS')
        self.set_frame_configure(ch2o_part)
        self.CH2O_label = Label(ch2o_part, text=self.CH2O, bg='black', fg='white', font=('Arial', 15))
        self.CH2O_label.grid(row=1, column=0, sticky='NEWS')



        sound_part = tk.Frame(sensor_part, bg='black')
        sound_part.grid(row=2,column=8,sticky='NEWS')
        self.set_frame_configure(sound_part)
        self.Sound_label = Label(sound_part, text=self.SOUND, bg='black', fg='white', font=('Arial', 15))
        self.Sound_label.grid(row=1, column=0, sticky='NEWS')



        sm_part = tk.Frame(sensor_part, bg='black')
        sm_part.grid(row=0,column=10,sticky='NEWS')
        self.set_frame_configure(sm_part)
        self.Sm_label = Label(sm_part, text=self.Sm, bg='black', fg='white', font=('Arial', 15))
        self.Sm_label.grid(row=1, column=0, sticky='NEWS')


        rn_part = tk.Frame(sensor_part, bg='black')
        rn_part.grid(row=2,column=10,sticky='NEWS')
        self.set_frame_configure(rn_part)
        self.Rn_label = Label(rn_part, text=self.Rn, bg='black', fg='white', font=('Arial', 15))
        self.Rn_label.grid(row=1, column=0, sticky='NEWS')


        nh3_part = tk.Frame(sensor_part, bg='black')
        nh3_part.grid(row=0,column=12,sticky='NEWS')
        self.set_frame_configure(nh3_part)
        self.NH3_label = Label(nh3_part, text=self.NH3, bg='black', fg='white', font=('Arial', 15))
        self.NH3_label.grid(row=1, column=0, sticky='NEWS')


        o3_part = tk.Frame(sensor_part, bg='black')
        o3_part.grid(row=2,column=12,sticky='NEWS')
        self.set_frame_configure(o3_part)
        self.O3_label = Label(o3_part, text=self.O3, bg='black', fg='white', font=('Arial', 15))
        self.O3_label.grid(row=1, column=0, sticky='NEWS')
        
        


        
        # element_button = ttk.Button(
        #     self,
        #     text="to Element",
        #     command=show_element,
        #     cursor="hand2"
        # )
        # element_button.grid(row=0, column=1, sticky="NEWS", pady = (10,0))

        
        
        def event_func(event, sensor_name):
            # 순서 바꾸면 안돼!!!!
            controller.sensor_name = sensor_name
            show_element()
        
        
            
            
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
            frame.rowconfigure(1,weight=1)
            frame.rowconfigure(2,weight=1)
            frame.rowconfigure(3,weight=1)

    def set_label(self, frame, title,row=2, column=0, font_size=15):
        common_label = Label(frame, text=title, bg='black', fg='white', font=('Arial',font_size))
        common_label.grid(row=row, column=column, sticky="NEWS")

    def time_update(self):
        time_string = strftime('%Y %m %D %H:%M:%S %p')
        self.time_label.config(text=time_string)
        self.time_label.after(1000, self.time_update)
        # print(uart_data_thread.TVOC)
    
    def get_all_data(self):
        self.temperature = self.controller.temperature
        self.temp_label.config(text=self.temperature)
        self.humidity = self.controller.humidity
        self.humidity_label.config(text=self.humidity)
        # 밑에 마저 해야한다.
        self.TVOC = self.controller.TVOC
        self.TVOC_label.config(text=self.TVOC)
        
        self.CO2 = self.controller.CO2
        self.CO2_label.config(text=self.CO2)
        
        self.PM25 = self.controller.PM25
        self.PM25_label.config(text=self.PM25)
        
        self.PM10 = self.controller.PM10
        self.PM10_label.config(text=self.PM10)
        
        self.CH2O = self.controller.CH2O
        self.CH2O_label.config(text=self.CH2O)
        
        self.Sm = self.controller.Sm
        self.Sm_label.config(text=self.Sm)
        
        self.NH3 = self.controller.NH3
        self.NH3_label.config(text=self.NH3)
        
        self.CO = self.controller.CO
        self.CO_label.config(text=self.CO)
        
        self.NO2 = self.controller.NO2
        self.NO2_label.config(text=self.NO2)
        
        self.H2S = self.controller.H2S
        self.H2S_label.config(text=self.H2S)
        
        self.LIGHT = self.controller.LIGHT
        self.Light_label.config(text=self.LIGHT)
        
        self.SOUND = self.controller.SOUND
        self.Sound_label.config(text=self.SOUND)
        
        self.Rn = self.controller.Rn
        self.Rn_label.config(text=self.Rn)
        
        self.O3 = self.controller.O3
        self.O3_label.config(text=self.O3)
        
        
        
        self.after(1000, self.get_all_data)
        # self.temp_label.after(1000, self.get_temperature, temperature)      # 맨뒤에 매개변수를 계속 넣어줘야해!!!!
        

    # def get_one_data(self, TVOC):
    #     self.TVOC = TVOC
    #     print('Right reception')
    #     print('TVOC : ', self.TVOC)
    #     print('global TVOC : ', uart_data_thread.TVOC)

    #     # 일단 time_label은 임시로 썼다@
    #     self.time_label.after(1000, self.get_one_data, TVOC)
    