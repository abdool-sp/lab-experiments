from umqtt.simple import MQTTClient
import time
from machine import Pin

led = Pin(5, Pin.OUT)  
p2 = Pin(0, Pin.IN)     # create input pin on GPIO2
value = p2.value()      # get value, 0 or 1

server = "broker.hivemq.com"

c = MQTTClient("umqtt_client", server)
c.connect()

def publish(value):
    value = str(value)
    print("Button pressed")
    c.publish(b"pin_topic", value.encode())



publish(value)
while True:
    if not p2.value():
        value = p2.value()
        led.on()
        publish(value)
    time.sleep_ms(200)
    led.off()

c.disconnect()


