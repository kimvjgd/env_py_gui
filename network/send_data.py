import paho.mqtt.client as mqtt
import os
import json
import time
from datetime import datetime
import random

THINGSBOARD_HOST = "210.117.143.37"
# THINGSBOARD_HOST = "demo.thingsboard.io"
ACCESS_TOKEN='51ZFhNEWFXLi4pW758Gy'
port = 10061
sensor_data = {'my-temperature': 0}

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, port, 60)
client.loop_start()

try:
    while True:
        senval = random.randrange(0, 180)
        print(senval)
        sensor_data['my-temperature'] = senval

        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
        time.sleep(5)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()


# timestamp = str(time.time())
# def on_publish(client, userdata, result):
#     print("data published to thingsboard")

# # client1 = paho.Client("d41e2660-f0a1-11ed-97fe-477ec4188e5d")
# client1 = paho.Client("sangsang")
# client1.on_publish = on_publish
# client1.username_pw_set(ACCESS_TOKEN)
# client1.connect(broker, port, keepalive=60)
# # data = {
# #     # "ACCESS_TOKEN" : '51ZFhNEWFXLi4pW758Gy',
# #     # "device_no": 'device 10000',
# #     "ts": timestamp,
# #     "values":{
# #      "S_0_0":0,
# #      "S_0_1":1,
# #      "S_0_2":2,
# #      "S_0_3":3,
# #      "S_0_4":4,
# #      "S_0_5":5,
# #      "S_0_6":6,
# #      "S_0_7":7,
# #      "S_0_8":8,
# #      "S_0_9":9,
# #      "S_0_10":10,
# #      "S_0_11":11,
# #      "S_0_12":12,
# #      "S_0_13":13,
# #  }
# # }
# while True:
#     payload ="111"
    
#     ret = client1.publish("v1/devices/me/telemetry", payload)
#     print("PLease check LATEST TELEMETRY field of your device")
#     print(payload)
#     time.sleep(5)
