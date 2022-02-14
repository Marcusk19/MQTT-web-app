from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from flask_mobility import Mobility
from flask_mobility.decorators import mobile_template
import paho.mqtt.publish as publish


load_dotenv()
MQTT_SERVER = os.getenv("MQTT_SERVER") # ip address of linode instance
print("Server: " + MQTT_SERVER)

app = Flask(__name__)

@app.route('/', methods = ["POST", "GET"])
@mobile_template('{mobile/}index.html')
def index(template):
    if request.method == "POST":
        destination = request.form.get("dest")
        source = request.form.get("source")
        publish.single("destination", destination, hostname=MQTT_SERVER)
        publish.single("source", source, hostname=MQTT_SERVER)
        print("Published message to " + MQTT_SERVER)    
    return render_template(template)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port="80")