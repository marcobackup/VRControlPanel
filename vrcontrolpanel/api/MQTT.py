import paho.mqtt.client as mqtt


class MQTTClient:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client = mqtt.Client()

    def connect(self):
        return self.client.connect(self.ip, self.port, 60)

    def subscribe(self, topic):
        return self.client.subscribe(topic)

    def start(self):
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()
