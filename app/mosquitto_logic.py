
import sys, time

import paho.mqtt.client as mqtt

from random import randrange, uniform

mqttBroker      = "localhost"
client          = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

#print(client)


try:
    client.connect(mqttBroker, 1883, 60)
except :
    print("Connection to Mosquitto failed!")
    sys.exit(1)
    
    
class mosquittoBuild(object):
    def __init__(self, *args):
        super(mosquittoBuild, self).__init__(*args)
    
    def establish_conn(self):
        try:
            client.connect(mqttBroker, 1883, 60)
        except :
            print("Connection to Mosquitto failed!")
            sys.exit(1)
        
        return client
    