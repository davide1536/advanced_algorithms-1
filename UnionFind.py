#classe utile per la Union-Find
#capitolo 21.3/4 del libro
################# non testato #################
from Nodo import Nodo

class UnionFind:
    def makeSet(self, nodo):
        nodo.padre = nodo
        nodo.rank = 0
    
    def link(self, nodo1, nodo2):
        if nodo1.rank > nodo2.rank:
            nodo2.padre = nodo1
        else:
            nodo1.padre = nodo2
            if nodo1.rank == nodo2.rank:
                nodo2.rank += 1
    
    def union(self, nodo1, nodo2):
        self.link(nodo1, nodo2)

    def findSet(self, nodo1):
        if nodo1 != nodo1.padre:
            nodo1.padre = self.findSet(nodo1.padre)
        return nodo1.padre

    