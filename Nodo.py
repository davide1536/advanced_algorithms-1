import math
class Nodo:
    def __init__(self, nodo, padre = None, rank = 0, key = 0):
        self.nodo = nodo
        self.padre = padre
        self.rank = rank
        self.key = key
    
