from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo, años, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.años = años
        self.__kilometraje = None  # atributo privado
        self.set_kilometraje(kilometraje)

    @abstractmethod
    def calculacosto(self):
        pass

    def mostrarinfo(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Años: {self.años}")
        print(f"Kilometraje: {self.get_kilometraje()} km")

    def get_kilometraje(self):
        return self.__kilometraje.get_km()

    def set_kilometraje(self, kilometraje):
        if kilometraje.get_km() < 0:
            raise ValueError("El kilometraje no puede ser menor que 0")
        self.__kilometraje = kilometraje

class Kilometraje(ABC):
    def __init__(self, km):
        self.set_km(km)

    @abstractmethod
    def get_km(self):
        pass

    @abstractmethod
    def set_km(self, km):
        pass

class KilometrajeSimple(Kilometraje):
    def __init__(self, km):
        super().__init__(km)

    def get_km(self):
        return self.km

    def set_km(self, km):
        if km < 0:
            raise ValueError("El kilometraje no puede ser menor que 0")
        self.km = km

class moto(Vehiculo):
    def __init__(self, marca, modelo, años, kilometraje):
        super().__init__(marca, modelo, años, kilometraje)

    def calculacosto(self):
        return (2025 - self.años) * 1000

class auto(Vehiculo):
    def __init__(self, marca, modelo, años, kilometraje):
        super().__init__(marca, modelo, años, kilometraje)

    def calculacosto(self):
        return (2025 - self.años) * 2000

class camion(Vehiculo):
    def __init__(self, marca, modelo, años, kilometraje):
        super().__init__(marca, modelo, años, kilometraje)

    def calculacosto(self):
        return (2025 - self.años) * 3000

# Ejemplo de uso
kmmoto = KilometrajeSimple(10000)
moto1 = moto("Honda", "CBR", 2020, kmmoto)
moto1.mostrarinfo()
print(f"Costo de mantenimiento: {moto1.calculacosto()}")

kmauto = KilometrajeSimple(3000)
auto1 = auto("Fiat", "Palio", 2021, kmauto)
auto1.mostrarinfo()
print(f"Costo de mantenimiento: {auto1.calculacosto()}")

kmcamion = KilometrajeSimple(3000)
camion1 = camion("volvo", "FH", 2010, kmcamion)
camion1.mostrarinfo()
print(f"Costo de mantenimiento: {camion1.calculacosto()}")