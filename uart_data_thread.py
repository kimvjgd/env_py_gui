from threading import Thread, Lock
import serial
import pyautogui
from sensor_list import SENSOR_DICT

pyautogui.FAILSAFE = False

# 나중에 음수로 오면 error이니깐 -> 핸들링 작업 해야함


class UartDataThread(Thread):
    def __init__(self, controller):
        Thread.__init__(self)
        self.serialport = serial.Serial('/dev/ttyS5', 115200, timeout=0.1)
        self.two_pos = [[0,0],[0,0]]
        self.last_x = 0                             # 근데 흠...
        self.last_y = 0
        self.serial_str = ''
        self.x = 0
        self.y = 0
        self.TVOC = 1.0
        self.CO2 = 0
        self.PM1 = 0
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
        
        self.TVOC_level = 0                 # 0 - 제대로 된 센서 값을 받아오지 못하는 것이다.
        self.CO2_level = 0                  # 1 - 좋음
        self.PM1_level = 0
        self.PM25_level = 0                 # 2 - 보통
        self.PM10_level = 0                 # 3 - 나쁨
        self.CH2O_level = 0                 # 4 - 아주 나쁨
        self.Sm_level = 0
        self.NH3_level = 0
        self.CO_level = 0
        self.NO2_level = 0
        self.H2S_level = 0
        self.LIGHT_level = 0
        self.SOUND_level = 0
        self.Rn_level = 0
        self.O3_level = 0
    
    # def show_data(self):
    #     print(self.TVOC)
    #     print(self.CO2)
        
        
    def run(self):
        while 1:
            self.lock.acquire()
            self.serial_str = str(self.serialport.readline())[2:-5]
            
            if self.serial_str == '':                                                                   # 아무것도 오고 있지 않을 때            => 고쳐야 되겠다...
                # print('이제 이런 경우는 없다고 보면 되지 않나?')
                # self.two_pos = [[self.last_x, self.last_y], [-1, -1]]
                # if(self.two_pos[0] != [-1, -1]) and (self.two_pos[1] == [-1, -1]):
                #     pyautogui.click()
                # self.last_x = -1
                # self.last_y = -1
                # print('여기를 들른다.')
                pass
                
            else:
                # print('터치가 되든 안되든 이렇게')
                
                
                serial_list = self.serial_str.split(',')
                print(serial_list)
                # print(len(serial_list))
                if len(serial_list) == 19:
                    self.x, self.y = float(serial_list[0]), float(serial_list[1])

                    if self.x != 0 and self.y != 0:       # 터치가 되어질때 => 이떄는 x, y가 0, 0이 들어오고
                        self.x = int((self.x-180)/3740*799)
                        self.y = int((self.y-400)/3410*479)     # x, y를 맞는 좌표로 바꿔준다.
                        self.two_pos = [[self.last_x, self.last_y],[self.x, self.y]]
                        self.last_x = self.x
                        self.last_y = self.y
                        pyautogui.moveTo(self.x, self.y)

                        
                        

                    else:                           # 터치말고 데이터 수집 구간 => 이떄는 x, y가 0 이 들어온다.
                        # if self.x > 0 and self.y > 0:
                        #     pyautogui.moveTo(self.x, self.y)
                        # print('데이터 수집')
                        self.two_pos = [[self.last_x, self.last_y], [-1, -1]]
                        if(self.two_pos[0] != [-1, -1]) and (self.two_pos[1] == [-1, -1]):
                            pyautogui.click()
                        self.last_x = -1
                        self.last_y = -1
                        self.TVOC = float(serial_list[2])
                        self.CO2 = float(serial_list[3])
                        self.PM1 = float(serial_list[4])
                        self.PM25 = float(serial_list[5])
                        self.PM10 = float(serial_list[6])
                        self.CH2O = float(serial_list[7])
                        self.Sm = float(serial_list[8])
                        self.NH3 = float(serial_list[9])
                        self.CO = float(serial_list[10])
                        self.NO2 = float(serial_list[11])
                        self.H2S = float(serial_list[12])
                        self.LIGHT = float(serial_list[13])
                        self.SOUND = float(serial_list[14])
                        self.Rn = float(serial_list[15])
                        self.O3 = float(serial_list[16])
                        self.temperature = float(serial_list[17])
                        self.humidity = float(serial_list[18])
                        
                        
                        # if self.x ==0 and self.y ==0:       # 터치를 하고 있지 않을때
                        
                        self.controller.TVOC = serial_list[2]
                        self.controller.CO2 = serial_list[3]
                        self.controller.PM1 = serial_list[4]
                        self.controller.PM25 = serial_list[5]
                        self.controller.PM10 = serial_list[6]
                        self.controller.CH2O = serial_list[7]
                        self.controller.Sm = serial_list[8]
                        self.controller.NH3 = serial_list[9]
                        self.controller.CO = serial_list[10]
                        self.controller.NO2 = serial_list[11]
                        self.controller.H2S = serial_list[12]
                        self.controller.LIGHT = serial_list[13]
                        self.controller.SOUND = serial_list[14]
                        self.controller.Rn = serial_list[15]
                        self.controller.O3 = serial_list[16]
                        self.controller.temperature = serial_list[17]
                        self.controller.humidity = serial_list[18]
                        
                        
                        

                        # self.key_value_list = [[],[]]
                        # self.key_list = []
                        # self.value_list = []
                        for k, v in SENSOR_DICT.items():
                            if k == 'TVOC':
                                if self.TVOC >= 0:
                                    if self.TVOC < v[2]:
                                        self.controller.TVOC_level = 1
                                        continue
                                    elif self.TVOC < v[3]:
                                        self.controller.TVOC_level = 2
                                        continue
                                    elif self.TVOC < v[4]:
                                        self.controller.TVOC_level = 3
                                        continue
                                    else:
                                        self.controller.TVOC_level = 4
                                        continue
                                else:
                                    self.controller.TVOC_level = 0
                                    print('TVOC error')
                                    continue
                            elif k == 'CO2':
                                if self.CO2 >= 0:
                                    if self.CO2 < v[2]:
                                        self.controller.CO2_level = 1
                                        continue
                                    elif self.CO2 < v[3]:
                                        self.controller.CO2_level = 2
                                        continue
                                    elif self.CO2 < v[4]:
                                        self.controller.CO2_level = 3
                                        continue
                                    else:
                                        self.controller.CO2_level = 4
                                        continue
                                else:
                                    self.controller.CO2_level = 0
                                    print('CO2 error')
                                    continue
                            elif k == 'PM1':
                                if self.PM1 >= 0:
                                    if self.PM1 < v[2]:
                                        self.controller.PM1_level = 1
                                        continue
                                    elif self.PM1 < v[3]:
                                        self.controller.PM1_level = 2
                                        continue
                                    elif self.PM1 < v[4]:
                                        self.controller.PM1_level = 3
                                        continue
                                    else:
                                        self.controller.PM1_level = 4
                                        continue
                                else:
                                    self.controller.PM1_level = 0
                                    print('PM1 error')
                                    continue
                            elif k == 'PM25':
                                if self.PM25 >= 0:
                                    if self.PM25 < v[2]:
                                        self.controller.PM25_level = 1
                                        continue
                                    elif self.PM25 < v[3]:
                                        self.controller.PM25_level = 2
                                        continue
                                    elif self.PM25 < v[4]:
                                        self.controller.PM25_level = 3
                                        continue
                                    else:
                                        self.controller.PM25_level = 4
                                        continue
                                else:
                                    self.controller.PM25_level = 0
                                    print('PM25 error')
                                    continue
                            elif k == 'PM10':
                                if self.PM10 >= 0:
                                    if self.PM10 < v[2]:
                                        self.controller.PM10_level = 1
                                        continue
                                    elif self.PM10 < v[3]:
                                        self.controller.PM10_level = 2
                                        continue
                                    elif self.PM10 < v[4]:
                                        self.controller.PM10_level = 3
                                        continue
                                    else:
                                        self.controller.PM10_level = 4
                                        continue
                                else:
                                    self.controller.PM10_level = 0
                                    print('PM10 error')
                                    continue
                            elif k == 'CH2O':
                                if self.CH2O >= 0:
                                    if self.CH2O < v[2]:
                                        self.controller.CH2O_level = 1
                                        continue
                                    elif self.CH2O < v[3]:
                                        self.controller.CH2O_level = 2
                                        continue
                                    elif self.CH2O < v[4]:
                                        self.controller.CH2O_level = 3
                                        continue
                                    else:
                                        self.controller.CH2O_level = 4
                                        continue
                                else:
                                    self.controller.CH2O_level = 0
                                    print('CH2O error')
                                    continue
                            elif k == 'SM':
                                if self.Sm >= 0:
                                    if self.Sm < v[2]:
                                        self.controller.Sm_level = 1
                                        continue
                                    elif self.Sm < v[3]:
                                        self.controller.Sm_level = 2
                                        continue
                                    elif self.Sm < v[4]:
                                        self.controller.Sm_level = 3
                                        continue
                                    else:
                                        self.controller.Sm_level = 4
                                        continue
                                else:
                                    self.controller.Sm_level = 0
                                    print('SM error')
                                    continue
                            elif k == 'NH3':
                                if self.NH3 >= 0:
                                    if self.NH3 < v[2]:
                                        self.controller.NH3_level = 1
                                        continue
                                    elif self.NH3 < v[3]:
                                        self.controller.NH3_level = 2
                                        continue
                                    elif self.NH3 < v[4]:
                                        self.controller.NH3_level = 3
                                        continue
                                    else:
                                        self.controller.NH3_level = 4
                                        continue
                                else:
                                    self.controller.NH3_level = 0
                                    print('NH3 error')
                                    continue
                            elif k == 'CO':
                                if self.CO >= 0:
                                    if self.CO < v[2]:
                                        self.controller.CO_level = 1
                                        continue
                                    elif self.CO < v[3]:
                                        self.controller.CO_level = 2
                                        continue
                                    elif self.CO < v[4]:
                                        self.controller.CO_level = 3
                                        continue
                                    else:
                                        self.controller.CO_level = 4
                                        continue
                                else:
                                    self.controller.CO_level = 0
                                    print('CO error')
                                    continue
                            elif k == 'NO2':
                                if self.NO2 >= 0:
                                    if self.NO2 < v[2]:
                                        self.controller.NO2_level = 1
                                        continue
                                    elif self.NO2 < v[3]:
                                        self.controller.NO2_level = 2
                                        continue
                                    elif self.NO2 < v[4]:
                                        self.controller.NO2_level = 3
                                        continue
                                    else:
                                        self.controller.NO2_level = 4
                                        continue
                                else:
                                    self.controller.NO2_level = 0
                                    print('NO2 error')
                                    continue
                            elif k == 'H2S':
                                if self.H2S >= 0:
                                    if self.H2S < v[2]:
                                        self.controller.H2S_level = 1
                                        continue
                                    elif self.H2S < v[3]:
                                        self.controller.H2S_level = 2
                                        continue
                                    elif self.H2S < v[4]:
                                        self.controller.H2S_level = 3
                                        continue
                                    else:
                                        self.controller.H2S_level = 4
                                        continue
                                else:
                                    self.controller.H2S_level = 0
                                    print('H2S error')
                                    continue
                            elif k == 'LIGHT':
                                if self.LIGHT >= 0:
                                    if self.LIGHT < v[2]:
                                        self.controller.LIGHT_level = 1
                                        continue
                                    elif self.LIGHT < v[3]:
                                        self.controller.LIGHT_level = 2
                                        continue
                                    elif self.LIGHT < v[4]:
                                        self.controller.LIGHT_level = 3
                                        continue
                                    else:
                                        self.controller.LIGHT_level = 4
                                        continue
                                else:
                                    self.controller.LIGHT_level = 0
                                    print('LIGHT error')
                                    continue
                            elif k == 'SOUND':
                                if self.SOUND >= 0:
                                    if self.SOUND < v[2]:
                                        self.controller.SOUND_level = 1
                                        continue
                                    elif self.SOUND < v[3]:
                                        self.controller.SOUND_level = 2
                                        continue
                                    elif self.SOUND < v[4]:
                                        self.controller.SOUND_level = 3
                                        continue
                                    else:
                                        self.controller.SOUND_level = 4
                                        continue
                                else:
                                    self.controller.SOUND_level = 0
                                    print('SOUND error')
                                    continue
                            elif k == 'RN':
                                if self.Rn >= 0:
                                    if self.Rn < v[2]:
                                        self.controller.Rn_level = 1
                                        continue
                                    elif self.Rn < v[3]:
                                        self.controller.Rn_level = 2
                                        continue
                                    elif self.Rn < v[4]:
                                        self.controller.Rn_level = 3
                                        continue
                                    else:
                                        self.controller.Rn_level = 4
                                        continue
                                else:
                                    self.controller.Rn_level = 0
                                    print('RN error')
                                    continue
                            elif k == 'O3':
                                if self.O3 >= 0:
                                    if self.O3 < v[2]:
                                        self.controller.O3_level = 1
                                        continue
                                    elif self.O3 < v[3]:
                                        self.controller.O3_level = 2
                                        continue
                                    elif self.O3 < v[4]:
                                        self.controller.O3_level = 3
                                        continue
                                    else:
                                        self.controller.O3_level = 4
                                        continue
                                else:
                                    self.controller.O3_level = 0
                                    print('O3 error')
                                    continue
                            else:
                                print('uart k, v 에서 잘못되었다... 왜?')
                            
                            
                            
                        #     # print('key : ', k)
                        #     # print('value : ', v[2:5])
                        #     # self.key_list.append(k)
                        #     # self.value_list.append(v[2:5])
                        #     self.key_value_list[0].append(k)
                        #     self.key_value_list[1].append(v[2:5])
                        # print(self.key_value_list)
                        # for sensor_name in self.key_value_list[0]:
                        #     if sensor_name == 'TVOC':
                        #         print('TVOC')
                        #         continue
                        #     elif sensor_name == 'CO2':
                        #         print('CO2')
                        #         continue
                        #     elif
                            
                            
                        
                            
                            
                        
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
                else:
                    pass        
                        
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