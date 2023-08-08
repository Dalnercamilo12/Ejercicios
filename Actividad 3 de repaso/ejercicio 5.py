import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_perímetro(self):
        perímetro = 2 * math.pi * self.radio
        return perímetro
    
    def calcular_area(self):
        área = math.pi * self.radio**2
        return área
    
    def punto_pertenece(self, punto):
        distancia = math.sqrt((punto.x - self.centro.x)**2 + (punto.y - self.centro.y)**2)
        return distancia <= self.radio

centro = Punto(2, 9)

mi_circulo = Circulo(centro, 4)

print("Área:", mi_circulo.calcular_area())
print("Perímetro:", mi_circulo.calcular_perímetro())

punto_prueba = Punto(3, 7)
if mi_circulo.punto_pertenece(punto_prueba):
    print("hola ese punto pertenece al círculo.")
else:
    print("Ese punto no pertenece al círculo.")