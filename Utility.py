#classe utile per la Union-Find e mergeSort
#capitolo 21.3/4 del libro
################# non testato #################
from Nodo import Nodo


################# Merge + MergeSort #################

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



################# Union-Find #################

def makeSet(nodo):
    nodo.padre = nodo
    nodo.rank = 0

def link(nodo1, nodo2):
    if nodo1.rank > nodo2.rank:
        nodo2.padre = nodo1
    else:
        nodo1.padre = nodo2
        if nodo1.rank == nodo2.rank:
            nodo2.rank += 1

def union(nodo1, nodo2):
    link(nodo1, nodo2)

def findSet(nodo1):
    if nodo1 != nodo1.padre:
        nodo1.padre = findSet(nodo1.padre)
    return nodo1.padre

    