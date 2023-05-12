# # 장치아이디: d41e2660-f0a1-11ed-97fe-477ec4188e5d
# # 엑세스 토큰 : 51ZFhNEWFXLi4pW758Gy

# # Time에 대한 정보
# timestamp = str(time.time())



# # MQTT broker 정보
# broker_address = "210.117.143.37"
# broker_port = 10061

import paho.mqtt.client as mqtt
import time
import json

brokers_out ={"broker1": "210.117.143.37"}

data_out=json.dumps(brokers_out['broker1'])

data_in = data_out

brokers_in = json.loads(data_in)

cont = input('enter to continue')

def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8", 'ignore'))


topic = "test/json_test"
client=mqtt.Client("pythontest1")
client.loop_start()
client.subscribe(topic)
