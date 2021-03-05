import numpy as np
import math


def click(m, v):
    matrizEstado = m * v
    vectorEstado = list()
    for i in matrizEstado:
        a = 0
        for j in i:
            a += j
        vectorEstado.append(a)
    return matrizEstado, np.array(vectorEstado)


def manyClicks(m, v, clicks):
    if clicks <= 1:
        s = click(m, v)
    else:
        tempS = click(m, v)
        s = manyClicks(m, tempS[1], clicks - 1)
    return s

def dobleRendijaProb(rendijas,receptores):
    dimension = 1+rendijas+receptores
    matriz = np.zeros((dimension,dimension))
    vector = np.zeros(dimension)
    vector[0] = 1
    p1 = 1/rendijas
    p2 = receptores/rendijas
    for i in range(rendijas):
        matriz[i + 1][0] = p1
    if not(p2.is_integer()):
        p2 = math.ceil(receptores/rendijas)
        k = 1
        j = 1
        for i in range(rendijas + 1, len(matriz)):
            matriz[i][j] = 1/p2
            if k  == p2:
                j += 1
                matriz[i][j] = 1 / p2
                k = 1
            else:
                k += 1

    else:
        k = 1
        j = 1
        for i in range(rendijas + 1, len(matriz)):
            matriz[i][j] = 1 / p2
            if k == p2:
                j += 1
                k = 1
            else:
                k += 1
    for i in range(rendijas +1, len(matriz)):
        matriz[i][i] = 1
    a = manyClicks(matriz,vector,2)
    print("Matriz estado:\n", a[0])
    print("vector estado:\n", a[1])
    return a[1]


def main():
    #Canicas
    m = np.array([[0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 1],
                  [0, 0, 0, 1, 0, 0],
                  [0, 0, 1, 0, 0, 0],
                  [1, 0, 0, 0, 1, 0]])
    v2 = np.array([6, 2, 1, 5, 3, 10])
    a = manyClicks(m, v2, 1)
    #Varias Rendijas Probabilisticas
    print("Matriz estado:\n", a[0])
    print("vector estado:\n", a[1])
    rendijas = 2
    receptores = 5
    vector = dobleRendijaProb(rendijas,receptores)
    #Varias Rendijas Cuanticas

if __name__ == '__main__':
    main()
