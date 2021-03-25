from Grafo import Grafo
from Nodo import Nodo
from Arco import Arco
import os

lista_nodi = []
lista_archi = []
lista_adj = []


f = open("algoritmi-avanzati-laboratorio/mst_dataset/input_random_01_10.txt", "r")
prima_riga = f.readline().split(" ")

grafo_1 = Grafo(prima_riga[0], prima_riga[1], lista_nodi, lista_archi, lista_adj)

for line in f:
    #riga del file formata da [nodo1, nodo2, peso_arco_1]
    riga = line.split(" ")

    #nodo_1 = Nodo(1, [[1,2], [1,4]])


