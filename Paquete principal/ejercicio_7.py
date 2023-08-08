def main():
    lista = [15,22,53,4,23,41]
    Mayor= num_mayor(lista)
    Menor= num_menor(lista)
    print(f"El mayor en la lista es: {Mayor}")
    print(f"El menor en la lista es {Menor}")
def num_mayor(list):
    mayor = list[0]
    for i in range(len(list)):
        if list[i] > mayor:
            mayor = list[i]
    return mayor
def num_menor(list):
    menor = list[0]
    for i in range(len(list)):
        if list[i] < menor:
            menor = list[i]
    return menor
main()