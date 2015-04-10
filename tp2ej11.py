# coding=utf-8
__author__ = 'guillermo'
"""11. Realice un script que guarde en una lista los primeros N números primos, donde N se
ingresa por teclado.

Los números primos son aquellos números enteros que sólo son divisibles por si mismos y por la unidad".
Ejemplos: 1,2,3,5,7,11,13,17,19..., -1,-2,-3,...
"""
tupla = (2, 3, 5, 7)
lnump = []
N = int(raw_input('Ingrese la cantidad de numeros primos: '))

for i in range(1, N+1):
    j = 0
    band = True
    while (i <= tupla[j]) and (band == True):
        if (i % tupla[j]) != 0:
            j += 1
            print 'ok'


        else:
            band = False
        print i, tupla[j], band

    if band == True:
        lnump.append(i)
print lnump

