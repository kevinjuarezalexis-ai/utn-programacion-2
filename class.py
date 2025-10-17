from abc import ABC, abstractmethod

class vehiculo:
    def __init__(self,marca,modelo,años,kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.años = años
        self.kilometraje = kilometraje


    def calculacosto(self,marca,modelo,años):
        pass
        

    def mostrarinfo(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Años: {self.años}")
        print(f"Kilometraje: {self.kilometraje.get_km()} km")

class Kilometraje:
    def __init__(self, km):
        self.km = km  

    def get_km(self):
        return self.km

    def set_km(self,km):
        if km >= 0:
            self.km = km

class moto(vehiculo):
         def __init__(self,marca,modelo,años):
          super().__init__(marca,modelo,años)
          self.marca = marca
          self.modelo = modelo
          self.años = años

         def calculacosto (self,años):
          return 2025 - self.años * 1000
         
        
class auto(vehiculo):
    def __init__(self,marca,modelo,años):
          super().__init__(marca,modelo,años)
          self.marca = marca
          self.modelo = modelo
          self.años = años

class camion(vehiculo):
     def __init__(self,marca,modelo,años):
          super().__init__(marca,modelo,años)
          self.marca = marca
          self.modelo = modelo
          self.años = años
        
kmmoto = Kilometraje(10000)
moto1 = vehiculo("Honda", "CBR", 2020, kmmoto)
moto1.mostrarinfo()
moto1.calculacosto()
kmauto = Kilometraje(3000)
auto1 = vehiculo("fiat", "palido", 2021, kmauto)
auto1.mostrarinfo()
auto1.calculacosto
