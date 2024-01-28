#Iniciar un diccionario vacio
jugador = {}

#Se une un jugador
jugador['nombre'] = 'Cesar'
jugador['puntaje'] = 0
print(jugador)

#Incrementando el puntaje
jugador['puntaje'] = 100
print(jugador)

jugador['puntaje'] = 200
print(jugador)

#Acceder a un valor que no existe
print(jugador.get('consola', 'no existe ese elemento'))

#Iterar en el diccionario
for llave, valor in jugador.items():
    print(llave)
    print(valor)

#Eliminar nombre y puntaje
del jugador['nombre']
del jugador['puntaje']
print(jugador)