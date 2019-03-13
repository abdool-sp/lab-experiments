from machine import Pin, PWM
from umqtt.simple import MQTTClient
pwm0 = PWM(Pin(2))      # create PWM object from a pin
#pwm0.freq()             # get current frequency
pwm0.freq(1000)         # set frequency
#pwm0.duty()             # get current duty cycle
pwm0.duty(10)          # set duty cycle
pwm0.deinit()           # turn off PWM on the pin

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


def set_pwm(value):
    pwm0.duty(int(value.decode()))          # set duty cycle


def sub_cb(topic, msg):
    global state
    print((topic, msg))
    print(msg.decode())
    set_pwm(msg)
    

def main(server="broker.hivemq.com"):
    c = MQTTClient("umqtt_client", server)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"pwm_topic")
    while True:
        if True:
            # Blocking wait for message
            c.wait_msg()
        else:
            c.check_msg()
            time.sleep(1)

    c.disconnect()

if __name__ == "__main__":
    do_connect()
    main()
