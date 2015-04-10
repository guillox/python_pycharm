# coding=utf-8
__author__ = 'guillermo'
"""
Parte I: Realice los siguientes ejercicios SIN utilizar estructuras de control.

1. Dada la siguiente tupla
tupla = (1, False, ['x', 'y', 'z'], 'casa')
a. ¿Es posible modificar el valor de False por True? ¿Y si queremos modificar 'x' por 'a'?
Justifique.No es posible modificar un valor de la tupla pq es inmutable, y si podemos modificar la x por la a ya que es una lista y es modificable
b. ¿Cómo haría para definir una tupla de un solo elemento?
c. ¿Para qué le parece que son especialmente útiles las tuplas?"""

tupla = (1, False, ['x', 'y', 'z'], 'casa')
#. ¿Es posible modificar el valor de False por True? ¿Y si queremos modificar 'x' por 'a'?Justifique.
#tupla[1] = True
tupla[2][0] = 'a'
print tupla

#b. ¿Cómo haría para definir una tupla de un solo elemento?
tupla2 =(23)
print tupla2
#c. ¿Para qué le parece que son especialmente útiles las tuplas?"""
"""Las tuplas son más rápidas que las listas. Si está usted definiendo un conjunto constante de valores y todo lo que va a hacer con él es recorrerla, utilice una tupla en lugar de una lista.
¿Recuerda que dije que las claves de un diccionario pueden ser enteros, cadenas y “algunos otros tipos”? Las tuplas son uno de estos tipos. Las tuplas pueden utilizarse como claves en un diccionario, pero las listas no.[2]
Las tuplas se utilizan para formatear cadenas, como veremos en seguida."""