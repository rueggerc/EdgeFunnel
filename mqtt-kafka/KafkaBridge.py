
import paho.mqtt.client as mqtt
 
MQTT_SERVER = "captain"
MQTT_PATH = "/home/sensors/#"

def publish_kafka_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        brokers = "kube:9092"
        _producer = KafkaProducer(bootstrap_servers=brokers, api_version=(0, 10))
        print("Got Producer")
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer
 
def on_mqtt_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_PATH)
 
def on_mqtt_message(client, userdata, message):
    print("message received=", str(message.payload.decode("utf-8")))
    payload = str(message.payload.decode("utf-8"))
    print("The message is {}".format(payload))
    
    # 'sensor3,64.04,99.90,1556182811311'
    items = payload.split(",")    
    key = items[0]

    print(f"host={host} temp={temperature} humidity={humidity}")
    publish_kafka_message(kafka_producer, kafka_topic, key, payload)
    
    
def main():
    print("BEGIN")
    
    kafka_topic = sys.argv[1]
    kafka_producer = connect_kafka_producer()

    client = mqtt.Client()
    client.on_connect = on_mqtt_connect  
    client.on_message = on_mqtt_message
 
    client.connect(MQTT_SERVER, 1883, 60)
    client.loop_forever()

if __name__ == '__main__':
    main()









