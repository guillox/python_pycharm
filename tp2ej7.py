# coding=utf-8
__author__ = 'guillermo'
"""7. Realice un script que imprima la suma de los primeros 10 números impares.



"""
#Con while
cant = 0
suma = 0
num = 1
while cant < 10:
    if num % 2 != 0:
        cant += 1
        suma += num
        print num
    num += 1
print 'la suma de los primero numero impares es:',suma






