
# alumnos: Juarez kevin , Francisco chaile
from abc import ABC, abstractmethod
#colocamos lo de abc de abtracion
#ponemo la clase padre y colocar el metodo abstracto
class Vehiculo(ABC):
    def __init__(self, marca, modelo, años, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.años = años
        self.__kilometraje = None  # un atributo privado
        self.set_kilometraje(kilometraje)
    @abstractmethod #para usar un metodo abstracto
    def calculacosto(self):
        pass

    def mostrarinfo(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Años: {self.años}")
        print(f"Kilometraje: {self.get_kilometraje()} km")

    def get_kilometraje(self):
        return self.__kilometraje

    def set_kilometraje(self, kilometraje):
        if kilometraje < 0:
            raise ValueError("El kilometraje no puede ser menor que 0")
        self.__kilometraje = kilometraje

# creamos la clases hijos que van a heredar, herencia y poli

# clase hija moto
class moto(Vehiculo):
    def __init__(self, marca, modelo, años, kilometraje):
        super().__init__(marca, modelo, años, kilometraje)
    def calculacosto(self):
        return (2025 - self.años) * 1000
# clase hija auto
class auto(Vehiculo):
    def __init__(self, marca, modelo, años, kilometraje):
        super().__init__(marca, modelo, años, kilometraje)
    def calculacosto(self):
        return (2025 - self.años) * 2000
# clase hija camion xd
class camion(Vehiculo):
    def __init__(self, marca, modelo, años, kilometraje):
        super().__init__(marca, modelo, años, kilometraje)
    def calculacosto(self):
        return (2025 - self.años) * 3000

# Ejemplo de uso con un ejemplo de cada clase de hijo
kmmoto = 15000
moto1 = moto("Honda", "CBR", 2020, kmmoto)
moto1.mostrarinfo()
print(f"Costo de mantenimiento: {moto1.calculacosto()}")

kmauto = 3000
auto1 = auto("Fiat", "Palio", 2021, kmauto)
auto1.mostrarinfo()
print(f"Costo de mantenimiento: {auto1.calculacosto()}")

kmcamion = 3000
camion1 = camion("volvo", "FH", 2010, kmcamion)
camion1.mostrarinfo()
print(f"Costo de mantenimiento: {camion1.calculacosto()}") 