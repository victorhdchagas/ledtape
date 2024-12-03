from machine import ADC,reset
import uasyncio
import ujson

def getTemperature():
    adc = ADC(4)
    ADC_voltage = adc.read_u16() * (3.3 / (65536))
    return 27 - (ADC_voltage - 0.706)/0.001721

def save(dados):
    with open('dados.json', 'w') as f:
        ujson.dump(dados, f)

# Função para ler dados de um arquivo JSON
def read():
    with open('dados.json', 'r') as f:
        return ujson.load(f)

async def loop():
    while True:
        config=read()
        configTemp = config["temp"] if 'temp' in config and config["temp"] is not None and type(config["temp"]) is list else []
        if(len(configTemp)>7):
            configTemp.pop(0)
        configTemp.append(getTemperature())
        config["temp"] = configTemp
        save(config)
        await uasyncio.sleep((60*60)*6)