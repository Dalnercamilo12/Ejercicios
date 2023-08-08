def main():
    lista = [15,22,53,4,23,4]
    acumulado = MediaAritmetica(lista)
    print(f"La media aritmetica de la lista es: {round(acumulado,1)}")
def MediaAritmetica(list):
    sumanumeros = 0
    contador = 0
    for i in range(len(list)):
        sumanumeros = list[i] + sumanumeros
        contador= contador + 1
    total=sumanumeros/contador
    return total
main()