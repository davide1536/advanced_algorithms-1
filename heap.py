#DESCRIZIONE CLASSE E FUNZIONI HEAP:
#La classe heap è costituita da:
    #vettore associato all'heap
    #lunghezza del vettore
    #lunghezza dell'heap (che all'inizio equivale alla lunghezza del vettore)
#Le funzioni disponibili sono:
    #BuildMinHeap(h) --> h = oggetto heap, la funzione dato un oggetto heap h costruisce una minHeap
    #HeapDecreaseKey(h, i, key) --> h = oggetto heap, i=valore indice, key = nuova chiave, dato un oggetto heap h sostituisce il valore del vettore associato
                                                                                            #all'indice i con il nuovo valore key
    #MinHeapInsert(h, key) --> h= heap, key = nuovo valore da aggiungere all'heap, dato un oggetto heap aggiungo un nuovo valore key
    #HeapMinimum(h) --> ottengo il valore minimo dell'heap
    #HeapExtractMin(h) --> recupera il valore minimo dall'heap e eliminalo
class heap:
    def __init__(self, vector):
        self.vector = vector
        self.length = len(vector)
        self.heapsize = self.length

def BuildMinHeap(h):
    for i in range (h.length//2-1, -1, -1):
        print(i)
        MinHeapify(h, i)

def MinHeapify (h, i):
    l = left(i)
    r = right(i)
    minimum = i
    if l <= h.heapsize-1 and h.vector[l] < h.vector[i]:
        minimum = l
    else:
        minimum = i
    if r <= h.heapsize-1 and h.vector[r] < h.vector[minimum]:
        minimum = r
    if minimum != i:
        temp = h.vector[i]
        h.vector[i] = h.vector[minimum]
        h.vector[minimum] = temp
        return MinHeapify(h,minimum)

def HeapDecreasKey(h, i, key):
    if key > h.vector[i]:
        exit("la nuova chiave è più grande di quella corrente")
    h.vector[i] = key
    while i>0 and h.vector[parent(i)] > h.vector[i]:
        temp = h.vector[i]
        h.vector[i] = h.vector[parent(i)]
        h.vector[parent(i)] = temp
        i = parent(i)

def MinHeapInsert(h, key):
    h.heapsize = h.heapsize+1
    h.vector.insert(h.heapsize-1, float('inf')) #il valore più piccolo di tutti
    HeapDecreasKey(h, h.heapsize-1, key)


def HeapMinimum(h):
    return h.vector[0]

def HeapExtractMin(h):
    if h.heapsize < 1:
        print ("underflow dell'heap")
    minimum = h.vector[0]
    h.vector[0] = h.vector[h.heapsize-1]
    h.heapsize = h.heapsize - 1
    MinHeapify(h, 0)
    return minimum

def right(index):
    return 2*index+2

def left(index):
    return 2*index+1

def parent(index):
    return (index-1)//2 



