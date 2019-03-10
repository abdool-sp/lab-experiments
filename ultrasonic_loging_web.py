try:
    import urequests as requests
except ImportError:
    import requests

from machine import ADC
from hcsr04 import HCSR04

sensor = HCSR04(trigger_pin=16, echo_pin=0)

distance = sensor.distance_cm()

print('Distance:', distance, 'cm')

url = "https://nodered-47.herokuapp.com/post"

def get_distance():
    distance = sensor.distance_cm()
    return distance

def post(value):
    data = {}
    data['value'] = value
    r = requests.post(url,data)
    print(r)
    print(r.content)
    print(r.text)
    print(r.content)
    print(r.json())
    r.close()

while True:
    if distance != get_distance():
        distance = get_distance()
        post(distance())
