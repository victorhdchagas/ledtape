# LedTape

Compatível com:
1- Fita Led WS2812
2- Raspberry Pi Pico 2

A classe Ledtape é responsável por criar a referencia da fita led, logo, ela precisa receber uma tupla com todos os pixels da fita.

Cada scene recebe uma tupla de pixel de inicio e de fim.

Scenes tambem dependem de um algoritmo pra tratar os pixels associados a mesma.

Ledtape tem um método blink que recebe uma instancia de Scene
