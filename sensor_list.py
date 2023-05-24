# from enum import Enum

# class SensorList(Enum):
#     TVOC = 1
#     CO = 2
#     CO2 = 3
#     NO2 = 4
#     PM25 = 5
#     H2S = 6
#     PM10 = 7
#     LIGHT = 8
#     CH2O = 9
#     SOUND = 10
#     SM = 11
#     RN = 12
#     NH3 = 13
#     O3 = 14

# sensorname : ['main에서 쓰이는 img.png', 'element_page에서 쓰이는 img.png']
SENSOR_DICT = {
    'TVOC':['img/sensor/Main-TVOC.png','img/sensor/TVOC.png', 200, 600, 2000,400],  # ~200 : 좋음(1) || ~600 : 보통(2) || ~2000 : 나쁨(3) || 2000~ : 아주나쁨(4)        마지막은 권고치
    'CO':['img/sensor/Main-CO.png','img/sensor/CO.png', 2, 9, 15,10],
    'CO2':['img/sensor/Main-CO2.png','img/sensor/CO2.png', 450, 1000, 2000,1000],
    'NO2':['img/sensor/Main-NO2.png','img/sensor/NO2.png', 0.03, 0.05, 0.2,0.05],
    'PM25':['img/sensor/Main-PM2.5.png','img/sensor/PM2.5.png', 15, 35, 75,35],
    'H2S':['img/sensor/Main-H2S.png','img/sensor/H2S.png', 0.005, 0.02, 0.3,0.005],
    'PM10':['img/sensor/Main-PM10.png','img/sensor/PM10.png', 30, 80, 150,75],
    'LIGHT':['img/sensor/Main-LIGHT.png','img/sensor/LIGHT.png', 3, 5, 10,10],
    'CH2O':['img/sensor/Main-CH2O.png','img/sensor/CH2O.png', 0.001, 0.01, 0.08,0.1],
    'SOUND':['img/sensor/Main-SOUND.png','img/sensor/SOUND.png', 35, 40, 60,60],
    'SM':['img/sensor/Main-Sm.png','img/sensor/Sm.png', 0, 1, 2,1],  # temp
    'RN':['img/sensor/Main-Rn.png','img/sensor/Rn.png', 74, 200, 300,200],  # unit 설정 필수 일단 pCi/l
    'NH3':['img/sensor/Main-NH3.png','img/sensor/NH3.png', 0.15, 1, 5,1],
    'O3':['img/sensor/Main-O3.png','img/sensor/O3.png', 0.03, 0.09, 0.15,0.02],
}

