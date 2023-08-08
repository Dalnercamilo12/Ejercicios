import random
def main():
    list= []
    centinela = input("presione una tecla o digite 0 para terminar:")
    contador = 0
    while centinela != "0":
        dato = random.randint(1,100)
        if dato % 2 == 0:
            list.append(dato)
            print(f"El numero {dato} se ha añadido a la lista ")
            contador = contador + 1
            print(f"en la lista se han añadido: {contador} numeros")
        else:
            centinela = input("para continuar presione cualquier tecla o digite 0 para terminar:")
    print(list)
main()