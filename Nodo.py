import math
class Nodo:
    def __init__(self, nodo, padre = None, rank = 0, key = 0, in_h = 1, vis = 0):
        self.nodo = nodo
        self.padre = padre  # padre del nodo (str)
        self.rank = rank    # utile per union-find
        self.key = key      
        self.in_h = in_h    # = 1 perchè tutti i nodi sono nell'heap (prim)
        self.vis = vis      # attributo visitato (dfs)
    
