""" Realizar un examen con 3 preguntas que tu desees, el usuario deberá responder 'SI' o 'NO' y al final otorgarle una calificación (La calificación se logra con una variable que inicia en 0 y por cada respuesta correcta incrementa en 1) """

calificacion = 0

pregunta1 = input('¿Comayagua en la Capital de Honduras? \r\n')
if pregunta1.upper() == 'NO':
    calificacion += 1

pregunta2 = input('¿Tres colores tiene la bandera de Honduras? \r\n')

if pregunta2.upper() == 'NO':
    calificacion += 1

pregunta3 = input('¿Honduras cuenta con billete de 200? \r\n')

if pregunta3.upper() == 'SI':
    calificacion += 1

print(f'Tu calificación es {calificacion}')