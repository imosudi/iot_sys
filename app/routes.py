import time
from flask import render_template, request
from random import uniform

from app import app
from app.mosquitto_logic import mosquittoBuild #, mqtt, client

def on_message(self, client, userdata, message):
        print("Received message: ", str(message.payload.decode("utf-8")))
        return str(message.payload.decode("utf-8"))
    
@app.route('/',methods=['GET','POST'])
def home():
    
    return render_template('index.html')

@app.route('/publish')
def publish():
    clientBuild     = mosquittoBuild()
    client          = clientBuild.establish_conn()
    while True:
        temperature = uniform(20.0, 21.0)
        topic           = "TEMPERATURE"
        client.publish(topic, temperature)
        time.sleep(5)
        return f"TEMPERATURE: {temperature} °C", {"Refresh": "10; url=/publish"}


@app.route('/subscribe')
def subscribe():
    clientBuild     = mosquittoBuild()
    topic           = "TEMPERATURE"
    client          = clientBuild.subscribe_conn(topic)
    
    print("OUPUT", client)
    #client.loop_forever()
    return (f"Received the following message: {on_message}")
    """while True:
        temperature = uniform(20.0, 21.0)
        client.subscribe("paho/temperature", temperature)
        time.sleep(5)
        return f"paho/temperature: {temperature}", {"Refresh": "30; url=/publish"}"""
