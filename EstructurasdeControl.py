#3. Estructuras de Control

#Ejercicio 1 - El termostato inteligente
# Situación: Estás programando el software de un termostato de aire acondicionado.
# El sistema lee la temperatura actual de la habitación.
# Si la temperatura es estrictamente mayor a 25 grados, el programa debe imprimir
# "Encendiendo aire acondicionado". Si es 25 grados o menos, debe imprimir
# "Temperatura adecuada, modo ahorro".
# Tu tarea: Escribe el código utilizando una estructura if-else para simular esta toma de
# decisión. Asume una variable inicial de temperatura, por ejemplo temperatura = 28.

# print("Ejercicio 1")
# temperatura = 28
# if temperatura > 25:
#     print("Encendiendo aire acondicionado.")
# else:
#     print("Temperatura adecuada, modo ahorro.")

#Ejercicio 2 - Clasificación de descuentos
# Situación: Una tienda en línea tiene un sistema de descuentos por volumen de compra.
# Si el total de la compra es mayor o igual a $1000, se aplica un 20% de descuento.
# Si el total es menor a $1000 pero mayor o igual a $500, se aplica un 10% de descuento.
# Si la compra es menor a $500, no hay descuento (0%).
# Tu tarea: Escribe la estructura condicional que evalúe una variable total_compra
# (por ejemplo, con valor 750) e imprima de cuánto es el descuento aplicado
# (ej. "Tienes un 10% de descuento").
# print("Ejercicio 2")
# total_compra = 750
# descuento = 0
# if total_compra >= 1000:
#     descuento = total_compra * 0.20
#     print("Descuento aplicado:", descuento)
# elif total_compra >= 500:
#     descuento = total_compra * 0.10
#     print("Descuento aplicado:", descuento)
# elif total_compra < 500:
#     print("No se aplica descuento. Por ende, se queda en", total_compra, "como el total de la compra.")

#Ejercicio 3 - Taquilla de cine con múltiples condiciones
# Situación: En un cine, para que te den el "Descuento Joven", debes cumplir con dos
# requisitos obligatorios al mismo tiempo: tener menos de 25 años Y presentar tu credencial
# de estudiante.
# Tu tarea: Crea dos variables iniciales: edad = 22 y tiene_credencial = True.
# Utiliza una estructura condicional y el operador lógico and para imprimir
# "Descuento aplicado" si cumple ambas condiciones, o "Precio regular" si le falta alguna
# (o ambas).

# print("Ejercicio 3")
# edad = 22
# tiene_credencial = True
# if edad < 25 and tiene_credencial:
#     print("Descuento aplicado")
# else:
#     print("Precio Regular")

#Ejercicio 4 - Sistema de Login Básico
# Situación: Estás creando la pantalla de inicio de sesión de un sistema.
# Tienes una base de datos simulada donde el usuario correcto es "admin" y la contraseña es
# "secreta123".
# El programa primero debe verificar si el usuario ingresado es correcto.
#   Si el usuario es correcto, evalúa la contraseña: si coincide, imprime "Acceso concedido"; si no, imprime "Contraseña incorrecta".
#   Si el usuario ingresado no es "admin", debe imprimir directamente "Usuario no encontrado".
#   Tu tarea: Utiliza estructuras condicionales anidadas (un if dentro de otro if o dentro del else) para resolver este flujo.

# print("Ejercicio 4")
# usuario = "admin"
# contrasena = "secreta123"
# if usuario == "admin":
#     if contrasena == "secreta123":
#         print("Usuario Concedido")
#     else:
#         print("Contraseña incorrecta")
# else:
#     print("Usuario no encontrado")

#Ejercicio 5 - ¿Par o impar?
# Situación: En muchos algoritmos es vital saber si un número es par o impar.
# Recuerda que un número es par si al dividirlo entre 2, el residuo (módulo) es exactamente 0.
# Tu tarea: Declara una variable con un número entero cualquiera (por ejemplo, numero = 14).
# Utiliza el operador de módulo (%), el operador de comparación de igualdad (==) y una
# estructura condicional para imprimir "El número es par" o "El número es impar" según
# corresponda.

# print("Ejercicio 5")
# numero = 14
# if numero % 2 == 0:
#     print("El numero es par")
# else:
#     print("El numero es impar")

#------------------------------------------------------------------------------------

#3.1. Bucles/loops
#Los Bucles nos permiten repetir un bloque de codigo varias veces. En Python, los mas comunes
#son:

# For Loop
# We can use it to iterate a sequence. It's normally used to repeat code a finite or a
# defined number of times.

# Example

#for variable in sequence:
    # Instructions.

#fruits = ["apple", "banana", "orange"]
#for fruit in fruits:
    #print(fruit)

# While Loop
#It repeats code while the condition is true. It has the next sintaxis:

#while condition:
    #Instructions

# Example

#counter = 0

#while counter < 5:
    #print(counter)
    #counter += 1

# In this example, we have a variable called counter that it's defined with 0.
# Next, we have a while loop that repeats the code while the condition (counter < 5).
# It repeats the code 5 times. Each time the code repeats, it prints into the console the
# number that the variable counter has at the moment before adding 1 to the counter variable.

# Loop Control

# They're special instructions to control the flow of the execution within loops.

# break
# This instruction exits a currently executed loop.
# if counter == 5:
#       break

# continue
# It's used to skip the actual iteration within the loop to start the next iteration.

# Example
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# pass
# It's a command that does nothing. It's oftenly used to mark where it needs to write code for a new
# instruction later.
# for i in range(5):
#     pass

# Exercises

# Exercise 1
# Estás programando el sistema de una nave espacial. Necesitas hacer un conteo regresivo utilizando
# un bucle while. Crea una variable contador que empiece en 5. Utiliza un bucle while que imprima
# el número actual y luego le reste 1 al contador en cada vuelta. El bucle debe detenerse cuando
# el contador llegue a 0. Después del bucle (fuera de la indentación), imprime "¡Despegue!".
print("Exercise 1")
counter = 5
while counter > 0:
    print(counter)
    counter -= 1

print("Despegue!")

# Exercise 2
# Tienes una lista con las calificaciones de un grupo de estudiantes. Solo quieres mostrar en
# pantalla las calificaciones que son aprobatorias (mayores o iguales a 70). Utiliza un
# bucle for para recorrer la lista calificaciones. Dentro del bucle, usa un if para verificar si la
# calificación actual es mayor o igual a 70. Si es así, imprímela.
print("Exercise 2")
grades = [45, 85, 30, 90, 70, 55, 100]
print("Passing Grades")
for grade in grades:
    if grade >= 70:
        print(grade)

# Exercise 3
# Quieres comprarte un teclado mecánico que cuesta $150. Actualmente tienes $0. Cada mes logras
# ahorrar $30. Crea una variable ahorro = 0. Utiliza un bucle while que se ejecute mientras el
# ahorro sea menor a 150. En cada iteración (cada mes), suma 30 al ahorro e imprime un mensaje que
# diga "Ahorro actual: [cantidad]". Cuando el bucle termine, imprime "¡Meta alcanzada!".
print("Exercise 3")
savings = 0
while savings < 150:
    savings += 30
    print("Money saved:", savings)

print("Goal achieved")

# Exercise 4
# Estás auditando los registros de acceso a un servidor. Tienes una lista de usuarios que intentaron
# ingresar. Tu sistema debe revisar uno por uno, pero si detecta que el usuario "hacker99" intentó
# entrar, debe detener completamente la revisión de inmediato para levantar una alerta. Usa un bucle
# for para recorrer la lista de usuarios. En cada iteración, imprime "Revisando a:
# [nombre de usuario]". Sin embargo, si el usuario es "hacker99", imprime "¡ALERTA DE INTRUSO!"
# y utiliza la instrucción break para detener el bucle por completo.
print("Exercise 4")
users = ["ana_perez", "dev_master", "hacker99", "admin_root", "carlos_88"]
for user in users:
    if user != "hacker99":
        print("Checking user", user)
    else:
        print("INTRUDER ALERT!")
        break

# Exercise 5
# Tienes una lista con los precios de los productos vendidos hoy. Por un error del sistema,
# algunos precios se registraron como 0 o con números negativos. Necesitas calcular la suma total de
# las ventas, pero ignorando los valores inválidos. Crea una variable total = 0. Recorre la lista
# precios con un bucle for. Si el precio es menor o igual a 0, utiliza continue para saltar a la
# siguiente iteración sin sumarlo. Si es un precio válido, súmalo a la variable total. Al final,
# imprime el valor de total.
print("Exercise 5")
prices = [120, -15, 340, 0, 89, -5, 200]
total = 0
for price in prices:
    if price <= 0:
        continue
    else:
        total += price

print("Final Total:", total)

