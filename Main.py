# -*- coding: utf-8 -*-
"""
Created on Tues Jan 22 10:29:20 2019

@author: Théo
"""

###Setup & import###
from Exploitation_fichier import Exploitation_fichier as EF


###Creation des arcs et des arrets###
liste_arc1,liste_arret1 = EF.Arc_Arret('1_Poisy-ParcDesGlaisins.txt',1)
liste_arc2,liste_arret2 = EF.Arc_Arret('2_Piscine-Patinoire_Campus.txt',2)


###Creation de liste de lignes###
liste_ligne =[[liste_arret1,liste_arc1],[liste_arret2,liste_arc2]] #l'indice de la liste corespond au numéro de la ligne -1


    
###Creation du graph###
#On transforme les temps en réels car ils ne sont qu'en minutes   
graph = EF.graph(liste_ligne)

###Execution des programmes###
print("")
gf = graph.fastest("Vernod", "Ponchy")
print(EF.presentation(gf, liste_ligne))
print("")
gs = graph.shortest("Vernod", "Pommaries")
print(EF.presentation(gs, liste_ligne))

print("")






###Graph pour tester les algos facilement###

#from Class_Graph import Graph
#graph_EZ = Graph([
#    ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
#    ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
#    ("e", "f", 9),("b", "g", 20),("d", "g", 1)])
#
#
#print("")
#print(graph_EZ.fastest("a", "f"))
#print(graph_EZ.shortest("a", "f"))



