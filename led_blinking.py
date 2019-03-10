from machine import Pin

p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0


while True:
   p0.value(1)
   sleep(1)
   p0.value(0)
