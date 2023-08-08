def main():
    radio = int(input("ingrese el radio del circulo:"))
    area = CalcularArea(radio)
    print(f"El area del circulo es:{area}")
def CalcularArea(r):
    Area= 3.14 * r**2
    return Area
main()