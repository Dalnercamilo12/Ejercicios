import random
def main():
    list=[]
    tamanio= random.randint(1,10)
    for i in range(tamanio):
        dato= random.randint(1,125)
        list.append(dato)
    print(list)
main()