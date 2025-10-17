import os #libreria con metodo de sistema

# imprimir el valor de i siempre q sea menor q 6
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print(" termino ciclo ")

# x = 5
# print("es 5" if x == 5 else "no es 5")   operador ternario
# usaremos junto a while

a = 1
while a < 6: print(a); a += 1  # en una sola linea
print("es 5" if a == 5 else "no es 5")

mensaje = input("para continuar presione s:  ")
while mensaje == "s":
    print ("estas en bucle")
    mensaje = input("para volver ver mensaje presione s:  ")
    break

def holaxd():
    e = 1
    while e < 6:
        print(e)
        e += 1
    else:
        print(" termino ciclo ")

holaxd()