import os
import time
class persona:
    #crear constructor
    def __init__(self, nombre, edad, DNI , sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
    
    
    def mostrardatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.DNI} , sexo: {self.sexo}")
        print(f"Peso: {self.peso} , altura: {self.altura}")

# principal
persona1 = persona("soledad", 46, "12345678", "F", 70, 1.75)  
persona2 = persona("juan", 35, "87654321", "M", 80, 1.80)
persona3 = persona("ana", 25, "11223344", "F", 60, 1.65)

persona1.mostrardatos()

time.sleep(5)
os.system("cls")
persona2.mostrardatos()
time.sleep(5)
os.system("cls")
persona3.mostrardatos()
time.sleep(5)
os.system("cls")