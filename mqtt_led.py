import time
from umqtt.simple import MQTTClient
from machine import Pin

led = Pin(2, Pin.OUT, value=1)


SERVER = "192.168.1.35"
TOPIC = b"led"

state = 0

def sub_cb(topic, msg):
    global state
    print((topic, msg))
    if msg == b"on":
        led.value(0)
        state = 1
    elif msg == b"off":
        led.value(1)
        state = 0
    elif msg == b"toggle":
        # LED is inversed, so setting it to current state
        # value will make it toggle
        led.value(state)
        state = 1 - state

def main(server="localhost"):
    c = MQTTClient("umqtt_client", server)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"foo_topic")
    while True:
        if True:
            # Blocking wait for message
            c.wait_msg()
        else:
            c.check_msg()
            time.sleep(1)

    c.disconnect()

if __name__ == "__main__":
    main()
