from umqtt.simple import MQTTClient

from machine import Pin


p2 = Pin(2, Pin.IN)     # create input pin on GPIO2
value = p2.value()      # get value, 0 or 1

server = ""

c = MQTTClient("umqtt_client", server)
c.connect()

def publish(value):
    value = str(value)
    c.publish(b"pin_topic", value.encode())



publish(value)
while True:
    if value = p2.value():
        value = p2.value()
        publish(value)
    

c.disconnect()


