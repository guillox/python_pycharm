# coding=utf-8
__author__ = 'guillermo'
"""10. Sea un diccionario con datos de personas y sus edades, guarde en 3 listas diferentes los nombres de las personas
menores a 18 años, aquellos cuya edad esté entre 18 y 45 años y las personas mayores a 45 años. Imprima los 3 grupos de
personas ordenados por nombre.

diccionario ={apellido:[dni,nombre,localidad,edad,telefono]

"""

diccionario = {'Marti': ['33836167', 'jose', 'Punta alta', 26, 12345],
               'Agnelli': ['35678345', 'Nicolas', 'La Plata', 24, 1234534],
               'Suarez': ['40836167', 'alberto', 'Bahia Blanca', 15, 12343235],
               'Gonzalez': ['20836167', 'raul', 'torkins', 50, 12343215]}
lm18 = []
le18y45 = []
lM45 = []
clave = diccionario.keys()
for i in clave:
    if diccionario[i][3] <= 18:
        lm18.append(diccionario[i][1])
    elif 18 < diccionario[i][3] <= 45:
        le18y45.append(diccionario[i][1])
    else:
        lM45.append(diccionario[i][1])
print lm18
print le18y45
print lM45


