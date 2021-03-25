from Grafo import Grafo
from Nodo import Nodo
from Arco import Arco
import os


lista_grafi = []

def crea_grafi():

    #per ogni documento
    lista_nodi = []
    lista_archi = []
    lista_adj = {}
    
    f = open("algoritmi-avanzati-laboratorio/mst_dataset/input_random_68_100000.txt", "r")

    #creo il primo grafo di prova
    prima_riga = f.readline().split(" ")
    grafo_1 = Grafo(prima_riga[0], prima_riga[1], lista_nodi, lista_archi, lista_adj)
    


    """ #leggo il file dalla seconda riga
    for line in f:
        print(line)
        
        #riga del file formata da [nodo1, nodo2, peso_arco_1]
        riga = line.split(" ")
        
        #nodi
        lista_temp_nodi.add(riga[0])
        #archi
        lista_archi.append( Arco(riga[0], riga[1], int(riga[2])) )
 """

    #altro modo
    #creo lista di stringhe "nodo1, nodo2, peso"
    righe = f.read().splitlines()
    
    #divido le stringhe in liste di 3 valori [nodo1, nodo2, peso]
    lista_valori = []
    for riga in righe:
        lista_valori.append(riga.split())
    
    
    #nodo temporaneo, serve come riferimento in caso di archi sullo stesso nodo (secondo if)
    nodo_temp = None
    for i in range(0, len(lista_valori)):
        
        if i != 0: #no primo nodo
       
            if lista_valori[i][0] == lista_valori[i-1][0]:      #non ho trovato un nuovo nodo
                arco_temp = Arco(lista_valori[i][0], lista_valori[i][1], int(lista_valori[i][2]))
                
                lista_archi.append(arco_temp)                   #aggiungo arco alla lista archi
                nodo_temp.lista_archi_adj.append(arco_temp)     #aggiungo arco adiacente al nodo
                lista_adj[nodo_temp].append(arco_temp)          #aggiungo arco alla lista di adiacenza del nodo


            else:       #ho trovato un nuovo nodo
                arco_temp = Arco(lista_valori[i][0], lista_valori[i][1], int(lista_valori[i][2]))
                nodo_temp = Nodo(lista_valori[i][0], [arco_temp])
                    
                lista_nodi.append(nodo_temp)  
                lista_archi.append(arco_temp)
                    
                lista_adj.setdefault(nodo_temp, [])     #imposto come chiave il nodo e come valore una lista
                lista_adj[nodo_temp].append(arco_temp)  #aggiungo l'arco alla lista degli archi del nodo chiave
                
        else:           #primo nodo
                arco_temp = Arco(lista_valori[i][0], lista_valori[i][1], int(lista_valori[i][2]))
                nodo_temp = Nodo(lista_valori[i][0], [arco_temp])
                    
                lista_nodi.append(nodo_temp)  
                lista_archi.append(arco_temp)
                    
                lista_adj.setdefault(nodo_temp, [])     #imposto come chiave il nodo e come valore una lista
                lista_adj[nodo_temp].append(arco_temp)  #aggiungo l'arco alla lista degli archi del nodo chiave

        
    ################### test ###################
    #for key, value in grafo_1.lista_adiacenza.items():
        #for i in range(0, len(value)):
            #print("nodo "+ key.nodo + ": (" + value[i].nodo1 +", "+ value[i].nodo2 + ") peso: "+ str(value[i].peso) )
    print("fine")   

crea_grafi()


