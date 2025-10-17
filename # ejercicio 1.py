# ejercicio 1
cont = 1
a = 1


def lista (nombre, apellido, curso, materia, promedio):
    print(nombre, apellido)
    print("curso:", curso, "materia:", materia, " promedio:", promedio)
    if promedio >= 7:
        print("El alumno ha aprobado.")
    elif promedio < 4:
        print("El alumno ha reprobado.")

print("ingrese la cantidad de alumnos que ingresan curso")
cantalum = int(input())

while cantalum >= cont:
    print("ingrese su nombre")
    nombre = input()
    print("ingrese su apellido")
    apellido = input()
    print("ingrese su curso")
    curso = input()
    print("ingrese su materia")
    materia = input()
    print("ingrese su 3 nota")
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    promedio = (nota1 + nota2 + nota3) / 3
    print("El promedio es ", promedio)
    
    lista(nombre, apellido, curso, materia, promedio)
    cont += 1
print("listo xd ")
