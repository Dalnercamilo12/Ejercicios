class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectángulo:
    def __init__(self, esquina_sup_izq, esquina_inf_der):
        self.esquina_sup_izq = esquina_sup_izq
        self.esquina_inf_der = esquina_inf_der
    
    def calcular_el_perímetro(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        perímetro = 2 * (base + altura)
        return perímetro
    
    def calcular_el_area(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        área = base * altura
        return área
    
    def es_cuadrado(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        return base == altura
    
esquina_sup_izq = Punto(2, 6)
esquina_inf_der = Punto(4, 3)

mi_rectángulo = Rectángulo(esquina_sup_izq, esquina_inf_der)

print("Perímetro:", mi_rectángulo.calcular_el_perímetro())
print("Área:", mi_rectángulo.calcular_el_area())

if mi_rectángulo.es_cuadrado():
    print("Hola ese rectángulo es un cuadrado.")
else:
    print("Lo siento ese rectángulo no es un cuadrado.")