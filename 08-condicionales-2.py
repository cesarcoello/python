#Ejemplo con elif
ocupacion = 'Jubilado'

if ocupacion == 'Estudiante':
    print('Tienes 50% de descuento')
elif ocupacion == 'Jubilado':
    print('Tienes 75% de descuento')
else:
    print('Debes pagar el 100%')