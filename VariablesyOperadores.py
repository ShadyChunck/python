#Codigo de Python
# print("Hola, Mundo")

# #Datos basicos
# a = b = c = 2
# d = 3
# print(a == d)

#Operadores
#Ejercicio 1
print("Ejercicio 1")
escritorio = 120
silla_ergonomica = 85
lampara = 15
costo_total = escritorio + silla_ergonomica + lampara
cupon_descuento = 0.20
descuento = costo_total * cupon_descuento
costo_final = costo_total - descuento
print("El costo final es:", costo_final)

#Ejercicio 2
print("Ejercicio 2")
microchips = 347
capacidad_por_caja = 12
cajas_posibles = microchips // capacidad_por_caja
print("Se pueden empacar un total de", cajas_posibles, "cajas")

#Ejercicio 3
print("Ejercicio 3")
microchips_sobrados = microchips % capacidad_por_caja
print("Sobran", microchips_sobrados, "microchips")

#Ejercicio 4
print("Ejercicio 4")
virus_alienigena = 5
minutos = 6
tamano_final = virus_alienigena * (2 ** minutos)
print("El tamaño final del virus es de", tamano_final, "unidades")

#Ejercicio 5
print("Ejercicio 5")
print("El promedio del alumno es de:", ((8.5 + 9.0 + 7.5) / 3))