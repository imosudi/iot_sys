
import sys, time

import paho.mqtt.client as mqtt

from random import randrange, uniform



#print(client)


"""try:
    client.connect(mqttBroker, 1883, 60)
except :
    print("Connection to Mosquitto failed!")
    sys.exit(1)"""


"""def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttBroker      = "localhost"
mqttc.connect("mqttBroker", 1883, 60)

mqttc.loop_forever()"""

def on_message1(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_message2(client, userdata, msg):
    print("Received msg ", str(msg.payload.decode("utf-8")))
    
class mosquittoBuild(object):
    def __init__(self, *args):
        self.mqttBroker      = "localhost" #"mqtt.eclipseprojects.io" #"localhost"
        self.client          = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        super(mosquittoBuild, self).__init__(*args)
    
    def establish_conn(self):
        mqttBroker      = self.mqttBroker
        client          = self.client
        try:
            client.connect(mqttBroker, 1883, 60)
        except :
            print("Connection to Mosquitto failed!")
            sys.exit(1)
        
        return client
    
    def on_message(self, client, userdata, message):
        print("Received message: ", str(message.payload.decode("utf-8")))
        print("miomiomiomio")
        the_msg = str(message.payload.decode("utf-8"))
        print("the_msg: ", the_msg)
        return the_msg
    
    def subscribe_conn(self, topic):
        mqttBroker      = self.mqttBroker
        client          = self.client
        client.connect(mqttBroker)
        
        client.loop_start()
        client.subscribe(topic)
        client.on_message = self.on_message
        print("client :", client.on_message)

        time.sleep(3)
        client.loop_stop
        
        """#try:
        if 1==1:    
            client.connect(mqttBroker)#, 1883, 10)
            client.on_connect   = client.subscribe(topic)
            client.on_message   = on_message1
            client.connect(mqttBroker, 1883, 60)
            #client.loop_start()
            #client.subscribe(topic)
            #client.on_message   = self.on_message #print(f"Received massage: {str(client.message_callback)}")
            print("TOPIC: ", topic)
            #client.loop_forever()
        #except :
        else:
            print("Connection to Mosquitto failed!")
            sys.exit(1)"""
        
        return  self.on_message
    