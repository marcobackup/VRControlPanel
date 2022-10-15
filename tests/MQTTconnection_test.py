import paho.mqtt.client as mqtt #import the client1
broker_address="broker.hivemq.com" 
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
print("connecting to broker")
client.connect(broker_address) #connect to broker
print("Subscribing to topic","VR/rover/control/velamount")
client.subscribe("VR/rover/control/velamount")
print("Publishing message to topic","VR/rover/control/velamount")
client.publish("VR/rover/control/velamount",'2')