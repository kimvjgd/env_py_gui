from threading import Thread
import serial
# import pyautogui

# pyautogui.FAILSAFE = False

class UartDataThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.serialport = serial.Serial('/dev/ttyS5', 115200, timeout=0.1)
        self.two_pos = [[0,0],[0,0]]
        self.last_x = 0
        self.last_y = 0
        self.serial_str = ''
        
        
        
    def run(self):
        while 1:
            self.serial_str = str(self.serialport.readline())[2:-5]
            serial_list = self.serial_str.split(',')
            print(serial_list)
            

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





