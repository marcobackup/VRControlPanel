import paho.mqtt.client as mqtt


class MQTTClient:

    def __init__(self, on_message):
        self.client = mqtt.Client()
        self.client.on_message = on_message

    def connect(self, ip, port):
        """
        connect
        connection to the broker
        """
        self.client.connect(ip, port, 60)

    def disconnect(self):
        """
        disconnect
        disconnection from the broker
        """
        self.client.disconnect()

    def subscribe(self, topic):
        """
        subscribe
        subscribe to topics
        """
        return self.client.subscribe(topic)

    def publish(self, topic, payload):
        """
        publish
        publish payload on topics
        """
        return self.client.publish(topic, payload)

    def start(self):
        """
        start
        start loop
        """
        self.client.loop_start()

    def stop(self):
        """
        stop
        stop loop
        """
        self.client.loop_stop()
