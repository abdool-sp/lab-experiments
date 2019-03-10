from machine import Pin, PWM

pwm0 = PWM(Pin(0))      # create PWM object from a pin
pwm0.freq()             # get current frequency
pwm0.freq(1000)         # set frequency
pwm0.duty()             # get current duty cycle
pwm0.duty(50)          # set duty cycle
pwm0.deinit()           # turn off PWM on the pin

def set_pwm(value):
    pwm0.duty(value)          # set duty cycle

def sub_cb(topic, msg):
    global state
    print((topic, msg))
    set_pwm(msg)
    

def main(server="localhost"):
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
    main()
