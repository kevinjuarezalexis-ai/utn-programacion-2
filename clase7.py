import os
import time
os.system ("cls")

class persona:
    #crear constructor
    def __init__(self, nombre, edad, DNI , sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.DNI}")
        print(f"Sexo: {self.sexo}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}")
