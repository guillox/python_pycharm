# coding=utf-8
__author__ = 'guillermo'
"""8. Dados dos números naturales ingresados por teclado, imprimir el máximo común divisor
de ambos


tupla.__len__() devuelve la cantidad de elementos de la tupla
"""

tupla = (2, 3, 5, 7)
num = int(raw_input('Ingrese el primer número natural: '))


for cant in range(0, 2):
    result = 1
    while num > 1:
        i = 0
        while i <= 3:
            if (num % tupla[i]) == 0:
                num = num / tupla[i]
                result *= tupla[i]
            i += 1
        if result == 1:
            result = num
    print 'el maximo comun divisor del num es:', result
    num = int(raw_input('ingrese el segundo numero natural: '))


