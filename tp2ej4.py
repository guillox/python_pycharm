# coding=utf-8
__author__ = 'guillermo'
"""4. Construya una estructura de datos para almacenar información acerca de eventos,guardando para cada evento una
descripción, fecha y hora,lista de invitados y si es público o no. Agregue algunos eventos como ejemplo, imprima la
cantidad de invitados de alguno en particular, agréguele dos invitados y elimine uno de otro evento.
¿Cómo haría si quisiera agregarle un estado a los invitados que indique si el mismo confirmó asistencia, aún no la
confirmó o bien la rechazó? Modifique la estructura para ello

eventos = [{'descripcion': , 'fecha': ,'hora':,listainvt:[],'publico':},{'descripcion': , 'fecha': ,'hora':,listainvt:[],'publico':},]

"""

eventos = [{'descripcion':'casamiento', 'fecha' :'12/23/15', 'hora': 16, 'listainvt': ['carlos', 'pedro', 'roberto', 'maria', 'laura','raul'],
            'publico':False}, {'descripcion': 'quinse', 'fecha': '10/12/15', 'hora': 22, 'listainvt': ['juan', 'carla', 'lucrecia', 'catalina', 'guillermo'],
            'publico':False}]



# imprima la cantidad de invitados de alguno en particular
print 'la cantidad de invitados de un evento es: ', len(eventos[0]['listainvt'])

#agréguele dos invitados

for i in range(0, 2):
    inv = raw_input('ingrese un nuevo invitado: ')
    (eventos[0]['listainvt']).append(inv)

print eventos

#elimine uno de otro evento.

print (eventos[1]['listainvt']).pop(2)
print (eventos[1]['listainvt'])

#¿Cómo haría si quisiera agregarle un estado a los invitados que indique si el mismo confirmó asistencia, aún no la
# confirmó o bien la rechazó? Modifique la estructura para ello

lista = (eventos[0]['listainvt'])
del eventos[0]['listainvt']
print eventos[0]
for i in range(0, len(lista)):
    estado = raw_input('ingrese un estado: ')
    eventos[0][lista[i]] = estado

print eventos[0]