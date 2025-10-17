# clase 2 xd
print("hello world")
edad2 = (input("ingrese su edad: "))
edad1 = 10
print(edad1)
print(type(edad2)) # tipo indica el tipo de dato almacenado en la variable
precio = 10.50
print(type(precio)) 
print(precio)
# booleana
respuesta = False

print(respuesta)

print(type(respuesta)) 

import os #libreria con metodo de sistema

os.system("cls") #limpiar pantalla

# operadores de comparacion
# > mayor < menor >= mayor o igual <= menor o igual , y = igual
# == igual, != diferente
# operadores logicos
# and y or - o not - (y/o)
# if condicionales
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    if edad > 40 :
        print("sos muy mayor xd")
    else:
        print("tenes entre 18 y 40")
else:
    if edad <= 10 :
        print("sos un niño xd")
    else:
        print("sos menor de edad xd")

# if else : analiza la primera condicion verdadera realizar un menu
# o evaluar varias opciones posibles

# realizar un programa que evalue si puede votar en prox elecciones
if 0 < edad < 16:
    print(f" no vota, tiene {edad} años")
elif edad <= 0:
    print(f"Edad no válida para votar")
elif 16 <= edad < 18:
    print(f"Puede votar, pero no tiene la obligacion")
elif 18 <= edad < 70:
    print(f"obligacion votar {edad} años")
else:
    print("no es argentino")

print("fin de evaluacion ")

os.system("cls")

#El director de una escuela está organizando un viaje de estudios, y requiere
#determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la empresa de
#viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el
#costo por cada alumno es de $6500; de 50 a 99 alumnos, el costo es de $7000, de 30 a 49,
#de $9500, y si son menos de 30, el costo del alquiler del colectivo es de $15000, sin importar el número de alumnos.

print("soy el director de una escuela")
cantidadalumnos = int(input("ingreso cantidad de alumnos: "))

if cantidadalumnos >= 100:
    costoalumno = 6500
    total = cantidadalumnos * costoalumno
    print(f"el costo es {costoalumno}, y el total es de {total}")
elif 50 <= cantidadalumnos < 100:
    costoalumno = 7000
    total = cantidadalumnos * costoalumno
    print(f"el costo es {costoalumno}, y el total es de {total}")
elif 30 <= cantidadalumnos < 50:
    costoalumno = 9500
    total = cantidadalumnos * costoalumno
    print(f"el costo es {costoalumno}, y el total es de {total}")
else:
    total = 15000
    print(f"el costo del alquiler del colectivo es de {total}")
    