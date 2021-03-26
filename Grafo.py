class Grafo:
    def __init__(self, n_nodi, n_archi, lista_nodi, lista_archi, lista_adiacenza, lista_adiacenza_nodi):
        self.n_nodi = n_nodi
        self.n_archi = n_archi
        self.lista_nodi = lista_nodi
        self.lista_archi = lista_archi
        self.lista_adiacenza = lista_adiacenza #dizionario key: nodo, value: lista archi del nodo
        self.lista_adiacenza_nodi = lista_adiacenza_nodi #dizionario key: nodo, value: lista nodi adiacenti