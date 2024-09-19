# Iniciando a Programação com ESP32.

Conjuntos de códigos simples para iniciar a programação com ESP32.

# Instalação do Arduino IDE e Configuração do ESP32

## Passo 1: Instalar o Arduino IDE

1. **Baixe o Arduino IDE**:
   - Acesse o [site oficial do Arduino](https://www.arduino.cc/en/software).
   - Escolha a versão adequada para o seu sistema operacional (Windows, macOS, Linux) e faça o download.

2. **Instale o Arduino IDE**:
   - **Windows**: Execute o arquivo `.exe` baixado e siga as instruções na tela.
   - **macOS**: Abra o arquivo `.dmg` e arraste o Arduino IDE para a pasta Aplicativos.
   - **Linux**: Descompacte o arquivo baixado e execute o script `install.sh` no terminal.

## Passo 2: Adicionar a Placa ESP32

1. **Abra o Arduino IDE**.

2. **Acesse as Preferências**:
   - No menu, clique em **Arquivo** > **Preferências** (ou use o atalho `Ctrl + ,`).

3. **Adicionar a URL da Placa ESP32**:
   - Na janela de preferências, localize o campo "URLs adicionais para gerenciadores de placas" (ou similar).
   - Adicione a seguinte URL:
     ```
     https://dl.espressif.com/dl/package_esp32_index.json
     ```
   - Se já houver URLs lá, separe-as com uma vírgula.

4. **Abrir o Gerenciador de Placas**:
   - Vá para o menu **Ferramentas** > **Placa** > **Gerenciador de Placas**.

5. **Instalar a Placa ESP32**:
   - No campo de pesquisa, digite "ESP32".
   - Quando a lista aparecer, encontre a opção "esp32 by Espressif Systems" e clique em **Instalar**.

6. **Selecionar a Placa ESP32**:
   - Após a instalação, vá para **Ferramentas** > **Placa** e escolha a placa ESP32 que você está usando (por exemplo, "ESP32 Dev Kit V1").


