from threading import Thread, Lock
import serial
import pyautogui


pyautogui.FAILSAFE = False

global TVOC
TVOC = 1.2

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
        
    
    def show_data(self):
        print(self.TVOC)
        print(self.CO2)
        
        
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
                
                self.x, self.y = float(serial_list[0]), float(serial_list[1])
                self.x = int((self.x-180)/3740*799)
                self.y = int((self.y-400)/3410*479)
                self.TVOC = float(serial_list[2])
                TVOC = float(serial_list[2])
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
                self.controller.temperature = serial_list[16]

                self.humidity = float(serial_list[17])
                
                self.two_pos = [[self.last_x, self.last_y],[self.x, self.y]]
                self.last_x = self.x
                self.last_y = self.y
                pyautogui.moveTo(self.x, self.y)
                print('TVOC ----- in uart_data_thread'+str(TVOC))
            self.lock.release()    

    @property
    def TVOC_VALUE(self):
        return self.TVOC
                

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




