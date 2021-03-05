import numpy as np
import math
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

def mod_comp(num):
    a = np.real(num)
    b = np.imag(num)
    return math.sqrt((a ** 2) + (b ** 2))

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

def dobleRendijaCuantum(rendijas,receptores):
    dimension = 1+rendijas+receptores
    matriz = np.zeros((dimension,dimension),dtype=complex)
    vector = np.zeros(dimension,dtype=complex)
    vector[0] = 1
    p1 = 1/math.sqrt(rendijas)
    p2 = receptores/rendijas
    for i in range(rendijas):
        matriz[i + 1][0] = p1
    if not(p2.is_integer()):
        p2 = math.ceil(receptores/rendijas)
        k = 1
        j = 1
        for i in range(rendijas + 1, len(matriz)):
            if i == rendijas + 1:
                a = (-1 + 1j)/math.sqrt(p2*rendijas)
            elif k != p2:
                a = (-1 - 1j)/math.sqrt(p2*rendijas)
            elif k == p2:
                a = (1 - 1j)/math.sqrt(p2*rendijas)
            matriz[i][j] = a
            if k  == p2:
                j += 1
                matriz[i][j] = (-1 + 1j)/math.sqrt(p2*rendijas)
                k = 1
            else:
                k += 1
    else:
        k = 1
        j = 1
        for i in range(rendijas + 1, len(matriz)):
            if k == 1:
                a = (-1 + 1j)/math.sqrt(p2*rendijas)
            elif k != p2:
                a = (-1 - 1j) / math.sqrt(p2 * rendijas)
            elif k == p2:
                a = (1 - 1j) / math.sqrt(p2 * rendijas)
            matriz[i][j] = a
            if k == p2:
                j += 1
                k = 1
            else:
                k += 1
    for i in range(rendijas +1, len(matriz)):
        matriz[i][i] = 1
    a = manyClicks(matriz,vector,2)
    vectorProb = []
    for i in a[1]:
        vectorProb.append(mod_comp(i)*mod_comp(i))
    print("Matriz estado:\n", a[0])
    print("vector estado:\n", vectorProb)
    return vectorProb

def graphVector(vector):
    grid = [x for x in range(len(vector))]
    plt.bar(grid, vector)
    plt.show()

def main():
    #TestCase1: Canicas
    m = np.array([[0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 1],
                  [0, 0, 0, 1, 0, 0],
                  [0, 0, 1, 0, 0, 0],
                  [1, 0, 0, 0, 1, 0]])
    v2 = np.array([6, 2, 1, 5, 3, 10])
    a = manyClicks(m, v2, 1)
    print("Matriz estado:\n", a[0])
    print("vector estado:\n", a[1])
    #TestCase2: Varias Rendijas Probabilisticas
    rendijas = 2
    receptores = 5
    vector1 = dobleRendijaProb(rendijas,receptores)
    #TestCase3: Varias Rendijas Cuanticas
    rendijas = 2
    receptores = 5
    vector2 = dobleRendijaCuantum(rendijas,receptores)
    #TestCase4: Graficar Vector de estado
    graphVector(a[1])
    graphVector(vector1)
    graphVector(vector2)

if __name__ == '__main__':
    main()
