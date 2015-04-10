# coding=utf-8
__author__ = 'guillermo'
"""2. Dados los siguientes conjuntos:
conj1 = set('python')
conj2 = set('pascal')
Imprimir todas las letras que contienen ambos, aquellas que tienen en común, las que
no, las que tiene el primero que no tenga el segundo y dada una letra ingresada por
teclado, verificar si se encuentra en alguno de ambos."""

conj1 = set('python')
conj2 = set('pascal')

# Imprimir todas las letras que contienen ambos
print conj1
print conj2

# aquellas que tienen en común(interseccion)
print conj1 & conj2

#las que no
print conj1 ^ conj2

#las que tiene el primero que no tenga el segundo
print conj1 - conj2

#dada una letra ingresada por teclado, verificar si se encuentra en alguno de ambos.
letra = raw_input('ingrese un caracter:')
print letra in conj1
print letra in conj2



