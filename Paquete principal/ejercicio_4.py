def main():
    numero=int(input("Ingrese un numero entero:"))
    par(numero)
def par(num):
    if num % 2 == 0:
        print(f"El numero {num} es par")
    else:
        print(f"El numero {num} no es par")
    return
main()