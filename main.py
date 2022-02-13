from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import paho.mqtt.publish as publish

load_dotenv()
MQTT_SERVER = os.getenv("MQTT_SERVER") # ip address of linode instance
print("Server: " + MQTT_SERVER)
MQTT_PATH = "test_channel" 

app = Flask(__name__)

@app.route('/', methods = ["POST", "GET"])
def index():
    if request.method == "POST":
        destination = request.form.get("dest")
        publish.single(MQTT_PATH, destination, hostname=MQTT_SERVER)
        print("Published message to " + MQTT_SERVER)    
    return render_template("index.html")

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0")