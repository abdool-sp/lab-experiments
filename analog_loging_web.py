try:
    import urequests as requests
except ImportError:
    import requests
import json as j
from machine import ADC
import gc
adc = ADC(0)
value = {'value': adc.read()}


url = "https://nodered-47.herokuapp.com/post"



def post(value):
    global  url
    print(value)
    temp=url+'?value='+str(value['value'])
    r = requests.post(temp)
    del temp
    #print(r)
    #print(r.content)
    print(r.text)
    #print(r.content)
    #print(r.json())
    r.close()


while True:
    if value != adc.read():
        value = {'value': adc.read()}
        print('sendin the post request')
        post(value)
        gc.collect()
