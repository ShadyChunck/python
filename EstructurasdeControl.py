#3. Estructuras de Control

#Ejercicio 1 - El termostato inteligente
# Situación: Estás programando el software de un termostato de aire acondicionado.
# El sistema lee la temperatura actual de la habitación.
# Si la temperatura es estrictamente mayor a 25 grados, el programa debe imprimir
# "Encendiendo aire acondicionado". Si es 25 grados o menos, debe imprimir
# "Temperatura adecuada, modo ahorro".
# Tu tarea: Escribe el código utilizando una estructura if-else para simular esta toma de
# decisión. Asume una variable inicial de temperatura, por ejemplo temperatura = 28.
print("Ejercicio 1")
temperatura = 28
if temperatura > 25:
    print("Encendiendo aire acondicionado.")
else:
    print("Temperatura adecuada, modo ahorro.")

#Ejercicio 2 - Clasificación de descuentos
# Situación: Una tienda en línea tiene un sistema de descuentos por volumen de compra.
# Si el total de la compra es mayor o igual a $1000, se aplica un 20% de descuento.
# Si el total es menor a $1000 pero mayor o igual a $500, se aplica un 10% de descuento.
# Si la compra es menor a $500, no hay descuento (0%).
# Tu tarea: Escribe la estructura condicional que evalúe una variable total_compra
# (por ejemplo, con valor 750) e imprima de cuánto es el descuento aplicado
# (ej. "Tienes un 10% de descuento").
print("Ejercicio 2")
total_compra = 750
descuento = 0
if total_compra >= 1000:
    descuento = total_compra * 0.20
    print("Descuento aplicado:", descuento)
elif total_compra >= 500:
    descuento = total_compra * 0.10
    print("Descuento aplicado:", descuento)
elif total_compra < 500:
    print("No se aplica descuento. Por ende, se queda en", total_compra, "como el total de la compra.")

#Ejercicio 3 - Taquilla de cine con múltiples condiciones
# Situación: En un cine, para que te den el "Descuento Joven", debes cumplir con dos
# requisitos obligatorios al mismo tiempo: tener menos de 25 años Y presentar tu credencial
# de estudiante.
# Tu tarea: Crea dos variables iniciales: edad = 22 y tiene_credencial = True.
# Utiliza una estructura condicional y el operador lógico and para imprimir
# "Descuento aplicado" si cumple ambas condiciones, o "Precio regular" si le falta alguna
# (o ambas).
print("Ejercicio 3")
edad = 22
tiene_credencial = True
if edad < 25 and tiene_credencial:
    print("Descuento aplicado")
else:
    print("Precio Regular")

#Ejercicio 4 - Sistema de Login Básico
# Situación: Estás creando la pantalla de inicio de sesión de un sistema.
# Tienes una base de datos simulada donde el usuario correcto es "admin" y la contraseña es
# "secreta123".
# El programa primero debe verificar si el usuario ingresado es correcto.
#   Si el usuario es correcto, evalúa la contraseña: si coincide, imprime "Acceso concedido"; si no, imprime "Contraseña incorrecta".
#   Si el usuario ingresado no es "admin", debe imprimir directamente "Usuario no encontrado".
#   Tu tarea: Utiliza estructuras condicionales anidadas (un if dentro de otro if o dentro del else) para resolver este flujo.
print("Ejercicio 4")
usuario = "admin"
contrasena = "secreta123"
if usuario == "admin":
    if contrasena == "secreta123":
        print("Usuario Concedido")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no encontrado")

#Ejercicio 5 - ¿Par o impar?
# Situación: En muchos algoritmos es vital saber si un número es par o impar.
# Recuerda que un número es par si al dividirlo entre 2, el residuo (módulo) es exactamente 0.
# Tu tarea: Declara una variable con un número entero cualquiera (por ejemplo, numero = 14).
# Utiliza el operador de módulo (%), el operador de comparación de igualdad (==) y una
# estructura condicional para imprimir "El número es par" o "El número es impar" según
# corresponda.
print("Ejercicio 5")
numero = 14
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
