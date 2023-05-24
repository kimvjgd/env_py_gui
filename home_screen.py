import tkinter as tk
from tkinter import ttk
from tkinter import *
from datetime import datetime
from time import strftime
from PIL import Image, ImageTk
import sys
from wifi_func import get_current_connection_state
import paho.mqtt.client as mqtt
import os
import json
import math
from sensor_list import SENSOR_DICT


THINGSBOARD_HOST = "210.117.143.37"
ACCESS_TOKEN='51ZFhNEWFXLi4pW758Gy'
port = 10061
# temp
sensor_data = {
        "values":{
                "S_0_0":0,
                "S_0_1":0,
                "S_0_2":0,
                "S_0_3":0,
                "S_0_4":0,
                "S_0_5":0,
                "S_0_6":0,
                "S_0_7":0,
                "S_0_8":0,
                "S_0_9":0,
                "S_0_10":0,
                "S_0_11":0,
                "S_0_12":0,
                "S_0_13":0,
                }}

class Home(ttk.Frame):
    def __init__(self, parent, controller, show_element, show_wifi, show_info, show_ethernet):
        super().__init__(parent)
        
        self.controller = controller
        self.show_wifi = show_wifi
        self.show_ethernet = show_ethernet
        
        self.TVOC = 0.0
        # self.TVOC = tk.StringVar(value=123)
        self.CO2 = 0.0
        self.PM1 = 0.0
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
        self.temperature = 0.0
        self.humidity = 0.0
        self.lan_state = 'wlan'         # wlan or ethernet or non_connection    <-    나중에 시간되면 class로 뺴서 enum으로 만들자
        self.pre_lan_state = 'wlan'                     # 하드 코딩의 묘미//
        self.client = mqtt.Client()
        self.client.username_pw_set(ACCESS_TOKEN)
        self.client.connect(THINGSBOARD_HOST, port, 60)
        self.client.loop_start()
        
        # self.time_update()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=5)
        
        
        # status (upper)
        status_part = tk.Frame(self, bg="black")
        status_part.grid(row=0, column=0, sticky="NEWS")
        status_part.columnconfigure(0, weight=10)
        status_part.columnconfigure(1, weight=1)
        status_part.columnconfigure(2, weight=1)
        status_part.columnconfigure(3, weight=1)
        status_part.columnconfigure(4, weight=1)                        # For MQTT send - gonna be erased soon
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
        
        non_connection_status_img = Image.open('img/wifi/non_connection.png')
        resized_non_connection_status_img = non_connection_status_img.resize((20, 20), Image.ANTIALIAS)
        self.photo_non_connection_status = ImageTk.PhotoImage(resized_non_connection_status_img)
        
        
        wifi_connection_status_img = Image.open('img/wifi/strength/wifi_strength_4.png')
        resized_wifi_connection_status_img = wifi_connection_status_img.resize((20, 20), Image.ANTIALIAS)
        self.photo_wifi_connection_status = ImageTk.PhotoImage(resized_wifi_connection_status_img)
        
        ethernet_connection_status_img = Image.open('img/wifi/ethernet.png')
        resized_ethernet_connection_status_img = ethernet_connection_status_img.resize((20, 20), Image.ANTIALIAS)
        self.photo_ethernet_connection_status = ImageTk.PhotoImage(resized_ethernet_connection_status_img)
        
        

        # wifi_image = tk.PhotoImage(file='img/wifi/wifi.png')
        quit_image = tk.PhotoImage(file='img/parts/back_button.png')
        
        
        # Temporary Quit Button for DEBUG!!!!!!!!!!
        quit_button = tk.Button(status_part, image=quit_image, command=controller.destroy, height=20, width=20)
        quit_button.image = quit_image                  # to keep a ref
        quit_button.grid(column=1,row=0)

        self.wifi_button = tk.Button(status_part, image=self.photo_wifi_connection_status,highlightthickness=0, command=show_wifi, height=20, width=20, bg='black', bd=0, borderwidth=0)
        self.wifi_button.image = self.photo_wifi_connection_status                  # to keep a ref
        self.wifi_button.grid(column=2,row=0)
        
        
        # Info Screen
        # info_button = tk.Button(status_part, image=info_image, command=show_info, height=20, width=20)
        # info_button.image = info_image                  # to keep a ref
        # info_button.grid(column=3,row=0)
        info_button = self.get_image_instance(status_part, 'img/wifi/info.png', 20, 20, 0, 3, 'NEWS', command=show_info)

        
        # Temporary MQTT Button for DEBUG!!!!!!!!!!
        mqtt_button = tk.Button(status_part,bg='red',image=quit_image,highlightthickness=0, command=self.send_mqtt_data, height=20, width=20, bd=0, borderwidth=0)
        mqtt_button.grid(column=4,row=0)
        
        
        # temperature & humidity
        
        # temperature
        # self.set_image(temp_hum_part, 'img/temperature/temp_img.png', row=0, column=0, height=40)
        self.get_image(temp_hum_part,'img/temperature/temp_img.png', 35, 35, 0, 0, 'NEWS')
        # self.set_label(temp_hum_part, self.temperature, row=0, column=1)
        self.temp_label = Label(temp_hum_part, text=self.temperature, bg='black', fg='white', font=('Arial', 15))
        self.temp_label.grid(row=0, column=1, sticky='NEWS')
        # self.set_image(temp_hum_part, 'img/temperature/temp5.png', row=0, column=2, height=20)
        self.get_image(temp_hum_part,'img/temperature/temp5.png', 240, 35, 0, 2, 'NEWS')


        # humidity
        # self.set_image(temp_hum_part, 'img/humidity/humidity_img.png', row=0, column=3, height=40)
        self.get_image(temp_hum_part,'img/humidity/humidity_img.png', 35, 35, 0, 3, 'NEWS')
        # self.set_label(temp_hum_part, '53%', row=0, column=4)
        self.humidity_label = Label(temp_hum_part, text=self.humidity, bg='black', fg='white', font=('Arial', 15))
        self.humidity_label.grid(row=0, column=4, sticky='NEWS')
        # self.set_image(temp_hum_part, 'img/humidity/humidity5.png', row=0, column=5, height=20)
        self.get_image(temp_hum_part,'img/humidity/humidity5.png', 240, 35, 0, 5, 'NEWS')
        
        
        
        
        # sensor values
        tvoc_part = tk.Frame(sensor_part,bg="black")
        tvoc_part.grid(row=0,column=0,sticky='NEWS')
        self.set_frame_configure(tvoc_part)
        self.TVOC_label = Label(tvoc_part, text=self.TVOC, bg='black', fg='white', font=('Arial', 15))
        self.TVOC_label.grid(row=1, column=0, sticky='NEWS')
        self.TVOC_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='TVOC'))
        self.TVOC_unit_label = Label(tvoc_part, text='ug/m3', bg='black', fg='white', font=('Arial', 11))
        self.TVOC_unit_label.grid(row=2,column=0)

        
        
        co_part = tk.Frame(sensor_part, bg='black')
        co_part.grid(row=2,column=0,sticky='NEWS')
        self.set_frame_configure(co_part)
        self.CO_label = Label(co_part, text=self.CO, bg='black', fg='white', font=('Arial', 15))
        self.CO_label.grid(row=1, column=0, sticky='NEWS')
        self.CO_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO'))
        self.CO_unit_label = Label(co_part, text='PPM', bg='black', fg='white', font=('Arial', 11))
        self.CO_unit_label.grid(row=2,column=0)
        

        co2_part = tk.Frame(sensor_part, bg='black')
        co2_part.grid(row=0,column=2,sticky='NEWS')
        self.set_frame_configure(co2_part)
        self.CO2_label = Label(co2_part, text=self.CO2, bg='black', fg='white', font=('Arial', 15))
        self.CO2_label.grid(row=1, column=0, sticky='NEWS')
        self.CO2_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO2'))
        self.CO2_unit_label = Label(co2_part, text='PPM', bg='black', fg='white', font=('Arial', 11))
        self.CO2_unit_label.grid(row=2,column=0)
        
        no2_part = tk.Frame(sensor_part, bg='black')
        no2_part.grid(row=2,column=2,sticky='NEWS')
        self.set_frame_configure(no2_part)
        self.NO2_label = Label(no2_part, text=self.NO2, bg='black', fg='white', font=('Arial', 15))
        self.NO2_label.grid(row=1, column=0, sticky='NEWS')
        self.NO2_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='NO2'))
        self.NO2_unit_label = Label(no2_part, text='PPM', bg='black', fg='white', font=('Arial', 11))
        self.NO2_unit_label.grid(row=2,column=0)
        
        pm25_part = tk.Frame(sensor_part, bg='black')
        pm25_part.grid(row=0,column=4,sticky='NEWS')
        # self.set_frame_configure(pm25_part)
        pm25_part.columnconfigure(0, weight=1)
        pm25_part.rowconfigure(0,weight=2)
        pm25_part.rowconfigure(1,weight=1)
        pm25_part.rowconfigure(2,weight=1)
        pm25_part.rowconfigure(3,weight=1)
        pm25_part.rowconfigure(4,weight=1)
        
        

        self.PM1_label = Label(pm25_part, text=self.PM25, bg='black', fg='white', font=('Arial', 12))
        self.PM1_label.grid(row=1, column=0, sticky='NEWS')
        
        self.PM25_label = Label(pm25_part, text=self.PM25, bg='black', fg='white', font=('Arial', 12))
        self.PM25_label.grid(row=2, column=0, sticky='NEWS')
        
        self.PM25_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM25'))
        self.PM25_unit_label = Label(pm25_part, text='ug/m3', bg='black', fg='white', font=('Arial', 11))
        self.PM25_unit_label.grid(row=3,column=0)

        h2s_part = tk.Frame(sensor_part, bg='black')
        h2s_part.grid(row=2,column=4,sticky='NEWS')
        self.set_frame_configure(h2s_part)
        self.H2S_label = Label(h2s_part, text=self.H2S, bg='black', fg='white', font=('Arial', 15))
        self.H2S_label.grid(row=1, column=0, sticky='NEWS')
        self.H2S_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='H2S'))
        self.H2S_unit_label = Label(h2s_part, text='PPM', bg='black', fg='white', font=('Arial', 11))
        self.H2S_unit_label.grid(row=2,column=0)

        pm10_part = tk.Frame(sensor_part, bg='black')
        pm10_part.grid(row=0,column=6,sticky='NEWS')
        self.set_frame_configure(pm10_part)
        self.PM10_label = Label(pm10_part, text=self.PM10, bg='black', fg='white', font=('Arial', 15))
        self.PM10_label.grid(row=1, column=0, sticky='NEWS')
        self.PM10_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM10'))
        self.PM10_unit_label = Label(pm10_part, text='ug/m3', bg='black', fg='white', font=('Arial', 11))
        self.PM10_unit_label.grid(row=2,column=0)

        light_part = tk.Frame(sensor_part, bg='black')
        light_part.grid(row=2,column=6,sticky='NEWS')
        self.set_frame_configure(light_part)
        self.Light_label = Label(light_part, text=self.LIGHT, bg='black', fg='white', font=('Arial', 15))
        self.Light_label.grid(row=1, column=0, sticky='NEWS')
        self.Light_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='LIGHT'))
        self.Light_unit_label = Label(light_part, text='Lux', bg='black', fg='white', font=('Arial', 11))
        self.Light_unit_label.grid(row=2,column=0)
        

        ch2o_part = tk.Frame(sensor_part, bg='black')
        ch2o_part.grid(row=0,column=8,sticky='NEWS')
        self.set_frame_configure(ch2o_part)
        self.CH2O_label = Label(ch2o_part, text=self.CH2O, bg='black', fg='white', font=('Arial', 15))
        self.CH2O_label.grid(row=1, column=0, sticky='NEWS')
        self.CH2O_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CH2O'))
        self.CH2O_unit_label = Label(ch2o_part, text='ug/m3', bg='black', fg='white', font=('Arial', 11))
        self.CH2O_unit_label.grid(row=2,column=0)



        sound_part = tk.Frame(sensor_part, bg='black')
        sound_part.grid(row=2,column=8,sticky='NEWS')
        self.set_frame_configure(sound_part)
        self.Sound_label = Label(sound_part, text=self.SOUND, bg='black', fg='white', font=('Arial', 15))
        self.Sound_label.grid(row=1, column=0, sticky='NEWS')
        self.Sound_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='SOUND'))
        self.Sound_unit_label = Label(sound_part, text='dB', bg='black', fg='white', font=('Arial', 11))
        self.Sound_unit_label.grid(row=2,column=0)



        sm_part = tk.Frame(sensor_part, bg='black')
        sm_part.grid(row=0,column=10,sticky='NEWS')
        self.set_frame_configure(sm_part)
        self.Sm_label = Label(sm_part, text=self.Sm, bg='black', fg='white', font=('Arial', 15))
        self.Sm_label.grid(row=1, column=0, sticky='NEWS')
        self.Sm_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='SM'))
        self.Sm_unit_label = Label(sm_part, text='PPM', bg='black', fg='white', font=('Arial', 11))
        self.Sm_unit_label.grid(row=2,column=0)


        rn_part = tk.Frame(sensor_part, bg='black')
        rn_part.grid(row=2,column=10,sticky='NEWS')
        self.set_frame_configure(rn_part)
        self.Rn_label = Label(rn_part, text=self.Rn, bg='black', fg='white', font=('Arial', 15))
        self.Rn_label.grid(row=1, column=0, sticky='NEWS')
        self.Rn_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='RN'))
        self.Rn_unit_label = Label(rn_part, text='Bq/m3', bg='black', fg='white', font=('Arial', 11))
        self.Rn_unit_label.grid(row=2,column=0)


        nh3_part = tk.Frame(sensor_part, bg='black')
        nh3_part.grid(row=0,column=12,sticky='NEWS')
        self.set_frame_configure(nh3_part)
        self.NH3_label = Label(nh3_part, text=self.NH3, bg='black', fg='white', font=('Arial', 15))
        self.NH3_label.grid(row=1, column=0, sticky='NEWS')
        self.NH3_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='NH3'))
        self.NH3_unit_label = Label(nh3_part, text='PPM', bg='black', fg='white', font=('Arial', 11))
        self.NH3_unit_label.grid(row=2,column=0)


        o3_part = tk.Frame(sensor_part, bg='black')
        o3_part.grid(row=2,column=12,sticky='NEWS')
        self.set_frame_configure(o3_part)
        self.O3_label = Label(o3_part, text=self.O3, bg='black', fg='white', font=('Arial', 15))
        self.O3_label.grid(row=1, column=0, sticky='NEWS')
        self.O3_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='O3'))
        self.O3_unit_label = Label(o3_part, text='O3', bg='black', fg='white', font=('Arial', 11))
        self.O3_unit_label.grid(row=2,column=0)
        
        


        
        # element_button = ttk.Button(
        #     self,
        #     text="to Element",
        #     command=show_element,
        #     cursor="hand2"
        # )
        # element_button.grid(row=0, column=1, sticky="NEWS", pady = (10,0))

        
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################

        def event_func(event, sensor_name, sensor_value):
            # 순서 바꾸면 안돼!!!!
        #     print('Value : ', end='')
        #     print(sensor_value)
        #     print('Range : ', end='')
        #     print(SENSOR_DICT[sensor_name][2:5])
            controller.sensor_name = sensor_name
            controller.selected_sensor_range = SENSOR_DICT[sensor_name][2:5]
            show_element()
            
        
        
            
###########################################################################################################            
        #tvoc_part - contents
        
        tvoc_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='TVOC', sensor_value=self.controller.TVOC))
        # self.set_image(tvoc_part, 'img/sensor/Main-TVOC.png')
        # self.set_label(tvoc_part, 'TVOC')

        tvoc_img = PhotoImage(file='img/sensor/Main-TVOC.png')
        tvoc_img_label = Label(tvoc_part, image=tvoc_img, bg='black', height=80)
        tvoc_img_label.image = tvoc_img
        tvoc_img_label.grid(row=0, column=0)
        tvoc_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='TVOC', sensor_value=self.controller.TVOC))

        tvoc_label = Label(tvoc_part, text='TVOC', bg='black', fg='white', font=('Arial', 15))
        tvoc_label.grid(row=3, column=0, sticky='NEWS')
        tvoc_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='TVOC', sensor_value=self.controller.TVOC))
###########################################################################################################
        #co_part - contents

        co_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO', sensor_value=self.controller.CO))
        # self.set_image(co_part, 'img/sensor/Main-CO.png')
        # self.set_label(co_part, 'CO')

        co_img = PhotoImage(file='img/sensor/Main-CO.png')
        co_img_label = Label(co_part, image=co_img, bg='black', height=80)
        co_img_label.image = co_img
        co_img_label.grid(row=0, column=0)
        co_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO', sensor_value=self.controller.CO))

        co_label = Label(co_part, text='CO', bg='black', fg='white', font=('Arial', 15))
        co_label.grid(row=3, column=0, sticky='NEWS')
        co_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO', sensor_value=self.controller.CO))
###########################################################################################################
        #co2_part - contents

        co2_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO2',sensor_value=self.controller.CO2))
        # self.set_image(co2_part, 'img/sensor/Main-CO2.png')
        # self.set_label(co2_part, 'CO2')

        co2_img = PhotoImage(file='img/sensor/Main-CO2.png')
        co2_img_label = Label(co2_part, image=co2_img, bg='black', height=80)
        co2_img_label.image = co2_img
        co2_img_label.grid(row=0, column=0)
        co2_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO2',sensor_value=self.controller.CO2))

        co2_label = Label(co2_part, text='CO2', bg='black', fg='white', font=('Arial', 15))
        co2_label.grid(row=3, column=0, sticky='NEWS')
        co2_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO2',sensor_value=self.controller.CO2))
###########################################################################################################
        #no2_part - contents

        no2_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='NO2', sensor_value=self.controller.NO2))
        # self.set_image(no2_part, 'img/sensor/Main-NO2.png')
        # self.set_label(no2_part, 'NO2')

        no2_img = PhotoImage(file='img/sensor/Main-NO2.png')
        no2_img_label = Label(no2_part, image=no2_img, bg='black', height=80)
        no2_img_label.image = no2_img
        no2_img_label.grid(row=0, column=0)
        no2_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='NO2', sensor_value=self.controller.NO2))

        no2_label = Label(no2_part, text='NO2', bg='black', fg='white', font=('Arial', 15))
        no2_label.grid(row=3, column=0, sticky='NEWS')
        no2_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='NO2', sensor_value=self.controller.NO2))
###########################################################################################################
        #pm25_part - contents

        pm25_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM25', sensor_value=self.controller.PM25))
        # self.set_image(pm25_part, 'img/sensor/Main-PM2.5.png')
        # self.set_label(pm25_part, 'PM2.5')

        pm25_img = PhotoImage(file='img/sensor/Main-PM2.5.png')
        pm25_img_label = Label(pm25_part, image=pm25_img, bg='black', height=80)
        pm25_img_label.image = pm25_img
        pm25_img_label.grid(row=0, column=0)
        pm25_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM25', sensor_value=self.controller.PM25))

        pm25_label = Label(pm25_part, text='PM1.0, 2.5', bg='black', fg='white', font=('Arial', 12))
        pm25_label.grid(row=4, column=0, sticky='NEWS')
        pm25_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM25', sensor_value=self.controller.PM25))
###########################################################################################################
        #h2s_part - contents

        h2s_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='H2S', sensor_value=self.controller.H2S))
        # self.set_image(h2s_part, 'img/sensor/Main-H2S.png')
        # self.set_label(h2s_part, 'H2S')

        h2s_img = PhotoImage(file='img/sensor/Main-H2S.png')
        h2s_img_label = Label(h2s_part, image=h2s_img, bg='black', height=80)
        h2s_img_label.image = h2s_img
        h2s_img_label.grid(row=0, column=0)
        h2s_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='H2S', sensor_value=self.controller.H2S))

        h2s_label = Label(h2s_part, text='H2S', bg='black', fg='white', font=('Arial', 15))
        h2s_label.grid(row=3, column=0, sticky='NEWS')
        h2s_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='H2S', sensor_value=self.controller.H2S))
###########################################################################################################
        #pm10_part - contents

        pm10_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM10', sensor_value=self.controller.PM10))
        # self.set_image(pm10_part, 'img/sensor/Main-PM10.png')
        # self.set_label(pm10_part, 'PM10')

        pm10_img = PhotoImage(file='img/sensor/Main-PM10.png')
        pm10_img_label = Label(pm10_part, image=pm10_img, bg='black', height=80)
        pm10_img_label.image = pm10_img
        pm10_img_label.grid(row=0, column=0)
        pm10_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM10', sensor_value=self.controller.PM10))

        pm10_label = Label(pm10_part, text='PM10', bg='black', fg='white', font=('Arial', 15))
        pm10_label.grid(row=3, column=0, sticky='NEWS')
        pm10_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM10', sensor_value=self.controller.PM10))
###########################################################################################################
        #light_part - contents

        light_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='LIGHT', sensor_value=self.controller.LIGHT))
        # self.set_image(light_part, 'img/sensor/Main-Light.png')
        # self.set_label(light_part, 'Light')

        light_img = PhotoImage(file='img/sensor/Main-Light.png')
        light_img_label = Label(light_part, image=light_img, bg='black', height=80)
        light_img_label.image = light_img
        light_img_label.grid(row=0, column=0)
        light_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='LIGHT', sensor_value=self.controller.LIGHT))

        light_label = Label(light_part, text='Light', bg='black', fg='white', font=('Arial', 15))
        light_label.grid(row=3, column=0, sticky='NEWS')
        light_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='LIGHT', sensor_value=self.controller.LIGHT))
###########################################################################################################
        #ch2o_part - contents

        ch2o_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='CH2O', sensor_value=self.controller.CH2O))
        # self.set_image(ch2o_part, 'img/sensor/Main-CH2O.png')
        # self.set_label(ch2o_part, 'CH2O')

        CH2O_img = PhotoImage(file='img/sensor/Main-CH2O.png')
        CH2O_img_label = Label(ch2o_part, image=CH2O_img, bg='black', height=80)
        CH2O_img_label.image = CH2O_img
        CH2O_img_label.grid(row=0, column=0)
        CH2O_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CH2O', sensor_value=self.controller.CH2O))

        CH2O_label = Label(ch2o_part, text='CH2O', bg='black', fg='white', font=('Arial', 15))
        CH2O_label.grid(row=3, column=0, sticky='NEWS')
        CH2O_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CH2O', sensor_value=self.controller.CH2O))
###########################################################################################################
        #sound_part - contents

        sound_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='SOUND', sensor_value=self.controller.SOUND))
        # self.set_image(sound_part, 'img/sensor/Main-Sound.png')
        # self.set_label(sound_part, 'Sound')

        sound_img = PhotoImage(file='img/sensor/Main-Sound.png')
        sound_img_label = Label(sound_part, image=sound_img, bg='black', height=80)
        sound_img_label.image = sound_img
        sound_img_label.grid(row=0, column=0)
        sound_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='SOUND', sensor_value=self.controller.SOUND))

        sound_label = Label(sound_part, text='Sound', bg='black', fg='white', font=('Arial', 15))
        sound_label.grid(row=3, column=0, sticky='NEWS')
        sound_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='SOUND', sensor_value=self.controller.SOUND))
###########################################################################################################
        #sm_part - contents

        sm_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='SM', sensor_value=self.controller.SM))
        # self.set_image(sm_part, 'img/sensor/Main-Sm.png')
        # self.set_label(sm_part, 'Sm')

        Sm_img = PhotoImage(file='img/sensor/Main-Sm.png')
        Sm_img_label = Label(sm_part, image=Sm_img, bg='black', height=80)
        Sm_img_label.image = Sm_img
        Sm_img_label.grid(row=0, column=0)
        Sm_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='SM', sensor_value=self.controller.SM))

        Sm_label = Label(sm_part, text='Sm', bg='black', fg='white', font=('Arial', 15))
        Sm_label.grid(row=3, column=0, sticky='NEWS')
        Sm_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='SM', sensor_value=self.controller.SM))
###########################################################################################################
        #rn_part - contents

        rn_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='RN', sensor_value=self.controller.RN))
        # self.set_image(rn_part, 'img/sensor/Main-Rn.png')
        # self.set_label(rn_part, 'Rn')

        Rn_img = PhotoImage(file='img/sensor/Main-Rn.png')
        Rn_img_label = Label(rn_part, image=Rn_img, bg='black', height=80)
        Rn_img_label.image = Rn_img
        Rn_img_label.grid(row=0, column=0)
        Rn_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='RN', sensor_value=self.controller.RN))

        Rn_label = Label(rn_part, text='Rn', bg='black', fg='white', font=('Arial', 15))
        Rn_label.grid(row=3, column=0, sticky='NEWS')
        Rn_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='RN', sensor_value=self.controller.RN))
###########################################################################################################
        #nh3_part - contents

        nh3_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='NH3', sensor_value=self.controller.NH3))
        # self.set_image(nh3_part, 'img/sensor/Main-NH3.png')
        # self.set_label(nh3_part, 'NH3')

        NH3_img = PhotoImage(file='img/sensor/Main-NH3.png')
        NH3_img_label = Label(nh3_part, image=NH3_img, bg='black', height=80)
        NH3_img_label.image = NH3_img
        NH3_img_label.grid(row=0, column=0)
        NH3_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='NH3', sensor_value=self.controller.NH3))

        NH3_label = Label(nh3_part, text='NH3', bg='black', fg='white', font=('Arial', 15))
        NH3_label.grid(row=3, column=0, sticky='NEWS')
        NH3_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='NH3', sensor_value=self.controller.NH3))
###########################################################################################################
        #o3_part - contents

        o3_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='O3', sensor_value=self.controller.O3))
        # self.set_image(o3_part, 'img/sensor/Main-O3.png')
        # self.set_label(o3_part, 'O3')

        O3_img = PhotoImage(file='img/sensor/Main-O3.png')
        O3_img_label = Label(o3_part, image=O3_img, bg='black', height=80)
        O3_img_label.image = O3_img
        O3_img_label.grid(row=0, column=0)
        O3_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='O3', sensor_value=self.controller.O3))

        O3_label = Label(o3_part, text='O3', bg='black', fg='white', font=('Arial', 15))
        O3_label.grid(row=3, column=0, sticky='NEWS')
        O3_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='O3', sensor_value=self.controller.O3))
###########################################################################################################  
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
        sep_v_img = PhotoImage(file='img/parts/Main_V_separator.png',height=350)
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
        # time_string = strftime('%Y-%m-%d %H:%M:%S')
        time_string = strftime('%Y-%m-%d %H:%M')
        self.time_label.config(text=time_string)
        self.time_label.after(1000, self.time_update)
    
    def lan_connection_update(self):
        connection_state = get_current_connection_state()                       # [ethernet, wlan] <- False(미연결) & True(연결)
        # print(connection_state)                                                 # ex) [False, True] -> wlan 연결 [True, True] -> wlan무시 ethernet연결
        if connection_state[0] == True:         # ethernet mode
                self.lan_state = 'ethernet'                                     # todo : enum으로 나중에 빼면 좋음
                # self.wifi_button.config(image='img/',command=None)
                if self.pre_lan_state != self.lan_state:
                        self.wifi_button.config(image=self.photo_ethernet_connection_status, command=self.show_ethernet)
                        self.wifi_button.image = self.photo_ethernet_connection_status

                        
                self.pre_lan_state = 'ethernet'
        elif connection_state[0] == False and connection_state[1] == True:              # wifi 연결
                self.lan_state = 'wlan'
                if self.pre_lan_state != self.lan_state:
                        self.wifi_button.config(image=self.photo_wifi_connection_status, command=self.show_wifi)
                        self.wifi_button.image = self.photo_wifi_connection_status
                        
                self.pre_lan_state = 'wlan'
        elif connection_state[0] == False and connection_state[1] == False:
                self.lan_state = 'none'
                if self.pre_lan_state != self.lan_state:
                        self.wifi_button.config(image=self.photo_non_connection_status, command=self.show_wifi)
                        self.wifi_button.image = self.photo_non_connection_status
                self.pre_lan_state = 'none'
        # print(self.lan_state)
        self.after(3000, self.lan_connection_update)
        
    def get_image_instance(self, frame, path, width, height, row, column,sticky, command=None):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Label(frame, image=photo_img, bg='black')
        img_label.image = photo_img
        img_label.grid(row=row, column=column, sticky=sticky)
        def local_click(event):
            if command == None:
                pass
            else:
                command()
        img_label.bind("<Button-1>", local_click)
        return img_label
    
    def get_image(self, frame, path, width, height, row, column,sticky, command=None):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Label(frame, image=photo_img, bg='black')
        img_label.image = photo_img
        img_label.grid(row=row, column=column, sticky=sticky)
        def local_click(event):
            if command == None:
                pass
            else:
                command()
        img_label.bind("<Button-1>", local_click)
    
    def send_mqtt_data(self):

# import math
# a = 12345.6789876
# rounded_value = math.floor(a*1000)
# print(rounded_value)
        # ct = datetime.now()
# ts = ct.timestamp()
# # ct stores current time
# print("current time:-", ct)

# # ts store timestamp of current time
# ts = ct.timestamp()
# print("timestamp:-", ts)
        ct = datetime.now()
        ts = ct.timestamp()
        ts = math.floor(ts*1000)
        sensor_data = {
        'ts': ts,
        'values':{
                "S_0_0":int(self.TVOC),
                "S_0_1":int(self.CO2),
                "S_0_2":int(self.PM10),
                "S_0_3":int(self.PM25),
                "S_0_4":int(self.CH2O),
                "S_0_5":int(self.NH3),
                "S_0_6":int(self.Sm),
                "S_0_7":int(self.CO),
                "S_0_8":int(self.NO2),
                "S_0_9":int(self.LIGHT),
                "S_0_10":int(self.SOUND),
                "S_0_11":int(self.Rn),
                "S_0_12":int(self.temperature),
                "S_0_13":int(self.humidity),
                }
        }
        print(sensor_data)
        self.client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
        
    def get_all_data(self):
        check_value = str(self.controller.TVOC)
        if not check_value.startswith('PY'):                    # 원래 이렇게 처리하는게 아닌데.. 시간이 없어서 나중에 고칠 것...
                self.temperature = self.controller.temperature
                self.temp_label.config(text=self.temperature)
                self.humidity = self.controller.humidity
                self.humidity_label.config(text=self.humidity)
                # 밑에 마저 해야한다.
                self.TVOC = self.controller.TVOC
                self.TVOC_label.config(text=self.TVOC)
                
                self.CO2 = self.controller.CO2
                self.CO2_label.config(text=self.CO2)
                
                self.PM1 = self.controller.PM1
                self.PM1_label.config(text=self.PM1)
                
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
                
                self.change_text_color(self.controller.TVOC_level, self.TVOC_label)
                # if self.controller.TVOC_level == 1:
                #         self.TVOC_label.config(fg='blue')
                # elif self.controller.TVOC_level == 2:
                #         self.TVOC_label.config(fg='green')
                # elif self.controller.TVOC_level ==3:
                #         self.TVOC_label.config(fg='brown')
                # else:
                #         self.TVOC_label.config(fg='red')

                # def change_text_color():
                        
                # if self.controller.CO2_level == 1:
                #         self.CO2_label.config(fg='')
                # elif self.controller.CO2_level == 2:
                #         self.CO2_label.config(fg='')
                # elif self.controller.CO2_level == 3:
                #         self.CO2_label.config(fg='')
                # else:
                #         self.CO2_label.config(fg='')
                # if self.controller.PM1_level == 1:
                #         self.PM1_label.config(fg='')
                # elif self.controller.PM1_level == 2:
                #         self.PM1_label.config(fg='')
                # elif self.controller.PM1_level == 3:
                #         self.PM1_label.config(fg='')
                # else:
                #         self.PM1_label.config(fg='')
                # if self.controller.PM25_level == 1:
                #         self.PM25_label.config(fg='')
                # elif self.controller.PM25_level == 2:
                #         self.PM25_label.config(fg='')
                # elif self.controller.PM25_level == 3:
                #         self.PM25_label.config(fg='')
                # else:
                #         self.PM25_label.config(fg='')
                # if self.controller.PM10_level == 1:
                #         self.PM10_label.config(fg='')
                # elif self.controller.PM10_level == 2:
                #         self.PM10_label.config(fg='')
                # elif self.controller.PM10_level == 3:
                #         self.PM10_label.config(fg='')
                # else:
                #         self.PM10_label.config(fg='')
                # if self.controller.CH2O_level == 1:
                #         self.CH2O_label.config(fg='')
                # elif self.controller.CH2O_level == 2:
                #         self.CH2O_label.config(fg='')
                # elif self.controller.CH2O_level == 3:
                #         self.CH2O_label.config(fg='')
                # else:
                #         self.CH2O_label.config(fg='')
                # if self.controller.Sm_level == 1:
                # elif self.controller.Sm_level == 2:
                # elif self.controller.Sm_level == 3:
                # else:
                # if self.controller.NH3_level == 1:
                # elif self.controller.NH3_level == 2:
                # elif self.controller.NH3_level == 3:
                # else:
                # if self.controller.CO_level == 1:
                # elif self.controller.CO_level == 2:
                # elif self.controller.CO_level == 3:
                # else:
                # if self.controller.NO2_level == 1:
                # elif self.controller.NO2_level == 2:
                # elif self.controller.NO2_level == 3:
                # else:
                # if self.controller.H2S_level == 1:
                # elif self.controller.H2S_level == 2:
                # elif self.controller.H2S_level == 3:
                # else:
                # if self.controller.LIGHT_level == 1:
                # elif self.controller.LIGHT_level == 2:
                # elif self.controller.LIGHT_level == 3:
                # else:
                # if self.controller.SOUND_level == 1:
                # elif self.controller.SOUND_level == 2:
                # elif self.controller.SOUND_level == 3:
                # else:
                # if self.controller.Rn_level == 1:
                # elif self.controller.Rn_level == 2:
                # elif self.controller.Rn_level == 3:
                # else:
                # if self.controller.O3_level == 1:
                # elif self.controller.O3_level == 2:
                # elif self.controller.O3_level == 3:
                # else:
                
                # for k, v in SENSOR_DICT.items():
                #         if k == 'TVOC':
                #                 if int(self.TVOC) >= 0:
                #                     if int(self.TVOC) < v[2]:
                #                         self.TVOC_label.config(fg='red')
                #                         continue
                #                     elif int(self.TVOC) < v[3]:
                                        
                #                         continue
                #                     elif int(self.TVOC) < v[4]:
                                        
                #                         continue
                #                     else:
                                        
                #                         continue
                #                 else:
                                    
                #                     print('TVOC error')
                #                     continue
                        # elif k == 'CO2':
                        #         if self.CO2 >= 0:
                        #             if self.CO2 < v[2]:
                                        
                        #                 continue
                        #             elif self.CO2 < v[3]:
                                        
                        #                 continue
                        #             elif self.CO2 < v[4]:
                                        
                        #                 continue
                        #             else:
                                        
                        #                 continue
                        #         else:
                                    
                        #             print('CO2 error')
                        #             continue
                        # elif k == 'PM1':
                        #         if self.PM1 >= 0:
                        #             if self.PM1 < v[2]:
                                        
                        #                 continue
                        #             elif self.PM1 < v[3]:
                                        
                        #                 continue
                        #             elif self.PM1 < v[4]:
                                        
                        #                 continue
                        #             else:
                                        
                        #                 continue
                        #         else:
                                    
                        #             print('PM1 error')
                        #             continue
                        # elif k == 'PM25':
                        #         if self.PM25 >= 0:
                        #             if self.PM25 < v[2]:
                                        
                        #                 continue
                        #             elif self.PM25 < v[3]:
                                        
                        #                 continue
                        #             elif self.PM25 < v[4]:
                                        
                        #                 continue
                        #             else:
                                        
                        #                 continue
                        #         else:
                                    
                        #             print('PM25 error')
                        #             continue
                        # elif k == 'PM10':
                        #         if self.PM10 >= 0:
                        #             if self.PM10 < v[2]:
                                        
                        #                 continue
                        #             elif self.PM10 < v[3]:
                                        
                        #                 continue
                        #             elif self.PM10 < v[4]:
                                        
                        #                 continue
                        #             else:
                                        
                        #                 continue
                        #         else:
                                    
                        #             print('PM10 error')
                        #             continue
                        # elif k == 'CH2O':
                        #         if self.CH2O >= 0:
                        #             if self.CH2O < v[2]:
                                        
                        #                 continue
                        #             elif self.CH2O < v[3]:
                                        
                        #                 continue
                        #             elif self.CH2O < v[4]:
                                        
                        #                 continue
                        #             else:
                                        
                        #                 continue
                        #         else:
                                    
                        #             print('CH2O error')
                        #             continue
                        # elif k == 'SM':
                        #         if self.Sm >= 0:
                        #             if self.Sm < v[2]:
                                        
                        #                 continue
                        #             elif self.Sm < v[3]:
                                        
                        #                 continue
                        #             elif self.Sm < v[4]:
                                        
                        #                 continue
                        #             else:
                                        
                        #                 continue
                        #         else:
                                    
                        #             print('SM error')
                        #             continue
                        # elif k == 'NH3':
                        #         if self.NH3 >= 0:
                        #             if self.NH3 < v[2]:
                                        
                        #                 continue
                        #             elif self.NH3 < v[3]:
                                        
                        #                 continue
                        #             elif self.NH3 < v[4]:
                                        
                        #                 continue
                        #             else:
                                        
                        #                 continue
                        #         else:
                                    
                        #             print('NH3 error')
                        #             continue
                        # elif k == 'CO':
                        #         if self.CO >= 0:
                        #             if self.CO < v[2]:
                                        
                        #                 continue
                        #             elif self.CO < v[3]:
                                        
                        #                 continue
                        #             elif self.CO < v[4]:
                                        
                        #                 continue
                        #             else:
                                        
                        #                 continue
                        #         else:
                                    
                        #             print('CO error')
                        #             continue
                        # elif k == 'NO2':
                        #         if self.NO2 >= 0:
                        #             if self.NO2 < v[2]:
                                        
                        #                 continue
                        #             elif self.NO2 < v[3]:
                                        
                        #                 continue
                        #             elif self.NO2 < v[4]:
                                        
                        #                 continue
                        #             else:
                                        
                        #                 continue
                        #         else:
                                    
                        #             print('NO2 error')
                        #             continue
                        # elif k == 'H2S':
                        #         if self.H2S >= 0:
                        #             if self.H2S < v[2]:
                                        
                        #                 continue
                        #             elif self.H2S < v[3]:
                                        
                        #                 continue
                        #             elif self.H2S < v[4]:
                                        
                        #                 continue
                        #             else:
                                        
                        #                 continue
                        #         else:
                                    
                        #             print('H2S error')
                        #             continue
                        # elif k == 'LIGHT':
                        #         if self.LIGHT >= 0:
                        #             if self.LIGHT < v[2]:
                                        
                        #                 continue
                        #             elif self.LIGHT < v[3]:
                                        
                        #                 continue
                        #             elif self.LIGHT < v[4]:
                                        
                        #                 continue
                        #             else:
                                        
                        #                 continue
                        #         else:
                                    
                        #             print('LIGHT error')
                        #             continue
                        # elif k == 'SOUND':
                        #         if self.SOUND >= 0:
                        #             if self.SOUND < v[2]:
                                        
                        #                 continue
                        #             elif self.SOUND < v[3]:
                                        
                        #                 continue
                        #             elif self.SOUND < v[4]:
                                        
                        #                 continue
                        #             else:
                                        
                        #                 continue
                        #         else:
                                    
                        #             print('SOUND error')
                        #             continue
                        # elif k == 'RN':
                        #         if self.Rn >= 0:
                        #             if self.Rn < v[2]:
                                        
                        #                 continue
                        #             elif self.Rn < v[3]:
                                        
                        #                 continue
                        #             elif self.Rn < v[4]:
                                        
                        #                 continue
                        #             else:
                                        
                        #                 continue
                        #         else:
                                    
                        #             print('RN error')
                        #             continue
                        # elif k == 'O3':
                        #         if self.O3 >= 0:
                        #             if self.O3 < v[2]:
                                        
                        #                 continue
                        #             elif self.O3 < v[3]:
                                        
                        #                 continue
                        #             elif self.O3 < v[4]:
                                        
                        #                 continue
                        #             else:
                                        
                        #                 continue
                        #         else:
                                    
                        #             print('O3 error')
                        #             continue
                        # else:
                        #         print('uart k, v 에서 잘못되었다... 왜?')
        
        
        self.after(2000, self.get_all_data)

    def change_text_color(self,level, label):
        print('level : ', level)
        print('label : ', label)
        if level == 1:
                label.config(fg='blue')
        elif level == 2:
                label.config(fg='green')    
        elif level == 3:
                label.config(fg='brown')    
        elif level == 4:
                label.config(fg='red')
        else:
                pass
    
    
    def quit_program(self):
        sys.exit()