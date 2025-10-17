# tp 2
a = "0"
class operacion:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


class suma(operacion):
    def calcular(self):
        return self.num1 + self.num2
    
class resta(operacion):
    def calcular(self):
        return self.num1 - self.num2
    
class multiplicacion(operacion):
    def calcular(self):
        return self.num1 * self.num2

class division(operacion):
    def calcular(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "no se puede dividir por cero"
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
while True:
    

    a = input("Ingrese la operación a realizar (suma, resta, multiplicacion, division) o 'salir' para terminar: ")
    if a == "suma":
        suma_op = suma(num1, num2)
        print("Suma:", suma_op.calcular())
    elif a == "resta":
        resta_op = resta(num1, num2)
        print("Resta:", resta_op.calcular())
    elif a == "multiplicacion":
        multi_op = multiplicacion(num1, num2)
        print("Multiplicación:", multi_op.calcular())
    elif a == "division":
        divi_op = division(num1, num2)
        print("División:", divi_op.calcular())
    elif a == "salir":
        print("bye xd")
        break
    