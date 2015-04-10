# coding=utf-8
__author__ = 'guillermo'
"""9. Dado un número ingresado por teclado, guardar en una lista los múltiplos de 2 que hay hasta ese número y guardar
en otra lista los múltiplos de 3."""

lmult2 = []
lmult3 = []

num = int(raw_input('ingrese un numero: '))
for i in range(1, num + 1):
    if i % 2 == 0:
        lmult2.append(i)
    if i % 3 == 0:
        lmult3.append(i)

print 'los los multiplos de 2 que hay hasta', num, 'es: ', lmult2
print 'los los multiplos de 3 que hay hasta', num, 'es: ', lmult3