from machine import Pin

led = Pin(2, Pin.OUT)    # create output pin on GPIO0


while True:
   led.value(1)
   sleep(1)
   led.value(0)
   sleep(1)
