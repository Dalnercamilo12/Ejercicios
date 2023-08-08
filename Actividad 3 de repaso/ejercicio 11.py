class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Ha recibido {cantidad}.")
        else:
            print("La cantidad a depositar debe ser mayor que cero,Gracias.")
    
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se ha retirado {cantidad}.")
        else:
            print("No se puede realizar el retiro. La cantidad es inválida o excede el saldo disponible.")
    
    def aplicar_cuota(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Se ha aplicado una cuota de manejo del 2%: {cuota}")
    
    def consultar_saldo(self):
        print("Saldo actual:", self.balance)
    
    def mostrar_detalles(self):
        print("Detalles de la cuenta bancaria:")
        print("Número de cuenta:", self.numero_cuenta)
        print("Propietarios:", self.propietarios)
        print("Saldo:", self.balance)
cuenta_principal = CuentaBancaria("122420", ["Dalner", "Isabel"], 200000.0)
cuenta_principal.mostrar_detalles()