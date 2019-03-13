# import the libraries
from time import sleep_ms
from machine import UART
from machine import Pin
from umqtt.simple import MQTTClient


button = Pin(0, Pin.IN)



def exitUart(): # To set the baudrate to 115200 which is the normal baudrate
    serial= UART(0, 115200)

def main(client):
    serial= UART(0, 9600) #initialize serial communication
    print("\nConnecting....")
    serial.write('Connected to mobile phone')
    client.connect()
    print("\nReady!! ....")
    
    try:
        
        while button.value(): #if the button is not pressed 
            if serial.any(): # check if there is any data from the bluetooth module
                print("reading..")
                data = serial.read().decode() # read & decode the data from the module
                print(data)
                client.publish(b"bluetooth/lab",data.encode())
                print("published...")
                
             
    except  Exception as e:
        exitUart()
        print('Error '+ str(e)) #print 

if __name__ == '__main__':
    client =MQTTClient("lab","broker.hivemq.com")
    main(client)
    exitUart()
