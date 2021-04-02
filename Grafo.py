from Arco import Arco
from Nodo import Nodo
class Grafo:
    def __init__(self, n_nodi, n_archi, lista_nodi, lista_archi, id2Node, lista_adiacenza, lista_adiacenza_nodi):
        self.n_nodi = n_nodi
        self.n_archi = n_archi
        self.lista_nodi = lista_nodi
        self.lista_archi = lista_archi
        self.id2Node = id2Node
        self.lista_adiacenza = lista_adiacenza #dizionario key: nodo, value: lista archi del nodo
        self.lista_adiacenza_nodi = lista_adiacenza_nodi #dizionario key: nodo, value: lista nodi adiacenti
    

    def addNodo(self, nodo, archi):
        self.n_nodi += 1
        self.lista_nodi.add(nodo)
        self.lista_adiacenza.setdefault(nodo, []) #inizializzo il valore del nuovo nodo a lista 
        self.lista_adiacenza_nodi.setdefault(nodo, [])
        for arco in archi:
            self.n_archi += 1
            arco_inverso = Arco(arco.getNodo2(), arco.getNodo1(), arco.getPeso())
            self.lista_archi.append(arco)
            self.lista_archi.append(arco_inverso)
            
            self.lista_adiacenza[arco.getNodo2()].append(arco_inverso) #aggiungo arco inverso al nodo già presente nel grafo
            self.lista_adiacenza[nodo].append(arco) #aggiungo l'arco alla lista di adiacenza del nuovo nodo
            
            self.lista_adiacenza_nodi[arco.getNodo2()].append(nodo) #aggiungo il nuovo nodo alla lista dei vicini del nodo2
            self.lista_adiacenza_nodi[nodo].append(arco.getNodo2()) #agginugno il nodo2 alla lista dei vicini del nuovo nodo
    
    #restituisce l'oggetto noto, dato l'id 
    def getNodo(self, id_nodo):
        return self.id2Node[id_nodo]

    def getListaNodi(self):
        return list(self.id2Node.values())

    def getPadreFiglio(self):
        for nodo in self.id2Node.values():
            print(nodo.padre +" è padre di "+ nodo.nodo)
    