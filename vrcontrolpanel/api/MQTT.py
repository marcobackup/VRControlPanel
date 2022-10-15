import paho.mqtt.client as mqtt


class MQTTClient:

    def __init__(self, on_message):
        self.client = mqtt.Client()
        self.client.on_message = on_message

    def connect(self, ip, port):
        self.client.connect(ip, port, 60)

    def disconnect(self):
        self.client.disconnect()

    def subscribe(self, topic):
        return self.client.subscribe(topic)

    def publish(self, topic, payload):
        return self.client.publish(topic, payload)

    def start(self):
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()
