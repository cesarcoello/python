# Creando un diccionario simple

cancion = {
    'artista' : 'blink-182',
    'cancion' : 'I Miss You',
    'lanzamiento' : 2004,
    'likes' : 300000
}

print(cancion)

#Acceder a los elementos del diccionario
print(cancion['artista'])

#Mezclar con un string
artista = cancion['artista']
nombre_cancion = cancion['cancion']

print(f'Estoy escuchando {nombre_cancion} de {artista}')

#Agregar nuevos valores
cancion['playlist'] = 'Punk Rock'
print(cancion)

#Reemplazar valores existentes
cancion['cancion'] = 'Anthem Part Two'
print(cancion)

#Eliminar un elemento
del cancion['likes']
print(cancion)