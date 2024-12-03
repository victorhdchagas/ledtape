import random
import uasyncio
from classes import Color, PixelRange, PodororoArgs


# BRIGHTNESS = 0.2  # Adjust the brightness (0.0 - 1.0)

# Exemplo de algoritmo para a cena
async def blink_algorithm(pixelRange:PixelRange, neoRing ):
    color = Color(255, 0, 255)
    color.set_brightness(0.9)
    isAdding = False
    while True:
        for x in range(1,5):
            if(isAdding):
                 color.raise_brightness()
            else:
                color.lower_brightness()
            for i in range(pixelRange.start,pixelRange.end ):
                    neoRing[i] = color.get_color()
            neoRing.write()
            # print(f"{i}{x}{isAdding},{color.brightness}")
            await uasyncio.sleep(0.05)
        isAdding = not isAdding


async def blink_randomly(pixelRange:PixelRange, neoRing):
    while True:
        neoRing[random.randint(pixelRange.start,pixelRange.end)] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        neoRing.write()
        await uasyncio.sleep(random.uniform(0.04, 0.9))

async def fade(pixel_range:PixelRange, neoRing, color: Color):
    while True:
        while color.brightness < 1.0:
            color = color.raise_brightness(0.01)
            for i in range(pixel_range.start,pixel_range.end ):
                neoRing[i] = color.get_color()
            neoRing.write()
                
            await uasyncio.sleep(random.uniform(0.1, 0.4))

        while color.brightness > 0.5:
            color = color.lower_brightness(0.01)
            for i in range(pixel_range.start,pixel_range.end):
                neoRing[i] = color.get_color()
            neoRing.write()
            await uasyncio.sleep(random.uniform(0.1, 0.4))

async def pomodoro(pixel_range: PixelRange, neoRing, args: PodororoArgs):
    work_duration = args.work_duration
    break_duration = args.break_duration
    work_color = args.work_color
    break_color = args.break_color
    total_lamps = pixel_range.end - pixel_range.start  # Total de lâmpadas

    try:
        while True:
            # Período de trabalho
            for currentSec in range(work_duration):
                # Calcule quantas lâmpadas acender com base no tempo decorrido
                lamps_to_light = pixel_range.start + int((currentSec / work_duration) * total_lamps) + 1
                print(r"{:.2f}% - Lâmpadas acesas: {}".format((currentSec / work_duration) * 100, lamps_to_light))

                # Acenda as lâmpadas
                for i in range(pixel_range.start, pixel_range.end):
                    if i < lamps_to_light:
                        neoRing[i] = work_color.get_color()  # Lâmpadas acesas
                    else:
                        neoRing[i] = break_color.get_color()  # Lâmpadas apagadas

                neoRing.write()
                await uasyncio.sleep(1)  # Atualiza a cada segundo

            break_color.lower_brightness(break_color.brightness - 0.1)
            for currentSec in range(break_duration):
                # brightness_factor = (break_duration - currentSec) / break_duration  
                brightness_factor = (currentSec/break_duration)
                print(r"{:.2f}% - Lâmpadas apagadas: {}".format((currentSec / break_duration) * 100, brightness_factor))
                break_color.brightness = brightness_factor
                for i in range(pixel_range.start, pixel_range.end):
                    neoRing[i] = break_color.get_color()  

                neoRing.write()
                await uasyncio.sleep(1)  # Atualiza a cada segundo

    except Exception as e:
        print(e)
        pass
