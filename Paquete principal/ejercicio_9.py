import random
def main():
    filas = 3
    columnas = 3
    matriz = []
    for i in range(filas):
        matriz.append([0] * columnas)
    CrearMatriz(matriz, filas, columnas)
    MostrarMatriz(matriz, filas, columnas)
def CrearMatriz(mat,fill,col):
    for i in range(fill):
        for j in range(col):
            dato = random.randint(0,10)
            mat[i][j] = dato
    return
def MostrarMatriz(mat,fill,col):
    for i in range(fill):
        for j in range(col):
            print(mat[i][j], end="\t")
        print("\n")
    return
main()