def main():
    lista=[]
    lista = [15,22,53,4,23,4]
    acumulado = suma_listas(lista)
    print(f"El total del acumulado en la lista es: {acumulado}")
def suma_listas(list):
    total = 0
    for i in range(len(list)):
        total = list[i] + total
    return total
main()
