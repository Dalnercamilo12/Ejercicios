class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Ha recibido {cantidad} en la cuenta.")
        else:
            print("La cantidad debe ser mayor que cero, Gracias.")
    
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se ha retirado {cantidad}.")
        else:
            print("No se puede realizar el retiro. La cantidad es inválida o excede el saldo disponible.")

cuenta_principal = CuentaBancaria("122420", ["Dalner", "Isabel"], 200000.0)
cuenta_principal.retirar(3600.0)
print("Nuevo balance:", cuenta_principal.balance)