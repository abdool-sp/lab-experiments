try:
    import urequests as requests
except ImportError:
    import requests

from machine import ADC

adc = ADC(0)
value = {'value': adc.read()}


url = "https://nodered-47.herokuapp.com/post"



def post(value):
    r = requests.post(url,value)
    print(r)
    print(r.content)
    print(r.text)
    print(r.content)
    print(r.json())
    r.close()

while True:
    if value != adc.read():
        post(value)
