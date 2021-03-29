from Grafo import Grafo
from Nodo import Nodo
from Arco import Arco
from UnionFind import UnionFind
import os
import math
from heap import heap


directory = "algoritmi-avanzati-laboratorio/mst_dataset"
lista_grafi = []


#controllo nodi
def check_nodi(lista_grafi):
    for grafo in lista_grafi:
        nodi = len(grafo.lista_nodi) == int(grafo.n_nodi)
    return nodi



#controllo archi
def check_archi(lista_grafi):
    for grafo in lista_grafi:
        numero_archi = 0
        for nodo in grafo.lista_adiacenza.keys():
            numero_archi += len(grafo.lista_adiacenza[nodo])
            archi = numero_archi/2 == int(grafo.n_archi)
    return archi



def check_generale():
    print("numero grafi = " + str(len(lista_grafi)))
    print("Il numero di nodi è giusto in ogni grafo? " + str(check_nodi(lista_grafi)))
    print("Il numero di archi è giusto in ogni grafo? " + str(check_archi(lista_grafi)))
    #controllo numr



#per fare testing ho messo solo il grafo 8_20
def parsing():
    global directory
    for file in os.listdir(directory):
        if file == "input_random_01_10.txt":
            crea_grafi(file)



def crea_grafi(path):

    global lista_grafi
    lista_nodi = set()
    lista_archi = []
    lista_adiacenza = {}
    lista_adiacenza_nodi = {}
    
    f = open("algoritmi-avanzati-laboratorio/mst_dataset/" + path, "r")

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
        arco_2 = Arco(nodo_2, nodo_1, peso)
        
        lista_nodi.add(nodo_1)
        lista_nodi.add(nodo_2)
        lista_adiacenza.setdefault(nodo_1, [])    #inzializzo ogni chiave nodo a un valore list
        lista_adiacenza.setdefault(nodo_2, [])    #inzializzo ogni chiave nodo a un valore list
        lista_adiacenza_nodi.setdefault(nodo_1, [])    
        lista_adiacenza_nodi.setdefault(nodo_2, [])    

        #forse non serve una lista archi
        lista_archi.append(arco_1)
        lista_archi.append(arco_2)
    
    #for nodo in lista_nodi:
        #se serve un oggetto nodo, crearlo qui!!!!
        #obj_nodo = Nodo(nodo, altri_attributi)
        #lista_adiacenza.setdefault(nodo, [])    #inzializzo ogni chiave nodo a un valore list


    for i in range(0, len(lista_valori)):
        nodo_1 = lista_valori[i][0]
        nodo_2 = lista_valori[i][1]
        peso = lista_valori[i][2]
        lista_adiacenza_nodi[nodo_1].append(nodo_2)
        lista_adiacenza_nodi[nodo_2].append(nodo_1)
        lista_adiacenza[nodo_1].append(Arco(nodo_1, nodo_2, peso))      #arco(u,v)
        lista_adiacenza[nodo_2].append(Arco(nodo_2, nodo_1, peso))      #arco(v,u)

    lista_grafi.append(Grafo(n_nodi, n_archi, lista_nodi, lista_archi, lista_adiacenza, lista_adiacenza_nodi))



#algoritmo merge
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
        if left[i] <= right[j]:
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



def mergeSort(array, p, r):
    if p < r:
        q = (p+r)//2
        mergeSort(array, p, q)
        mergeSort(array, q+1, r)
        merge(array, p, q, r)
        


#def unionFind():



parsing()

for k,v in lista_grafi[0].lista_adiacenza.items():
    for arco in v:
        print(k + " : "+ "( " + arco.nodo1 + ", " + arco.nodo2 + ", " + str(arco.peso) + ")")