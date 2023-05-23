from threading import Thread, Lock
import serial
import pyautogui


pyautogui.FAILSAFE = False

# 나중에 음수로 오면 error이니깐 -> 핸들링 작업 해야함


class UartDataThread(Thread):
    def __init__(self, controller):
        Thread.__init__(self)
        self.serialport = serial.Serial('/dev/ttyS5', 115200, timeout=0.1)
        self.two_pos = [[0,0],[0,0]]
        self.last_x = 0
        self.last_y = 0
        self.serial_str = ''
        self.x = 0
        self.y = 0
        self.TVOC = 1.0
        self.CO2 = 0
        self.PM25 = 0
        self.PM10 = 0
        self.CH2O = 0
        self.Sm = 0
        self.NH3 = 0
        self.CO = 0
        self.NO2 = 0
        self.H2S = 0
        self.LIGHT = 0
        self.SOUND = 0
        self.Rn = 0
        self.O3 = 0
        self.temperature = 0
        self.humidity = 0
        self.controller = controller
        self.lock = Lock()
        
    
    # def show_data(self):
    #     print(self.TVOC)
    #     print(self.CO2)
        
        
    def run(self):
        while 1:
            self.lock.acquire()
            self.serial_str = str(self.serialport.readline())[2:-5]
            
            if self.serial_str == '':
                self.two_pos = [[self.last_x, self.last_y], [-1, -1]]
                if(self.two_pos[0] != [-1, -1]) and (self.two_pos[1] == [-1, -1]):
                    pyautogui.click()
                self.last_x = -1
                self.last_y = -1
                
            else:
                
                serial_list = self.serial_str.split(',')
                print(serial_list)
                # print(len(serial_list))
                if len(serial_list) == 18:
                    self.x, self.y = float(serial_list[0]), float(serial_list[1])
                    self.x = int((self.x-180)/3740*799)
                    self.y = int((self.y-400)/3410*479)
                    self.TVOC = float(serial_list[2])
                    self.CO2 = float(serial_list[3])
                    self.PM25 = float(serial_list[4])
                    self.PM10 = float(serial_list[5])
                    self.CH2O = float(serial_list[6])
                    self.Sm = float(serial_list[7])
                    self.NH3 = float(serial_list[8])
                    self.CO = float(serial_list[9])
                    self.NO2 = float(serial_list[10])
                    self.H2S = float(serial_list[11])
                    self.LIGHT = float(serial_list[12])
                    self.SOUND = float(serial_list[13])
                    self.Rn = float(serial_list[14])
                    self.O3 = float(serial_list[15])
                    self.temperature = float(serial_list[16])
                    self.humidity = float(serial_list[17])
                    
                    self.controller.TVOC = serial_list[2]
                    self.controller.CO2 = serial_list[3]
                    self.controller.PM25 = serial_list[4]
                    self.controller.PM10 = serial_list[5]
                    self.controller.CH2O = serial_list[6]
                    self.controller.Sm = serial_list[7]
                    self.controller.NH3 = serial_list[8]
                    self.controller.CO = serial_list[9]
                    self.controller.NO2 = serial_list[10]
                    self.controller.H2S = serial_list[11]
                    self.controller.LIGHT = serial_list[12]
                    self.controller.SOUND = serial_list[13]
                    self.controller.Rn = serial_list[14]
                    self.controller.O3 = serial_list[15]
                    self.controller.temperature = serial_list[16]
                    self.controller.humidity = serial_list[17]
                    
                    
                    # SENSOR_DICT = {
                    #     'TVOC':['img/sensor/Main-TVOC.png','img/sensor/TVOC.png', 200, 600, 2000],  # ~200 : 좋음(1) || ~600 : 보통(2) || ~2000 : 나쁨(3) || 2000~ : 아주나쁨(4)
                    #     'CO':['img/sensor/Main-CO.png','img/sensor/CO.png', 2, 9, 15],
                    #     'CO2':['img/sensor/Main-CO2.png','img/sensor/CO2.png', 450, 1000, 2000],
                    #     'NO2':['img/sensor/Main-NO2.png','img/sensor/NO2.png', 0.03, 0.05, 0.2],
                    #     'PM25':['img/sensor/Main-PM2.5.png','img/sensor/PM2.5.png', 15, 35, 75],
                    #     'H2S':['img/sensor/Main-H2S.png','img/sensor/H2S.png', 0.005, 0.02, 0.3],
                    #     'PM10':['img/sensor/Main-PM10.png','img/sensor/PM10.png', 30, 80, 150],
                    #     'LIGHT':['img/sensor/Main-LIGHT.png','img/sensor/LIGHT.png', 3, 5, 10],
                    #     'CH2O':['img/sensor/Main-CH2O.png','img/sensor/CH2O.png', 0.001, 0.01, 0.08],
                    #     'SOUND':['img/sensor/Main-SOUND.png','img/sensor/SOUND.png', 35, 40, 60],
                    #     'SM':['img/sensor/Main-Sm.png','img/sensor/Sm.png', 0, 1, 2],  # temp
                    #     'RN':['img/sensor/Main-Rn.png','img/sensor/Rn.png', 50, 100, 150],  # unit 설정 필수 일단 pCi/l
                    #     'NH3':['img/sensor/Main-NH3.png','img/sensor/NH3.png', 0.15, 1, 5],
                    #     'O3':['img/sensor/Main-O3.png','img/sensor/O3.png', 0.03, 0.09, 0.15],
                    # }
                    # level 을 여기서 측정하면 CPU 과부하가 너무 심해진다.
                    # self.controller.TVOC_level = 0
                    # self.controller.CO2_level = 0
                    # self.controller.PM25_level = 0
                    # self.controller.PM10_level = 0
                    # self.controller.CH2O_level = 0
                    # self.controller.Sm_level = 0
                    # self.controller.NH3_level = 0
                    # self.controller.CO_level = 0
                    # self.controller.NO2_level = 0
                    # self.controller.H2S_level = 0
                    # self.controller.LIGHT_level = 0
                    # self.controller.SOUND_level = 0
                    # self.controller.Rn_level = 0
                    # self.controller.O3_level = 0
                    
                    

                    
                    self.two_pos = [[self.last_x, self.last_y],[self.x, self.y]]
                    self.last_x = self.x
                    self.last_y = self.y
                    
                    
                    if self.x > 0 and self.y > 0:
                        pyautogui.moveTo(self.x, self.y)
            self.lock.release()    

###################################### self.serial_str ######################################
# 0 - touch x
# 1 - touch y
# 2 - TVOC
# 3 - CO2
# 4 - PM2.5
# 5 - PM10
# 6 - CH2O
# 7 - Sm
# 8 - NH3
# 9 - CO
# 10 - NO2
# 11 - H2S
# 12 - Light
# 13 - Sound
# 14 - Rn
# 15 - O3
# 16 - Temperature
# 17 - Humidity