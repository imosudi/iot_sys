from app import app

#mqttc.loop_stop()

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=9000, host="0.0.0.0",  debug=True)



#client.loop_start()

