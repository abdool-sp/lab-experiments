from machine import Pin
from time import sleep


led_1 = Pin(5, Pin.OUT, value=1)
led_2 = Pin(4, Pin.OUT, value=0)




while True:
   print('1')
   led_1.value(1)
   led_2.value(0)
   sleep(1)
   print('2')
   led_1.value(0)
   led_2.value(1)
   sleep(1)

