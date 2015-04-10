# coding=utf-8
__author__ = 'guillermo'

"""3. Dado el siguiente diccionario con la información de notas de alumnos:
notas = {'Maria': 9, 'Juan': 6, 'Jose': 10, 'Valeria': 7}
a. Imprimir los nombres de todos los alumnos ordenados alfabéticamente.
b. Imprimir sólo las notas y verifique si alguien obtuvo un 4.
c. Agregar la nota de Gabriela, quien sacó un 9, y modifique la nota de Juan por un 7.
Luego ingrese por teclado el nombre de un alumno e imprima si su nota está en el diccionario.
d. Modificar el inciso anterior para que imprima la nota del alumno ingresado o -1 en
caso de no existir en el diccionario sin utilizar condicionales.
e. Borrar la nota de Valeria y luego imprima la cantidad de notas del diccionario
f. ¿Qué sucede si hacemos notas['jose'] = 4?
g. Eliminar todas las notas del diccionario."""

notas = {'Maria': 9, 'Juan': 6, 'Jose': 10, 'Valeria': 7}

#a. Imprimir los nombres de todos los alumnos ordenados alfabéticamente.
clave = notas.keys()
clave.sort()
print clave

#b. Imprimir sólo las notas y verifique si alguien obtuvo un 4.
valor = notas.values()
print valor

print 'Hay notas con 4:', notas.has_key(4)

#c. Agregar la nota de Gabriela, quien sacó un 9, y modifique la nota de Juan por un 7.
notas['Gabriela'] = 9
notas['Juan'] = 7
print notas

#Luego ingrese por teclado el nombre de un alumno e imprima si su nota está en el diccionario.
nombre = raw_input('Ingrese nombre de alumno:')
print notas.get(nombre, "El alumno no fue encontrado")

#d. Modificar el inciso anterior para que imprima la nota del alumno ingresado o -1 en caso de no existir en el diccionario sin utilizar
#  condicionales.
nombre = raw_input('Ingrese nombre de alumno:')
print notas.get(nombre, -1)

#e. Borrar la nota de Valeria y luego imprima la cantidad de notas del diccionario
notas['Valeria'] = None

#f. ¿Qué sucede si hacemos notas['jose'] = 4? Se modifica el valor de la clave jose
notas['jose'] = 4
print notas

#g. Eliminar todas las notas del diccionario.
notas.clear()
print notas