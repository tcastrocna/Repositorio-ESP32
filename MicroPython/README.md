# Instalar Thonny IDE no Windows para ESP32

Este guia descreve o processo de instalação do Thonny IDE no Windows para trabalhar com ESP32.

## Passo 1: Instalar Python

1. Acesse o site oficial do Python: [⬇️Download Python](https://www.python.org/downloads/).
2. Baixe a versão mais recente do Python compatível com o Windows.
3. Durante a instalação, certifique-se de marcar a opção "Add Python to PATH".
4. Complete a instalação seguindo as instruções na tela.

## Passo 2: Instalar o Thonny IDE

1. Acesse o site oficial do Thonny IDE: [⬇️Download Thonny](https://thonny.org/).
2. Baixe a versão mais recente para Windows.
3. Siga as instruções de instalação do Thonny IDE.

## Passo 3: Configurar Thonny para ESP32

1. Abra o Thonny IDE após a instalação.
2. No menu superior, clique em **Tools** > **Options**.
3. Na aba **Interpreter**, selecione "MicroPython (ESP32)" na lista de interpreters.
4. Selecione a porta correspondente ao seu ESP32 em **Port** ou **WebREPL**.

## Passo 4: Instalar ou Atualizar o MicroPython no ESP32

1. Ainda na aba **Interpreter**, clique em **Install or update MicroPython (esptool)**.
2. Na janela que se abre:
   - **Target port:** Verifique se a porta correta está selecionada.
   - **MicroPython family:** Selecione **ESP32**.
   - **Variant:** Escolha **Espressif ESP32/WROOM**.
   - **Version:** Selecione a versão mais recente disponível.
3. Clique em **Install** para gravar o MicroPython no seu ESP32.

## Passo 5: Verificar a Instalação do MicroPython

1. Após a instalação, o Thonny deve se conectar automaticamente ao ESP32.
2. No terminal do Thonny, você deve ver o prompt `>>>`, indicando que o ESP32 está pronto para receber comandos Python.

## Passo 6: Gravar um Programa "Hello World" (Piscar o LED)

1. Abra um novo arquivo no Thonny.
2. Digite o seguinte código para piscar o LED integrado do ESP32:

````python
import time
from machine import Pin

led = Pin(02, Pin.OUT) #Define o led da placa, GPIO 2

#Inicia um loop
while True:
    led.on() #Liga o Led
    time.sleep(1) #Espera 1 segundo
    led.off() #Desliga o Led
    time.sleep(1) #Espera 1 segundo
 ````
3. Salve o arquivo com a extensão `.py`.
4. Carregue o código para o ESP32 clicando em **Run** ou pressionando `F5`.
5. Verifique se o LED integrado do ESP32 começa a piscar.

## ❌ Possíveis Erros

### O Windows Não Reconhece a Placa ESP32

Se o Windows não reconhecer a sua placa ESP32, é possível que seja um problema de driver para comunicação USB, e pode ser necessário instalar o driver correspondente.

#### Solução:

1. Baixe e instale os drivers CP210x (versão v6.7.6):
   - Acesse o site oficial da Silicon Labs: [⬇️ CP210x Windows Drivers v6.7.6](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers).
   - Escolha a versão correta para o seu sistema operacional (32-bit ou 64-bit).
   - Siga as instruções de instalação fornecidas.

2. Após a instalação, desconecte e reconecte a placa ESP32 ao computador.
3. Verifique se a porta é reconhecida no Thonny IDE em **Tools** > **Options** > **Interpreter** na seção **Port**.

Se o problema persistir, tente reiniciar o computador e verificar novamente as conexões da placa.

## Conclusão
Agora seu ESP32 está pronto para receber e executar código Python usando o Thonny IDE no Windows. Se tiver dúvidas ou problemas, consulte a [documentação oficial do Thonny](https://thonny.org/doc/).
