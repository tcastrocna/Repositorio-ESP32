import machine
import time
from machine import Pin

led = Pin(02, Pin.OUT) #Define o led da placa, GPIO 2

#Inicia um loop
while True:
    led.on() #Liga o Led
    time.sleep(1) #Espera 1 segundo
    led.off() #Desliga o Led
    time.sleep(1) #Espera 1 segundo