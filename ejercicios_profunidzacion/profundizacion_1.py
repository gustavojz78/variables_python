# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
print("Bienvenido. Seleccione una opción : \n 1-SUMA \n 2-RESTA \n 3-MULTIPLICAR \n 4-DIVIDIR \n 5-POTENCIA")
numero=int(input("seleccione opción: "))
if  numero == 1 :
    num1 = float(input("ingrese primer numero: "))
    num2 = float(input("ingrese segundo numero: "))
    suma = num1 + num2
    print("el resultado de la suma es : ", suma)
if   numero == 2 :
    num1 = float(input("ingrese primer numero: "))
    num2 = float(input("ingrese segundo numero: "))
    resta = num1 - num2
    print("el resultado de la resta es : ", resta)  
if   numero == 3 :
    num1 = float(input("ingrese primer numero: "))
    num2 = float(input("ingrese segundo numero: "))
    multi = num1 * num2
    print("el resultado de la multiplicación es : ", multi)    
if   numero == 4 :
    num1 = float(input("ingrese primer numero: "))
    num2 = float(input("ingrese segundo numero diferente a cero: "))
    div = num1 / num2
    print("el resultado de la división es : ", div) 
if   numero == 5 :
    num1 = int(input("ingrese numero base :"))
    num2 = int(input("ingrese exponente :"))
    pot = num1 ** num2
    print("el resultado de ", num1, "elevado a la ", num2, "es :", pot)   