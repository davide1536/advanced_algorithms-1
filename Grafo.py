from Arco import Arco
from Nodo import Nodo
class Grafo:
    def __init__(self, n_nodi = 0, n_archi = 0, lista_nodi = set(), lista_archi = [], id2Node = {}, lista_adiacenza = {}, lista_adiacenza_nodi = {}):
        self.n_nodi = n_nodi
        self.n_archi = n_archi
        self.lista_nodi = lista_nodi
        self.lista_archi = lista_archi
        self.id2Node = id2Node
        self.lista_adiacenza = lista_adiacenza #dizionario key: nodo (str), value: lista archi del nodo (obj arco)
        self.lista_adiacenza_nodi = lista_adiacenza_nodi #dizionario key: nodo (str), value: lista nodi adiacenti (obj nodo)
    

    def aggiungiNodo(self, nodo):
        obj_nodo = Nodo(nodo)
        self.id2Node[obj_nodo.nodo] = obj_nodo
        self.n_nodi += 1
        self.lista_nodi.add(nodo)
        self.lista_adiacenza.setdefault(nodo, []) #inizializzo il valore del nuovo nodo a lista 
        self.lista_adiacenza_nodi.setdefault(nodo, [])
    
    def aggiungiNodi(self, nodi):
        for nodo in nodi:
            obj_nodo = Nodo(nodo)
            self.id2Node[obj_nodo.nodo] = obj_nodo
            self.n_nodi += 1
            self.lista_nodi.add(nodo)
            self.lista_adiacenza.setdefault(nodo, []) #inizializzo il valore del nuovo nodo a lista 
            self.lista_adiacenza_nodi.setdefault(nodo, [])
       
    
    def aggiungiArco(self, arco):
        self.n_archi += 1
        arco_inverso = Arco(arco.nodo2, arco.nodo1, arco.peso)
        self.lista_archi.append(arco)
        self.lista_archi.append(arco_inverso)
        
        self.lista_adiacenza[arco.nodo2].append(arco_inverso) #aggiungo arco inverso al nodo già presente nel grafo
        self.lista_adiacenza[arco.nodo1].append(arco) 
        
        self.lista_adiacenza_nodi[arco.nodo2].append(self.getNodo(arco.nodo1)) #aggiungo il nuovo nodo alla lista dei vicini del nodo2
        self.lista_adiacenza_nodi[arco.nodo1].append(self.getNodo(arco.nodo2)) #agginugno il nodo2 alla lista dei vicini del nuovo nodo

    
    #restituisce l'oggetto noto, dato l'id 
    def getNodo(self, id_nodo):
        return self.id2Node[id_nodo]

    #restituisce la lista di oggetti nodi di un grafo
    def getListaNodi(self):
        return list(self.id2Node.values())

    #mostra vettore dei padri
    def getPadreFiglio(self):
        for nodo in self.id2Node.values():
            print(nodo.padre + " è padre di " + nodo.nodo)
    

    def printAdj(self):
        for i in self.lista_adiacenza_nodi.keys():
            print(i, [ (arco.getArco()[1], arco.getArco()[2]) for arco in self.lista_adiacenza[i]])
       
    