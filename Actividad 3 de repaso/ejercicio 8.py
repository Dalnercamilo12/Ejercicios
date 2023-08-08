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
            
cuenta_principal = CuentaBancaria("122420", ["Dalner", "Isabel"], 200000.0)
cuenta_principal.depositar(900.0)
print("balance:", cuenta_principal.balance)