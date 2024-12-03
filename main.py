# main.py

from ledtape import LedTape, Scene
from algorithms import fade, pomodoro
from classes import PixelRange, Color, PodororoArgs
import uasyncio
import config

# Cria uma instância de LedTape com uma tupla de pinos

led_tape = LedTape(PixelRange(0,30),15)  
lampScene = Scene(PixelRange(0, 4), fade)
# blinkScene = Scene(PixelRange(4, 26), blink_algorithm)
lampSceneEnd = Scene(PixelRange(26, 30), fade)
pomodoroScene = Scene(PixelRange(4, 26), pomodoro)
try:
    lampColor = Color(255,165,0,0.9)
    lampColor.set_brightness(0.9)
    lamp2Color = Color(255,165,0,0.9)
    lamp2Color.set_brightness(0.9)
    workColor = Color(0,255,0,0.9)
    workColor.set_brightness(0.5)
    breakColor = Color(255,0,0,0.9)
    breakColor.set_brightness(0.5)
    uasyncio.create_task(led_tape.blink(lampScene,lampColor))
    uasyncio.create_task(led_tape.blink(lampSceneEnd,lamp2Color))
    # uasyncio.create_task(led_tape.blink(blinkRandomlyScene))
    args = PodororoArgs(10,30,workColor,breakColor)
    uasyncio.create_task(led_tape.blink(pomodoroScene,args))
    uasyncio.run(config.loop())
    # uasyncio.run(led_tape.blink(pomodoroScene,args))
    # uasyncio.run(led_tape.blink(lampScene,lampColor))

except Exception as e:
    print("Quitting")
    print(e)
# led_tape.blink(fadeScene,(122,122,11))
# led_tape.blink(blinkScene)


