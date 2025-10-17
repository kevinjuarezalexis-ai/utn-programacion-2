# ejercicio 2

def xdxd():
    print("patentes:",patente)
    print("horas en total", hora2)
    if horas <= 2:
        total2 = hora2 * 1000
        print("el total a pagar es :", total2)
    elif horas <= 5:
        total2 = (hora2 * 800) 
        print("el total a pagar es :", total2)
    elif horas > 6:
        total2 = (hora2 * 500)
        print("el total a pagar es :", total2)
    print("total a pagar", total)

hora2 = 0   
a = 1
print("estacionamiento xd")

autos = int(input("ingrese cantidad de autos: "))
while autos >= a:
    patente = input("ingrese la patente del auto: ")
    horas = int(input("ingrese la cantidad de horas que estuvo el auto: "))
    hora2 = hora2 + horas
    if horas <= 2:
        total = horas * 1000
        print("el total a pagar es :", total)
    elif horas <= 5:
        total = (horas * 800) 
        print("el total a pagar es :", total)
    elif horas >= 6:
        total = (horas * 500)
        print("el total a pagar es :", total)
    a += 1
xdxd()