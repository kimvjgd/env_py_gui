import paho.mqtt.client as mqtt
import json
import time

# 장치아이디: d41e2660-f0a1-11ed-97fe-477ec4188e5d
# 엑세스 토큰 : 51ZFhNEWFXLi4pW758Gy

# Time에 대한 정보
timestamp = str(time.time())



# MQTT broker 정보
broker_address = "210.117.143.37"
broker_port = 10061

# MQTT 클라이언트 생성
client = mqtt.Client()

# MQTT broker 연결
client.connect(broker_address, broker_port)

client.username_pw_set(username='d41e2660-f0a1-11ed-97fe-477ec4188e5d', password='51ZFhNEWFXLi4pW758Gy')

# headers
headers = {
    'Authorization': '51ZFhNEWFXLi4pW758Gy'
}

# 전송할 데이터
data = {"ts": timestamp,
 "values":{
     "S_0_0":0,
     "S_0_1":1,
     "S_0_2":2,
     "S_0_3":3,
     "S_0_4":4,
     "S_0_5":5,
     "S_0_6":6,
     "S_0_7":7,
     "S_0_8":8,
     "S_0_9":9,
     "S_0_10":10,
     "S_0_11":11,
     "S_0_12":12,
     "S_0_13":13,
 }
}
payload = json.dumps(data)

# MQTT topic 설정
topic = "sensors/data"



# MQTT 메시지 전송
client.publish(topic, payload)

# MQTT 연결 종료
client.disconnect()

# import requests

# response = requests.post(headers=headers, data=data)