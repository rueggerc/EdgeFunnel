
import paho.mqtt.client as mqtt
 
MQTT_SERVER = "captain"
MQTT_PATH = "/home/sensors/#"
 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_PATH)
 
def on_message(client, userdata, message):
    print("message received=", str(message.payload.decode("utf-8")))
    payload = str(message.payload.decode("utf-8"))
    print("The message is {}".format(payload))
 
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)
client.loop_forever()


if __name__ == '__main__':
    pass