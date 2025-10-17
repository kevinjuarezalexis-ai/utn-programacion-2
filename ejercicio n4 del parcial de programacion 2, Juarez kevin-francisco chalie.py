# ejercicio n4 del parcial de programacion 
# alumno: Juarez kevin alexis- francisco chalie

# agregago que sera abstracto y usaremo lo metodos
from abc import ABC, abstractmethod
#clase padre abstracta
class Mascota(ABC):
    def __init__(self, nombre, edad, raza,):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.__historialmedico = list() #atributo encapsulado

    @abstractmethod #usamos un metodo abstracto
    def emitir_sonido(self):
        pass

    def agregar_historial(self, entrada): #verificamos que no tenga historial para agregar uno
        if not entrada:
            return
        self.__historialmedico.append(entrada)

    def mostrar_historial(self): #mostramos el historial
        return list(self.__historialmedico)
# creamos la clase hijas
class perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza)

    def emitir_sonido(self): # ponemos que hara ruido
        return "Guau"

class gato(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza)
    def emitir_sonido(self):
        return "Meow"

class ave(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza)

    def emitir_sonido(self):
        return "crow"    
    
# ahora creamos datos que seran ejemplo de como funciona
gato1 = gato("Michi", 3, "Siames")
gato1.agregar_historial("Vacunado")
print(f"el gato esta {gato1.emitir_sonido()}")
print(gato1.mostrar_historial())
perro1 = perro("Firulais", 5, "Labrador")
print(f"el perro esta {perro1.emitir_sonido()}")
perro1.agregar_historial("Vacunado")
print(perro1.mostrar_historial())
ave1 = ave("pepita", 1, "loro")
print(f"el ave esta {ave1.emitir_sonido()}")
ave1.agregar_historial("no esta vacunado")
print(ave1.mostrar_historial())

# falta agrega clase relacional de dueños xd