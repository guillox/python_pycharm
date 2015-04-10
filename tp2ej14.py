# coding=utf-8
__author__ = 'guillermo'
"""14. Dados los siguientes datos en un diccionario:
datos = {"captured_at": "2015-03-27T12:10:00Z", "temperature": 17, "humidity": 72, "dew": 12, "bar": 1021, "uv": 2,
"wind_chill": 17, "wind_speed": 1,"wind_direction": "SSW"}
Realice un script que informe cada dato, convirtiendo los campos al castellano al momento de accederlos
Nota: Tenga en cuenta que no se accede en orden a un diccionario.
captured_in :capturado en
temperature : temperatura
humidity : humedad
dew:rocío
bar:bar
uv:uv
wind chill:sensación térmica
wind speed:velocidad del viento
wind direction:dirección del viento
"""

datos = {"captured_at": "2015-03-27T12:10:00Z", "temperature": 17, "humidity": 72, "dew": 12, "bar": 1021, "uv": 2,
"wind_chill": 17, "wind_speed": 1, "wind_direction": "SSW"}

datosesp = {}
lista = datos.keys()
print lista

datosesp['velocidad del viento'] = datos[lista[0]]
datosesp['uv'] = datos[lista[1]]
datosesp['bar'] = datos[lista[2]]
datosesp['temperatura'] = datos[lista[3]]
datosesp['sensacion termicar'] = datos[lista[4]]
datosesp['direccion del viento'] = datos[lista[5]]
datosesp['rocio'] = datos[lista[6]]
datosesp['capturado en'] = datos[lista[7]]
datosesp['humedad'] = datos[lista[8]]

print datosesp




