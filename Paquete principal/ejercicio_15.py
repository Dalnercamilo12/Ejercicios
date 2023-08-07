def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]
def main():
    cadena = input("Ingrese una cadena de texto: ")
    if es_palindromo(cadena):
        print("es un palíndromo.")
    else:
        print("{no es un palíndromo.")
if __name__ == "__main__":
    main()




