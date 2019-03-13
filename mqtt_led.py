import time
from umqtt.simple import MQTTClient
from machine import Pin

led = Pin(2, Pin.OUT, value=1)

SERVER = "broker.hivemq.com"
TOPIC = b"led"

state = 0

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Galaxy', 'abdool1751')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


def sub_cb(topic, msg):
    global state
    print((topic, msg))
    if msg == b"on":
        led.value(1)
        state = 1
    elif msg == b"off":
        led.value(0)
        state = 0
    elif msg == b"toggle":
        # LED is inversed, so setting it to current state
        # value will make it toggle
        led.value(state)
        state = 1 - state

def main():
    c = MQTTClient("umqtt_client", SERVER)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"led_topic")
    while True:
        if True:
            # Blocking wait for message
            c.wait_msg()
        else:
            c.check_msg()
            time.sleep(1)

    c.disconnect()

if __name__ == "__main__":
    try:
        do_connect()
        main()
    except:
        pass
        
