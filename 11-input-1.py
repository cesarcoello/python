nombre = input('¿Cuál es tu nombre? \r\n')
print(f'Hola {nombre}')

#Leer datos que seran numeros
edad = input('¿Cuál es tu edad? \r\n')
#convertir edad (string) a int
edad = int(edad)
if edad >= 18:
    print('Ya puedes votar')
else:
    print('Aun no puedes votar')

#Mezclarlo con operadores
numero = input('Agrega un numero y te dire si es par o impar \r\n')
numero = int(numero)

if numero % 2 == 0:
    print(f'{numero} es par')
else:
    print(f'{numero} es impar')