lenguajes = ['Python', 'Kotlin', 'JavaScript', 'PHP']

print( lenguajes) 
print( lenguajes[0]) #Python

#Ordenar list alfabeticamente
lenguajes.sort()
print(lenguajes)

#Acceder a un elemnto dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#Modificando valores de un list
lenguajes[2] = 'Goland'
print(lenguajes)

#Agregar elementos a un list
lenguajes.append('Ruby')
print(lenguajes)

#Eliminar de un list
del lenguajes[1]
print(lenguajes)

#Eliminar de un list
lenguajes.pop() #Eliminar el ultimo elemento
print(lenguajes)

#Eliminar con pop en una posicion en especifico
lenguajes.pop(0)
print(lenguajes)

#Eliminar por nombre
lenguajes.remove('Goland')
print(lenguajes)