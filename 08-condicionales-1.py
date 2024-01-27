#Revisar si una condicion es mayor a

balance = 500
if balance > 600:
    print('Si puedes pagar')
else:
    print('No tienes saldo')

#Likes
likes = 200
if likes ==200:
    print(f'Excelente, {likes} likes')

#if con texto
lenguaje = 'python'
if lenguaje == 'python':
    print('Excelente decision')

#if not (para negar)
if not lenguaje == 'Java':
    print('Que agradable sujeto')

#Evaluar un Boolean
autenticado = True
if autenticado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesion')

#Evaluar elemento de una lista
lenguajes = ['Python', 'Kotlin', 'JavaScript', 'PHP']

if 'Go' in lenguajes:
    print('Go existe')
else:
    print('No, no existe')

#If anidados
usuario_autenticado = True
usuario_admin = True
if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sesion')