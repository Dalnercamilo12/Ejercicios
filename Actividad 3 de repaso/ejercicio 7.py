class Cuenta_Bancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

cuenta_principal = Cuenta_Bancaria("122420", ["Dalner", "Isabel"], 200000.0)

print("Número de cuenta:", cuenta_principal.numero_cuenta)
print("Propietarios:", cuenta_principal.propietarios)
print("Balance:", cuenta_principal.balance)