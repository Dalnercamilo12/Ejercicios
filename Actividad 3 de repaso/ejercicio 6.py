class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

Copas = "copas"
oros= "oros"
bastos = "bastos"
espadas = "Espadas"

carta_one= Carta(7, Copas)
carta_two = Carta("Reina",bastos)

print("Carta one Valor:", carta_one.valor, "-Pinta:", carta_one.pinta)
print("Carta two Valor:", carta_two.valor, "-Pinta:", carta_two.pinta)