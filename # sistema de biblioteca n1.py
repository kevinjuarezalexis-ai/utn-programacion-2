# sistema de biblioteca
from abc import ABC, abstractmethod
opcion = text = ""
class materialbibioteca(ABC):
    def __init__(self, titulo, autor,):
        self.titulo = titulo
        self.autor = autor
        self.__disponible = True
    @abstractmethod
    def mostrarinfo(self):
        pass

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False
    def devolver(self):
        self.__disponible = True

class libro(materialbibioteca):
    def __init__(self, titulo, autor):
        super().__init__(titulo, autor)
    
    def mostrarinfo(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}"

class revista(materialbibioteca):
    def __init__(self, titulo, autor):
        super().__init__(titulo, autor)
    
    def mostrarinfo(self):
        return f"Revista: {self.titulo}, Autor: {self.autor}"

libro1 = libro("Cien Años de Soledad", "Gabriel García Márquez")
print(libro1.mostrarinfo())
print("esta dispnible:", libro1.prestar())
revista1 = revista("National Geographic", "Varios Autores")
print(revista1.mostrarinfo())
print("esta dispnible:", revista1.prestar())
print("desea pillar un libro xd?")
xd = input("si o no:   ")
if xd == "si":
    opcion = input("que desea pillar libro o revista?   ")
    if opcion == "libro":
        print(libro1.mostrarinfo())
        print("Has prestado el libro.", libro1.prestar())
    elif opcion == "revista":
       print(revista1.mostrarinfo())
       print("Has prestado la revista.", revista1.prestar())
else:
    print("gracias por usar el sistema de biblioteca")