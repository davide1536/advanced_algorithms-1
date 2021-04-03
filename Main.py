from Grafo import Grafo
from Nodo import Nodo
from Arco import Arco
from heap import heap, HeapDecreaseKey, HeapExtractMin, HeapMinimum, BuildMinHeap, isIn
from Utility import merge, mergeSort_weight
import random
import os
import math
from random import seed
from random import randint
import gc
from time import perf_counter_ns
from collections import defaultdict
import collections
import matplotlib.pyplot as plt


per_m = "algoritmi-avanzati-laboratorio/"
#per_m = ""
#togliere per_m
directory = per_m+"mst_dataset/"
lista_grafi = []


#per fare testing ho messo solo il grafo 8_20
def parsing():
    global directory
    for file in os.listdir(directory):
        if not (file.endswith("100000.txt") or file.endswith("80000.txt") or file.endswith("40000.txt") or file.endswith("20000.txt")):
            crea_grafi(file)



#funzione che dato un path, aggiunge un oggetto grafo 
#alla lista lista_grafi
def crea_grafi(path):

    global lista_grafi
    id2Node = {}
    lista_nodi = set()
    lista_archi = []
    lista_adiacenza = {}
    lista_adiacenza_nodi = {}
    
    f = open(per_m+"mst_dataset/" + path, "r")

    #creo il primo grafo di prova
    prima_riga = f.readline().split(" ")
    n_nodi = prima_riga[0] 
    n_archi = prima_riga[1]
    
    #creo lista di stringhe "nodo1, nodo2, peso"
    righe = f.read().splitlines()
    
    #divido le stringhe in liste di 3 valori [nodo1, nodo2, peso]
    lista_valori = []
    for riga in righe:
        lista_valori.append(riga.split())
    f.close()
        

    #creo i set di nodi e lista archi
    for i in range(0, len(lista_valori)):
        #valori estratti dal file
        nodo_1 = lista_valori[i][0]
        nodo_2 = lista_valori[i][1]
        peso = lista_valori[i][2]
        arco_1 = Arco(nodo_1, nodo_2, peso)
        #arco_2 = Arco(nodo_2, nodo_1, peso)
        
        lista_nodi.add(nodo_1)
        lista_nodi.add(nodo_2)
        lista_adiacenza.setdefault(nodo_1, [])    #inzializzo ogni chiave nodo a un valore list
        lista_adiacenza.setdefault(nodo_2, [])    #inzializzo ogni chiave nodo a un valore list
        lista_adiacenza_nodi.setdefault(nodo_1, [])
        lista_adiacenza_nodi.setdefault(nodo_2, [])

        #forse non serve una lista archi
        lista_archi.append(arco_1)
        #lista_archi.append(arco_2)
    
    for nodo in lista_nodi:
        #se serve un oggetto nodo, crearlo qui!!!!
        obj_nodo = Nodo(nodo)
        id2Node[obj_nodo.nodo] = obj_nodo


    for i in range(0, len(lista_valori)):
        nodo_1 = lista_valori[i][0]
        nodo_2 = lista_valori[i][1]
        peso = lista_valori[i][2]
        lista_adiacenza_nodi[nodo_1].append(id2Node[nodo_2])
        lista_adiacenza_nodi[nodo_2].append(id2Node[nodo_1])
        lista_adiacenza[nodo_1].append(Arco(nodo_1, nodo_2, peso))      #arco(u,v)
        lista_adiacenza[nodo_2].append(Arco(nodo_2, nodo_1, peso))      #arco(v,u)

    
    lista_grafi.append(Grafo(n_nodi, n_archi, lista_nodi, lista_archi, id2Node, lista_adiacenza, lista_adiacenza_nodi))




def measure_run_time(n_instances, graphs, algorithm):
    sum_times = 0
    for i in range(n_instances):
        if algorithm == "prim":
            gc.disable()
            nodo_casuale = next(iter(graphs[i].lista_nodi))    #casuale perchè il set lista_nodi cambia ordine ad ogni parsing
            start_time = perf_counter_ns()
            prim(graphs[i],graphs[i].getNodo(nodo_casuale))
            end_time = perf_counter_ns()
            gc.enable()
            sum_times += end_time - start_time

        if algorithm == "NaiveKruskal":
            pass
        if algorithm == "Kruskal":
            pass
    avg_time = round((sum_times / n_instances)//1000, 3) #millisecondi
    return avg_time




def plot_graph():
    graphs_groupped = defaultdict(list)
    
    #raggruppo i grafi in base alla dimensione dei loro nodi con un dizionario key:n_nodi, value: grafi con quel numero di nodi        
    for i in range (len(lista_grafi)):
        graphs_groupped[int(lista_grafi[i].n_nodi)].append(lista_grafi[i])

    #ordino il dizionario in base alla key (numero di nodi)
    graphs_groupped = collections.OrderedDict(sorted(graphs_groupped.items()))

    #prendo i tempi
    times = [measure_run_time(len(graphs_groupped[key]), graphs_groupped[key], "prim") for key in graphs_groupped]

    #grandezza gruppi
    sizes = [key for key in graphs_groupped]

    #calcolo ratios e costant
    ratios = [None] + [round(times[i+1]/times[i],3) for i in range(len(sizes)-1)]
    c_estimates = [round(times[i]/sizes[i],3) for i in range(len(sizes))]

    print("Size\t\ttTime(ms)\t\tCostant\t\tRatio")
    print(65*"-")
    for i in range(len(sizes)):
        if i < 10:
            print(sizes[i], '' , times[i], '', '', c_estimates[i], '', ratios[i], sep="\t")
        else:
            print(sizes[i], '', times[i], '', c_estimates[i], '', ratios[i], sep="\t")
    print(65*"-")


    #for key in graphs_groupped:
        #print("il grafo con ", key, "nodi ci ha messo (in media):")
        #time = measure_run_time(len(graphs_groupped[key]), graphs_groupped[key], "prim")
        #print (time, "secondi")
        #times.append(time)

    #grafico dei tempi
    plt.plot(graphs_groupped.keys(), times)
    plt.ylabel('run time(ns)')
    plt.xlabel('size')
    plt.show()



def prim(g, radice):
    radice.padre = radice.nodo
    lista_nodi_obj = g.getListaNodi()
    for nodo in lista_nodi_obj:
        nodo.key = float('inf')  #float('inf') indica un valore superiore a qualsiasi altro valore
    radice.key = 0
    q = heap(lista_nodi_obj)
    BuildMinHeap(q)
    while q.heapsize != 0:
        u = HeapExtractMin(q)
        for arco in g.lista_adiacenza[u.nodo]:      #per ogni arco, in lista di adiacenza di u
            nodo_adj = g.getNodo(arco.nodo2)        #g.getNodo(arco.nodo2) = (oggetto) nodo adiacente a u
            if isIn(q,nodo_adj) == 1 and arco.peso < nodo_adj.key:
                nodo_adj.padre = u.nodo
                nodo_adj.key = arco.peso
                HeapDecreaseKey(q, q.vector.index(nodo_adj), nodo_adj.key)
    return g


def naiveKruskal(g):
    grafo_mst = Grafo()
    mergeSort_weight(g.lista_archi, 0, len(g.lista_archi))



######################## MAIN ########################

parsing()
print("FINE PARSING")
plot_graph()
print("fine esecuzione")

# for i in range(0, len(lista_grafi)):
#     nodo_casuale = next(iter(lista_grafi[i].lista_nodi))    #casuale perchè il set lista_nodi cambia ordine ad ogni parsing
#     mst = prim2(lista_grafi[i], lista_grafi[i].getNodo(nodo_casuale))
#     print("grafo con: "+ str(len(mst.lista_nodi)) + " nodi" )
# print("FINE Prim")




##################################PROVA GRAFO PRIM#################################
# nodes =[
# Nodo(1, None, None, None),
# Nodo(2, None, None, None),
# Nodo(3, None, None, None),
# Nodo(4, None, None , None),
# ]

# lista_adiacenza = {}
# for i in range (len(nodes)):
#     lista_adiacenza[i+1] = nodes[i]

# arches = [
# Arco(1,2,1),
# Arco(2,1,1),
# Arco(1,3,4),
# Arco(3,1,4),
# Arco(1,4,3),
# Arco(4,1,3),
# Arco(2,4,2),
# Arco(4,2,2),
# Arco(3,4,5),
# Arco(4,3,5),
# ]
