#Tarea1
import math

print("Para saber el area total del muñeco, porfavor digite las siguentes medidas")
base_triang = float (input ("¿Cual es la base del triangulo?"))
altura_triang = float (input ("¿Cual es la altura del triangulo?"))
area_triang = float (base_triang * altura_triang / 2)
print(f"El area del triangulo es: {area_triang:.2f}")


base_torso = float (input ("¿Cual es la base del rectangulo del torso? "))
altura_torso = float (input ("¿Cual es la altura del rectangulo del torso? "))
area_torso = float (base_torso * altura_torso)
print(f"El area del rectangulo del torso es: {area_torso:.2f}")


base_brazos = float (input ("¿Cual es la base del brazo? "))
altura_brazos = float (input ("¿Cual es la altura del brazo? "))
area_brazo = float (base_brazos * altura_brazos)
area_brazos = float ((base_brazos * altura_brazos) * 2)
print(f"El area del rectangulo del brazo es:{area_brazo:.2f}")
print(f"La suma del area de ambos brazos juntos seria: {area_brazos:.2f}")


base_piernas = float (input ("¿Cual es la base de una pierna? "))
altura_piernas = float (input ("¿Cual es la altura de la pierna? "))
area_pierna = float (base_piernas * altura_piernas)
area_piernas = float ((base_piernas * altura_piernas) * 2)
print(f"El area del rectangulo de una pierna es: {area_pierna:.2f}")
print(f"La suma del area de ambas piernas juntas seria: {area_piernas:.2f}")


radio_cabeza = float (input ("Por ultimo, ¿Cual es el radio del circulo? "))
area_circulo = float (math.pi * (radio_cabeza ** 2))
print(f"El area del circulo es: {area_circulo:.2f}")

area_total = area_torso + area_brazos + area_piernas + area_triang + area_circulo

print(f"El area total de su nuevo muñeco es de: {area_total:.2f}")















#

