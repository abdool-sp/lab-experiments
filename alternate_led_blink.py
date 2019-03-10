from machine import Pin
from time import sleep


led_1 = Pin(0, Pin.OUT)
led_2 = Pin(2, Pin.OUT)


while True:
   led_1.value(1)
   led_2.value(0)
   sleep(1)
   led_1.value(0)
   led_2.value(1)
