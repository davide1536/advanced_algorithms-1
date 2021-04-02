import math
class Nodo:
    def __init__(self, nodo, padre = None, rank = 0, key = 0, in_h = 1):
        self.nodo = nodo
        self.padre = padre
        self.rank = rank
        self.key = key
        self.in_h = in_h    # = 1 perchè tutti i nodi sono nell'heap (prim)
    
