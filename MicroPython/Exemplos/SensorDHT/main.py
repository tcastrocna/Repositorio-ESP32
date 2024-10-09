import machine
import time
import dht

# Defina o pino ao qual o DHT11 está conectado (exemplo: GPIO 14)
dht_pin = machine.Pin(27)

# Inicialize o sensor DHT11
sensor = dht.DHT11(dht_pin) # Substitua por dht.DHT22(dht_pin) se for usar o DHT22

while True:
    try:
        # Faça a leitura do sensor
        sensor.measure()
        temperatura = sensor.temperature()  # Obtém a temperatura
        umidade = sensor.humidity()  # Obtém a umidade

        # Exibe os dados no console
        print("Temperatura: {}°C".format(temperatura))
        print("Umidade: {}%".format(umidade))
        
    except OSError as e:
        print("Erro ao ler o sensor: ", e)
    
    # Aguarda 2 segundos antes da próxima leitura
    time.sleep(2)
