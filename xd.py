print("soy un director")
alumnos = int(input("Ingrese la can"))
if alumnos >= 100:
    print ("el costo de cada alm es 6500")
elif 50 <= alumnos < 100:
    print ("el costo de cada alm es 7000")
elif 30 <= alumnos < 50:
    print ("el costo de cada alm es 9500")
else:
    print ("es 15k")