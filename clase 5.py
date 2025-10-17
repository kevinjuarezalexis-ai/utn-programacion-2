# tp1
class Empleado:
    def __init__(self, nombre, dni, salario_base):
        self._nombre = nombre
        self._dni = dni
        self._salario_base = salario_base

    def calcular_salario(self):
        pass

    def mostrar_info(self):
        print(f"Nombre: {self._nombre}")
        print(f"DNI: {self._dni}")
        print(f"Salario: {self.calcular_salario():}")

class EmpleadoAsalariado(Empleado):
    def calcular_salario(self):
        return self._salario_base * 1.10  # salario base + 10% bono

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, dni, salario_base, horas, valor_hora):
        super().__init__(nombre, dni, salario_base)
        self._horas = horas
        self._valor_hora = valor_hora

    def calcular_salario(self):
        return self._horas * self._valor_hora

def imprimir_detalles(empleado):
    empleado.mostrar_info()

# Ejemplo de uso
asalariado = EmpleadoAsalariado("Ana Pérez", "12345678", 2000)
por_horas = EmpleadoPorHoras("Luis Gómez", "87654321", 0, 120, 15)

imprimir_detalles(asalariado)
print("---")
imprimir_detalles(por_horas)