#classe utile per la Union-Find e mergeSort
#capitolo 21.3/4 del libro
################# non testato #################
import copy
from Nodo import Nodo
from Grafo import Grafo


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

# Complessità O(n)
# - se G non ha un ciclo allora G è un albero ed m = n-1
# - se G ha un ciclo allora dopo aver attraversato al più n archi la procedura termina 
#   (viene scoperto un arco all'indietro)
#
# INPUT : grafo e nodo iniziale
# OUTPUT : true, se c'è un ciclo, false altrimenti
def dfs_ciclo(g, u, padri, visitati):
    visitati[int(u.nodo)] = 1
    for v in g.lista_adiacenza_nodi[u.nodo]:
        if v.nodo != padri[int(u.nodo)]:       # escludo il padre dalla lista degli adiacenti (sarà ovviamente già visitato)
            if visitati[int(v.nodo)] == 0:
                padri[int(v.nodo)] = u.nodo
                if dfs_ciclo(g, v, padri, visitati):
                    return True     # abbiamo incontrato un nodo già visitato e stiamo risalendo la ricorsione
            else:
                return True         # caso in cui incontriamo un nodo già visitato
    return False

                

# funzione che dato in input il grafo g, inizializza il grafo n_g con gli stessi nodi
def inizializzaGrafo(n_g, g):
        n_g.n_nodi = g.n_nodi
        n_g.lista_nodi = g.lista_nodi
        n_g.id2Node = g.id2Node
        
        for nodo in n_g.getListaNodi():
            n_g.lista_adiacenza_nodi.setdefault(nodo.nodo, [])
            n_g.lista_adiacenza.setdefault(nodo.nodo, [])


def checkMst(adj_list1, adj_list2):
    for key in adj_list1.keys():
        if not equals(adj_list1[key],adj_list2[key]):
            return False
    return True

def equals(l1, l2):
    l1 = [nodo.nodo for nodo in l1]
    l2 = [nodo.nodo for nodo in l2]
    l1.sort()
    l2.sort()
    if l1 != l2:
        print(l1,l2)
    return l1 == l2


################# Union-Find #################

def makeSet(nodo):
    nodo.padre = nodo.nodo
    nodo.size = 0

#union-by-rank
def link(nodo1, nodo2):
    if nodo1.size > nodo2.size:
        nodo2.padre = nodo1.nodo
    else:
        nodo1.padre = nodo2.nodo
        if nodo1.size == nodo2.size:
            nodo2.size += 1

#union-by-rank
def union2(nodo1, nodo2):
    link(nodo1, nodo2)

#union-by-size
def union(nodo1, nodo2, g):
    radice_nodo1 = findSet(g, nodo1) 
    radice_nodo2 = findSet(g, nodo2)
    r1 = g.getNodo(radice_nodo1)   #ottengo gli oggetti
    r2 = g.getNodo(radice_nodo2)  
    if radice_nodo1 == radice_nodo2:      #se hanno stessa radice, sono già nello stesso insieme
        return
    if r1.size >= r2.size:
        r2.padre = r1.nodo
        r1.size += r2.size
    else:
        r1.padre = r2.nodo
        r2.size += r2.size




def findSet(g, nodo1):
    if nodo1.nodo != nodo1.padre:
        nodo1.padre = findSet(g, g.getNodo(nodo1.padre))
    return nodo1.padre
    