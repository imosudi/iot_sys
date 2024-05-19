import time
from flask import render_template, request
from random import uniform

from app import app
from app.mosquitto_logic import mosquittoBuild, mqtt, client


@app.route('/',methods=['GET','POST'])
def home():
    
    return render_template('index.html')

@app.route('/publish')
def publish():
    clientBuild     = mosquittoBuild()
    client          = clientBuild.establish_conn()
    while True:
        temperature = uniform(20.0, 21.0)
        client.publish("paho/temperature", temperature)
        time.sleep(5)
        return f"paho/temperature: {temperature}", {"Refresh": "30; url=/publish"}


