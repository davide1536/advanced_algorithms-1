from Grafo import Grafo
from Nodo import Nodo
from Arco import Arco
import os


directory = "algoritmi-avanzati-laboratorio/mst_dataset"
lista_grafi = []


#controllo nodi
def check_nodi(lista_grafi):
    for grafo in lista_grafi:
        nodi = len(grafo.lista_nodi) == int(grafo.n_nodi)
    return nodi


def check_generale():
    print("numero grafi = " + str(len(lista_grafi)))
    print("i nodi corrispondono in ogni grafo? " + str(check_nodi(lista_grafi)))


def parsing():
    global directory
    for file in os.listdir(directory):
        #if file == "input_random_01_10.txt":
            #print(file)
        crea_grafi(file)


#funzione di servizio per fornire arco come lista di 3 valori
#  [nodo1, nodo2, peso]
def getArco(arco):
    return [arco.nod1, arco.nodo2, arco.peso]


def crea_grafi(path):

    global lista_grafi
    lista_nodi = set()
    lista_archi = []
    lista_adiacenza = {}
    
    f = open("algoritmi-avanzati-laboratorio/mst_dataset/" + path, "r")

    #creo il primo grafo di prova
    prima_riga = f.readline().split(" ")
    n_nodi = prima_riga[0] 
    n_archi = prima_riga[1]
    
    #creo lista di stringhe "nodo1, nodo2, peso"
    righe = f.read().splitlines()
    
    #divido le stringhe in liste di 3 valori [nodo1, nodo2, peso]
    lista_valori = []
    for riga in righe:
        lista_valori.append(riga.split())
    f.close()
        


    #creo i set di nodi
    for i in range(0, len(lista_valori)):
        nodo_1 = lista_valori[i][0]
        nodo_2 = lista_valori[i][1]
        peso = lista_valori[i][2]
        arco_1 = Arco(nodo_1, nodo_2, peso)
        arco_2 = Arco(nodo_2, nodo_1, peso)
        
        lista_nodi.add(nodo_1)
        lista_nodi.add(nodo_2)
        lista_adiacenza.setdefault(nodo_1, [])    #inzializzo ogni chiave nodo a un valore list
        lista_adiacenza.setdefault(nodo_2, [])    #inzializzo ogni chiave nodo a un valore list

        #forse non serve una lista archi
        lista_archi.append(arco_1)
        lista_archi.append(arco_2)
    
    #for nodo in lista_nodi:
        #se serve un oggetto nodo, crearlo qui!!!!
        #obj_nodo = Nodo(nodo, altri_attributi)
        #lista_adiacenza.setdefault(nodo, [])    #inzializzo ogni chiave nodo a un valore list


    for i in range(0, len(lista_valori)):
        lista_adiacenza[lista_valori[i][0]].append(Arco(lista_valori[i][0], lista_valori[i][1], lista_valori[i][2]))      #arco(u,v)
        lista_adiacenza[lista_valori[i][1]].append(Arco(lista_valori[i][1], lista_valori[i][0], lista_valori[i][2]))      #arco(v,u)

    lista_grafi.append(Grafo(n_nodi, n_archi, lista_nodi, lista_archi, lista_adiacenza))




parsing()
check_generale()



