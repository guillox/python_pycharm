# coding=utf-8
__author__ = 'guillermo'
"""6. Escriba un script que lea de teclado un número que represente la temperatura en grados Celsius e imprima en
pantalla “Frío” si es menor a 10 pero mayor a -10, “Templado” si es mayor a 10 y menor a 18, “Caluroso” si es mayor a 18
y menor a 30,“Muy Caluroso” si es mayor a 30 y menor a 40 y “Temperatura de otro planeta” en caso contrario

ejemplo
30 < temp <= 40   = temp>30 and temp<=40
"""

temp = int(raw_input('ingrese una temperatura en grado celsius: '))

if temp >= -10 and temp <= 10:
    print 'Frio'
elif temp > 10 and temp <= 18:
    print 'Templado'
elif temp > 18 and temp <= 30:
    print 'Caluroso'
elif 30 < temp <= 40:
    print 'Muy Caluroso'
else:
    print 'Temperatura de otro planeta'