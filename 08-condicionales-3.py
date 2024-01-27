#Operadores AND y OR

usuario_logueado = True
usuario_admin = True

if usuario_logueado and usuario_admin:
    print('Administrador')
elif usuario_admin:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesion')