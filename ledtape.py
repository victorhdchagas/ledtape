# ledtape/index.py

from machine import Pin
from classes import PixelRange
import neopixel

class Scene:
    def __init__(self, pixelRange:PixelRange, algorithm):
        self.pixelRange = pixelRange 
        self.algorithm = algorithm  

    async def execute(self, neopixel,parameters = None):
        if(parameters == None):
            await self.algorithm(self.pixelRange, neopixel)
            return
        await self.algorithm(self.pixelRange, neopixel, parameters)

class LedTape:
    def __init__(self, pixel_range:PixelRange,pin:int):
        self.pixelRange = pixel_range  
        self.neoRing = neopixel.NeoPixel(Pin(pin), pixel_range.end)

    async def blink(self, scene,parameters = None):
        print("Iniciando a cena de Blink...")
        if(parameters == None):
            await scene.execute(self.neoRing)
        else: 
            await scene.execute(self.neoRing,parameters)
