import tkinter as tk
from tkinter import ttk
from sensor_list import SENSOR_DICT
from tkinter import *
from PIL import Image, ImageTk

class Element(ttk.Frame):
    def __init__(self,parent, controller, show_home, sensor):
        super().__init__(parent)
        self.controller = controller
        self.sensor_name = sensor


        self.columnconfigure(0, weight=1)
        
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=6)
        
        status_part = tk.Frame(self, bg="black")
        status_part.grid(row=0, column=0, sticky="NEWS")
        
        
        status_part.rowconfigure(0, weight=1)

        status_part.columnconfigure(0, weight=1)
        status_part.columnconfigure(1, weight=10)
        status_part.columnconfigure(2, weight=1)
        
        back_button_part = tk.Frame(status_part, bg='black')
        back_button_part.grid(row=0, column=0, sticky="NEWS", pady=10,ipadx=0, ipady=0)
        back_button_part.place(relx=0.1, rely=0.5, anchor='c')          # 안맞으면...그냥 해야함... 나도 이유 모름... 그냥.... 그냥 함...  아니면 골 때려짐
        back_button_part.rowconfigure(0, weight=1)
        back_button_part.columnconfigure(0, weight=1)
        back_button_part.columnconfigure(1, weight=1)
        back_button_part.bind("<Button-1>", show_home)
        
        # self.get_button(back_button_part, show_home, "img/parts/back_button.png", 25, 25,0, 0, 'NE')
        self.get_image(back_button_part, "img/parts/back_button.png", 25, 25,0, 0, 'NE', command=show_home)
        back_label = Label(back_button_part, text='MAIN', font=('Arial', 20), fg='white', bg='black')
        back_label.grid(row=0, column=1, sticky='NW')
        
        # 나중에 정리....
        def back_click(event):
            show_home()
        
        back_label.bind("<Button-1>", back_click)
        
        ###############################################################################################################
        # main frame
        
        main_part = tk.Frame(self, bg='red')
        main_part.grid(row=1, column=0, sticky='NEWS')
        main_part.columnconfigure(0, weight=1)
        main_part.rowconfigure(0, weight=4)
        main_part.rowconfigure(1, weight=5)
        
        ######################## 1 2 1 1 1 ########################
        
        ### Sensor Description Part
        sensor_description_part = tk.Frame(main_part, bg='green')
        sensor_description_part.grid(row=0, column=0, sticky='NEWS')
        sensor_description_part.columnconfigure(0, weight=2)
        sensor_description_part.columnconfigure(1, weight=9)
        sensor_description_part.rowconfigure(0, weight=1)
        sensor_description_part.rowconfigure(1, weight=2)
        
        # left part(sensor photo는 rowspan=2로 해야할 것) rowspan 3이 되야하나...?
        # img = Label(sensor_description_part, bg='green')
        # img.grid(row=0, column=0, rowspan=2, sticky='NEWS')
        self.get_image(sensor_description_part, 'img/sensor/CH2O.png', 80, 80, 0, 0, 'NEWS', rowspan=2)
        
        # 1 - Sensor name
        title = Label(sensor_description_part, bg='red', text='TVOC!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        title.grid(row=0, column=1, sticky='NEWS')
        
        # 2 - Sensor description
        img = Label(sensor_description_part, bg='yellow', text='description!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        img.grid(row=1, column=1, sticky='NEWS')
        
        
        
        
        ### Sensor Gauge & Range Part
        sensor_value_part = tk.Frame(main_part, bg='black')
        sensor_value_part.grid(row=1, column=0, sticky='NEWS')
        sensor_value_part.columnconfigure(0,weight=1)
        sensor_value_part.rowconfigure(0,weight=3)
        sensor_value_part.rowconfigure(1,weight=4)
        sensor_value_part.rowconfigure(2,weight=3)
        # 1 - Sensor value
        value = Label(sensor_value_part, bg='orange', text='52g/m^3')
        value.grid(row=0, column=0, sticky='W')
        # 1 - Sensor gauge
        self.get_image(sensor_value_part, 'img/gauge/gage-12.png',700,50,row=1,column=0, sticky='NEWS')
        # gauge = Label(sensor_value_part, bg='magenta')
        # gauge.grid(row=1, column=0, sticky='NEWS')
        # 1 - Sensor range
        range = Label(sensor_value_part, bg='cyan')
        range.grid(row=2, column=0, sticky='NEWS')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def get_image(self, frame, path, width, height, row, column,sticky, command=None,rowspan=1):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Label(frame, image=photo_img, bg='black')
        img_label.image = photo_img
        img_label.grid(row=row, column=column, rowspan=rowspan, sticky=sticky)
        def local_click(event):
            command()
        img_label.bind("<Button-1>", local_click)

    def get_button(self, frame,command, path, width, height, row, column,sticky):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Button(frame, image=photo_img, bg='black', command=command,bd=0)        # bd = border
        img_label.image = photo_img
        img_label.grid(row=row, column=column, sticky=sticky)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         description_1_part = tk.Frame(self, bg="blue")
#         description_1_part.grid(row=1, column=0, sticky="NEWS")
#         description_1_part.columnconfigure(0, weight=1)
#         description_1_part.columnconfigure(1, weight=4)

        
        
#         description_2_part = tk.Frame(self, bg="white")
#         description_2_part.grid(row=2, column=0, sticky="NEWS")
#         description_2_part.columnconfigure(0, weight=1)
#         description_2_part.columnconfigure(1, weight=4)

        
#         current_value_part = tk.Frame(self, bg="green")
#         current_value_part.grid(row=3, column=0, sticky="NEWS")
        
#         color_gauge_part = tk.Frame(self, bg="yellow")
#         color_gauge_part.grid(row=4, column=0, sticky="NEWS")
        
#         num_value_part = tk.Frame(self, bg="grey")
#         num_value_part.grid(row=5, column=0, sticky="NEWS")


# ###########################################################################################        
#         # put product in frame  

#         # Status Part
#         left_part = tk.Frame(status_part)
#         left_part.grid(sticky="W")
#         left_part.columnconfigure(0, weight=1)
#         left_part.columnconfigure(1, weight=1)
        
#         left_part.rowconfigure(0, weight=1)
#         back_button = ttk.Button(left_part, text="Back", command=show_home, cursor="hand2",width=5)
#         back_button.grid(row=0, column=0)
        
#         to_main_label = tk.Label(left_part, text="MAIN")
#         to_main_label.grid(row=0, column=1)
        
#         #### Description Part
#         # description_left_part = tk.Frame(description_part)
#         # description_left_part.rowconfigure(0, weight=1)
#         # description_left_part.columnconfigure(0, weight=1)
#         # description_left_part.columnconfigure(1, weight=6)
#         # description_left_part.grid(row=0, column=0, sticky="NEWS")
        
#         #sample photo code
#         img = PhotoImage(file=SENSOR_DICT[sensor][1],height=100, width=100)
#         self.img_label = Label(description_1_part, image=img, bg='black')
#         self.img_label.image = img
#         # img_label.configure(image=PhotoImage(file=SENSOR_DICT[sensor][1]))
#         # img_label.image = PhotoImage(file=SENSOR_DICT[sensor][1])
#         self.img_label.grid(row=0, column=0, sticky="NEWS")
        
        
#         #### Current Value Part
        
#         #### Color Gauge Part
        
#         #### Num Value Part


    # def change_image(self,sensor_name):
    #     img = PhotoImage(file=SENSOR_DICT[sensor_name][1])
    #     self.img_label.configure(image=img)
    #     self.img_label.image = img
    #     print('######################################')
    #     print(sensor_name)
    #     print('######################################')
        