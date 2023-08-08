def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado
def main():
    numero = int(input("Ingrese un numero entero para calcular su factorial:"))
    resultado_factorial = factorial(numero)
    print(f"El factorial de {numero} es: {resultado_factorial}")
main()