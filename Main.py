from Grafo import Grafo
from Nodo import Nodo
from Arco import Arco
from UnionFind import UnionFind
from heap import heap
import os
import math
from heap import*


directory = "mst_dataset/"
lista_grafi = []


#per fare testing ho messo solo il grafo 8_20
def parsing():
    global directory
    for file in os.listdir(directory):
        if file == "input_random_03_10.txt":
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
    
    f = open("mst_dataset/" + path, "r")

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


# algoritmo merge modificato per confrontare i pesi degli archi, data una lista archi
# p, q, r sono indici dell'array tali che p <= q < r
# gli indici dividono l'array in sottosequenze t.c. A[p..q] A[q+1..r] 
def merge(array, p, q, r):
    #lunghezza sottoarray A[p..q]
    n1 = q-p+1
    #lunghezza sottoarray A[q+1..r]
    n2 = r-q
    left = [0] * n1
    right = [0] * n2
    
    for i in range(0, n1):
        left[i] = array[p+i]
    
    for i in range(0, n2):
        right[i] = array[q+i+1]
    
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if left[i].peso <= right[j].peso:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    #elementi rimanenri di left e right
    #non sono riuscito ad implementarlo con il valore infito del libro :(
    while i < n1:
        array[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = right[j]
        j += 1
        k += 1


def mergeSort_weight(array, p, r):
    if p < r:
        q = (p+r)//2
        mergeSort_weight(array, p, q)
        mergeSort_weight(array, q+1, r)
        merge(array, p, q, r)


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
                HeapDecreasKey(q, q.vector.index(v), v.key)




        

parsing()
for nodo in lista_grafi[0].getListaNodi():
    print (nodo.nodo)
print ("\n")
print(lista_grafi[0].getListaNodi().index(lista_grafi[0].getNodo('2')))

# for nodo in lista_grafi[0].lista_adiacenza_nodi['1']:
#     print(nodo.nodo)    
# for v in lista_grafi[0].lista_adiacenza['1']:
#     print("arco" + str(v.getArco()))
        
prim(lista_grafi[0], lista_grafi[0].getNodo('1'))
# for nodo in lista_grafi[0].id2Node.values():
#     print("sono il nodo: ", nodo.nodo, "il mio padre è: ",nodo.padre)

#print(len(lista_grafi))
#print("fine")
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
