class Arco:
    def __init__(self, nodo1, nodo2, peso):
        self.nodo1 = nodo1
        self.nodo2 = nodo2
        self.peso = int(peso)

    def getArco(self):
        return [self.nodo1, self.nodo2, self.peso]
    
        