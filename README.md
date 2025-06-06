# Sistema de Reconhecimento de Gestos em Situações de Falta de Energia

## Descrição do problema

Em casos de falta de energia elétrica, a comunicação e a segurança ficam prejudicadas, especialmente em ambientes escuros. Pessoas podem ter dificuldade para pedir ajuda ou sinalizar que estão em perigo, e serviços essenciais precisam de formas simples e eficazes para detectar essas situações.

## Visão geral da solução

Criamos um sistema em Python, utilizando MediaPipe, que detecta em tempo real gestos simples como abrir/fechar as mãos e abrir a boca, usando apenas a câmera do computador. Quando esses gestos são identificados, o sistema emite um alerta sonoro e exibe uma mensagem no console. A solução funciona mesmo com pouca luz e pode ser usada em casas, empresas e hospitais para sinalizar emergências de forma acessível e rápida.

## Gestos que ativam o alerta

- Abrir a boca.
- Abrir e fechar a mão.

## Tecnologias:

- Python
- MediaPipe
- OpenCV
- Pygame

## Vídeo demonstrativo

https://youtu.be/d1l_rFYWZfQ

## Como Funciona

- Captura em tempo real da câmera usando OpenCV.
- Processamento das imagens com MediaPipe Hands e FaceMesh para identificar:
- A distância entre o polegar e o indicador → indica mão aberta ou fechada.
- A abertura da boca → sinaliza possível pedido de ajuda.
- Quando detectado, toca o som alerta.mp3 e imprime o alerta no console.

## Como usar

1. Pré Requisistos

- Python
- Webcam funcional

2. Instale as dependências:

- pip install mediapipe opencv-python pygame

3. Execute o programa

- py main.py
