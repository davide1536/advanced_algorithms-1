from Grafo import Grafo
from Nodo import Nodo
from Arco import Arco
from heap import heap, HeapDecreaseKey, HeapExtractMin, HeapMinimum, BuildMinHeap, isIn
from Utility import merge, mergeSort_weight
import random
import os
import math


per_m = "algoritmi-avanzati-laboratorio/"
#per_m = ""
#togliere per_m
directory = per_m+"mst_dataset/"
lista_grafi = []


#per fare testing ho messo solo il grafo 8_20
def parsing():
    global directory
    for file in os.listdir(directory):
        #if file == "input_random_03_10.txt":    
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



def prim(g, radice):
    radice.padre = radice.nodo
    for nodo in g.getListaNodi():
        nodo.key = float('inf')  #float('inf') indica un valore superiore a qualsiasi altro valore
    radice.key = 0
    q = heap(g.getListaNodi())
    BuildMinHeap(q)
    while q.heapsize != 0:
        u = HeapExtractMin(q)
        print("estraggo il nodo ", u.nodo)
        for v in g.lista_adiacenza_nodi.get(u.nodo): #per ogni nodo v adiacente a u
            for arco in g.lista_adiacenza.get(u.nodo): #cerco l'arco (u,v) tra gli archi adiacenti di u
                if arco.nodo2 == v.nodo or arco.nodo1 == v.nodo:
                    uv = arco
            if isIn(q,v) == 1 and uv.peso < v.key:
                print ("aggiorno il nodo:", v.nodo)
                v.padre = u.nodo
                print ("il padre di", v.nodo, "è ", u.nodo)
                v.key = uv.peso
                print ("la key di ", v.nodo, "è", v.key, "\n ")
                HeapDecreaseKey(q, q.vector.index(v), v.key)



def prim2(g, radice):
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




######################## MAIN ########################

parsing()
print("FINE PARSING")
for i in range(0, len(lista_grafi)):
    nodo_casuale = next(iter(lista_grafi[i].lista_nodi))    #casuale perchè il set lista_nodi cambia ordine ad ogni parsing
    mst = prim2(lista_grafi[i], lista_grafi[i].getNodo(nodo_casuale))
    print("grafo con: "+ str(len(mst.lista_nodi)) + " nodi" )
print("FINE Prim")




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
