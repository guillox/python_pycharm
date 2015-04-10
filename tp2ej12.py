# coding=utf-8
__author__ = 'guillermo Marti'
"""12. Escriba un programa que simule el movimiento de un objeto en un escenario dado, para lo cual recibirá datos por
teclado y se moverá con números. Se ingresarán los siguientes datos:
a. dos números que representan las dimensiones: ancho y alto.
b. la posición actual en que se ubicará el objeto (verificar que no se ubique fuera del escenario, dado por el ancho y
alto).
c. la opción para moverlo: 4 para mover izq, 6 para mover der, 2 para bajar, 8 para subir, 0 terminar.
Aclaración: En todo movimiento se debe verificar que no se caiga del escenario y
mostrar la posición actual luego de cada movimiento."""

# a. dos números que representan las dimensiones: ancho y alto.
ancho = int(raw_input('ingrese el ancho del escenario:'))
alto = int(raw_input('ingrese el alto del escenario:'))

# b. la posición actual en que se ubicará el objeto (verificar que no se ubique fuera del escenario, dado por el ancho y
#alto).


x = int(raw_input('ingrese la coordenada x de la posicion del objeto: '))
y = int(raw_input('ingrese la coordenada y de la posicion del objeto: '))

while x > ancho or y > alto:
    print 'ingrese de nuevo la posicion x e y ya que se ubica fuera del escenario'
    x = int(raw_input('ingrese la coordenada x de la posicion del objeto: '))
    y = int(raw_input('ingrese la coordenada y de la posicion del objeto: '))


# la opción para moverlo: 4 para mover izq, 6 para mover der, 2 para bajar, 8 para subir, 0 terminar.
opc = int(raw_input('ingrese una opcion para moverlo: '))
while opc != 0:
    if opc == 4:
        x -= 1
    elif opc == 6:
        x += 1
    elif opc == 8:
        y += 1
    elif opc == 2:
        y -= 1
    else:
        print ('no se ingreso una opcion correcta')
    if (x < 0) or (x > ancho) or (y > alto) or (y < 0):
        print 'ingrese de nuevo la posicion x e y ya que se ubica fuera del escenario'
        opc = 0
    print 'posicion actual:', x, y
    if opc != 0:
        opc = int(raw_input('ingrese una opcion para moverlo'))
print 'simulacion finalizada'




