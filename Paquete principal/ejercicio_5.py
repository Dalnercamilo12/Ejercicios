def main():
    grados= int(input("Ingrese la temperatura en fahrenheit para convertir a celcius:"))
    celcius(grados)
def celcius(grados):
    temperatura= (grados - 32) * 5/9 #formula para convertir fahrenheit a celcius
    """round sirve para redondear el resultado"""
    print(f"La temperatura en celcius es: {round(temperatura, 1)}°")
    return
main()