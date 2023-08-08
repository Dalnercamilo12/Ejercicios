import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def mostrar(self):
        print("Coordenadas:", self.x, self.y)
        
    def cambiar_coordenadas(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y
        
    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)
        return distancia
    
punto_coordenadas1 = Punto(-2, 6)
punto_coordenadas2= Punto(3, 8)

punto_coordenadas1.mostrar()
punto_coordenadas2.mostrar()

punto_coordenadas1.cambiar_coordenadas(8, 10)
punto_coordenadas2.mostrar()

distancia = punto_coordenadas1.calcular_distancia(punto_coordenadas2)
print("Distancia entre punto_coordenadas1 y punto_coordenadas2:", distancia)