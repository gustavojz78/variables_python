# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(input("por favor ingrese su nombre : "))

print('Ingrese por consola su apellido/s:')
apellido = str(input("ahora su apellido : "))

# Imprima su nombre completo
print("su nombre es : ", nombre, apellido)
# Almacenar su nombre completo en una variable
# nombre_completo = .....
nombre_completo= nombre +apellido
# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)
cantidad_letrasNA= len(nombre+apellido)
cantidad_letrasN = len(nombre)
cantidad_letrasA = len(apellido)
print("su nombre completo tiene " , cantidad_letrasNA, "letras")
print("su nombre tiene " , cantidad_letrasN , "letras")
print("su apellido tiene " , cantidad_letrasA , "letras")