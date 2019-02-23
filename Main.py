# -*- coding: utf-8 -*-
"""
Created on Tues Jan 22 10:29:20 2019

@author: Théo
"""

import os
from Class import arret,arc
from datetime import datetime as time


def Creation (FileName,Num_Ligne) :
    os.chdir("C:\\Users\\Théo\\Documents\\Cours\\S6\\PROJ631 - Projet algorithmique\\data")
    with open(FileName,"r") as f:
        type_ligne =0
        retour = 0
        holiday = False
        liste_arret=[]
        liste_arc=[]
                    
    
        for ligne in f:
            
            """
            on va determiner si la liste est une liste d'arret 
            ou les horaires d'un arret
            initialement c'est une liste d'arret
            type_ligne = [0,1,2,3,4] = [liste arret,arret aller, arret retour, arret allerV, arret retourV]
            
            """
            
            if type_ligne == 0 and ligne == '\n' and holiday == False:
                type_ligne = 1
                indice_arret = 0
    
            elif type_ligne == 1 and ligne == '\n' and holiday == False: 
                retour = 1
                type_ligne = 2
                holiday = True
                indice_arret = len(liste_arret)-1
    
            elif type_ligne == 2 and ligne == '\n' and holiday == True:
                type_ligne = 0
                retour = 0
    
            elif type_ligne == 0 and ligne == '\n' and holiday == True:
                type_ligne = 3
                indice_arret = 0
                retour = 1
    
            elif type_ligne == 3 and ligne == '\n' and retour == 1:
                type_ligne = 4
                indice_arret = len(liste_arret)-1
                retour = 0
                holiday = False
                
                
                
            """
            on va maintenant traiter la ligne selon son type
            """
            
            if type_ligne == 0 and holiday== False :#c'est une liste d'arrets, mais on ne traite pas en holiday car c'est la meme chose
                for str_nom_arret in ligne.split(" N "):
                    nom_arret = arret(str_nom_arret)
                    liste_arret.append(nom_arret)
                    
                    
                liste_arret[0].setLigne(1)
                for i in range (len(liste_arret)-1):
                    liste_arc.append(arc(liste_arret[i].getName(),liste_arret[i+1].getName()))
                    liste_arret[i+1].setLigne(Num_Ligne)
                
                
            
            liste=[]
            if type_ligne == 1 :
                if ligne == '\n':
                    pass
                else :
                    first_elt = 0
                    for horaire in ligne.split(" "):
                        if first_elt == 0 :
                            first_elt = 1
                        else:
                            liste.append(horaire)
                    liste_arret[indice_arret].setHeure_aller(liste)
                    indice_arret +=1
    
            liste=[]
            if type_ligne == 2 :
                if ligne == '\n':
                    pass
                else :
                    first_elt = 0
                    for horaire in ligne.split(" "):
                        if first_elt == 0 :
                            first_elt = 1
                        else:
                            liste.append(horaire)
                    liste_arret[indice_arret].setHeure_retour(liste)
    #                print(liste_arret[indice_arret].getName())
    #                print(liste_arret[indice_arret].getHeure_retour())
                    indice_arret -=1        
          
            liste=[]
            if type_ligne == 3 :
                if ligne == '\n':
                    pass
                else :
                    first_elt = 0
                    for horaire in ligne.split(" "):
                        if first_elt == 0 :
                            first_elt = 1
                        else:
                            liste.append(horaire)
                    liste_arret[indice_arret].setHeure_allerV(liste)
    #                print(liste_arret[indice_arret].getName())
    #                print(liste_arret[indice_arret].getHeure_allerV())
                    indice_arret +=1       
            
            liste=[]
            if type_ligne == 4 :
                if ligne == '\n':
                    pass
                else :
                    first_elt = 0
                    for horaire in ligne.split(" "):
                        if first_elt == 0 :
                            first_elt = 1
                        else:
                            liste.append(horaire)
                    liste_arret[indice_arret].setHeure_retourV(liste)
    #                print(liste_arret[indice_arret].getName())
    #                print(liste_arret[indice_arret].getHeure_retourV())
                    indice_arret -=1         
    
    
    '''
    Maintenant qu'on a traité tout les horaires des arrets il faut mettre une duree a chaque arc
    '''
    ###On calcule toute les durées de l'aller
    for i in range(len(liste_arret)-1):
        liste_horaire1 = liste_arret[i].getHeure_aller()
        liste_horaire2 = liste_arret[i+1].getHeure_aller()
        liste_duree = []
        for j in range (len(liste_horaire1)):
            if liste_horaire1[j] == '-' or liste_horaire2[j] == '-' or '\n' in liste_horaire1[j] or '\n' in liste_horaire2[j]:
                liste_duree.append('-')
            else:
                temps1 = time.strptime(liste_horaire1[j],'%H:%M')
                temps2 = time.strptime(liste_horaire2[j],'%H:%M')
                duree = temps2- temps1
                liste_duree.append(str(duree))
        liste_arc[i].setTemps_aller(liste_duree)
        
    ###On calcule toute les durées du retour    
    for i in range(len(liste_arret)-1):
        liste_horaire2 = liste_arret[i].getHeure_retour()
        liste_horaire1 = liste_arret[i+1].getHeure_retour()
        liste_duree = []
        for j in range (len(liste_horaire1)):
            if liste_horaire1[j] == '-' or liste_horaire2[j] == '-' or '\n' in liste_horaire1[j] or '\n' in liste_horaire2[j]:
                liste_duree.append('-')
            else:
                temps1 = time.strptime(liste_horaire1[j],'%H:%M')
                temps2 = time.strptime(liste_horaire2[j],'%H:%M')
                duree = temps2- temps1
                liste_duree.append(str(duree))
        liste_arc[i].setTemps_retour(liste_duree)
        
    ###On calcule toute les durées de l'aller en preriode de vacances
    for i in range(len(liste_arret)-1):
        liste_horaire1 = liste_arret[i].getHeure_allerV()
        liste_horaire2 = liste_arret[i+1].getHeure_allerV()
        liste_duree = []
        for j in range (len(liste_horaire1)):
            if liste_horaire1[j] == '-' or liste_horaire2[j] == '-' or '\n' in liste_horaire1[j] or '\n' in liste_horaire2[j]:
                liste_duree.append('-')
            else:
                temps1 = time.strptime(liste_horaire1[j],'%H:%M')
                temps2 = time.strptime(liste_horaire2[j],'%H:%M')
                duree = temps2- temps1
                liste_duree.append(str(duree))
        liste_arc[i].setTemps_allerV(liste_duree)
        
    ###On calcule toute les durées du retour en période de vacances    
    for i in range(len(liste_arret)-1):
        liste_horaire2 = liste_arret[i].getHeure_retourV()
        liste_horaire1 = liste_arret[i+1].getHeure_retourV()
        liste_duree = []
        for j in range (len(liste_horaire1)):
            if liste_horaire1[j] == '-' or liste_horaire2[j] == '-' or '\n' in liste_horaire1[j] or '\n' in liste_horaire2[j]:
                liste_duree.append('-')
            else:
                temps1 = time.strptime(liste_horaire1[j],'%H:%M')
                temps2 = time.strptime(liste_horaire2[j],'%H:%M')
                duree = temps2- temps1
                liste_duree.append(str(duree))
        liste_arc[i].setTemps_retourV(liste_duree)
        
        
        
        
    return liste_arc , liste_arret


liste_arc1,liste_arret1 = Creation('1_Poisy-ParcDesGlaisinsModifie.txt',1)
liste_arc2,liste_arret2 = Creation('2_Piscine-Patinoire_Campus.txt',2)



###Ajout des lignes sur chaque arret###    
for arret1 in liste_arret1:
    for arret2 in liste_arret2:
        if arret1.getName() == arret2.getName():
            arret1.setLigne(2)
            arret2.setLigne(1)

###Création de liste de lignes###
liste_ligne =[[],[liste_arret1,liste_arc1],[liste_arret2,liste_arret2]]
#l'indice de la liste corespond au numéro de la ligne car i=0 =  []






#def parcours (liste_arret,arret_dep,arret_arrive):
#    #on va chercher l indice de l arret de depart avant de commencer la partie rec
#    i=0
#    sens_retour =0
#    while arret_dep != liste_arret[i].getName():
#        i+=1
#        if liste_arret[i].getName() == arret_arrive:
#            sens_retour = 1
#    def partie_rec (liste_arret,i):
#        if liste_arret1[i].getName() == arret_arrive :
#            return 'TROUVE !!!'
#        else:
#            if sens_retour == 0:
#                i+=1
#                return partie_rec (liste_arret,i)
#                
#            elif sens_retour == 1:
#                i-=1
#                return partie_rec (liste_arret,i)
#    return partie_rec(liste_arret1,i)
 


   
def parcours2 (arret_dep, arret_arrive, numLigne_dep, liste_ligne):
    liste_arret,liste_arc = liste_ligne[numLigne_dep]
    i=0
    sens_retour =0
    while arret_dep != liste_arret[i].getName():
        i+=1
        if liste_arret[i].getName() == arret_arrive:
            sens_retour = 1
    def partie_rec2 (arret_dep,arret_arrive,i):
        if liste_arc[i].getArret_arr() == arret_arrive:
            return 'TRRRRRRRROUVEEEEEEEEE'
        else:
            if sens_retour == 0:
                return partie_rec2 (liste_arc[i].getArret_arr(),arret_arrive,i+1)
                
            elif sens_retour == 1:
                return partie_rec2 (liste_arc[i].getArret_arr(),arret_arrive,i-1)
    return partie_rec2 (arret_dep,arret_arrive,i)






#print(parcours(liste_arret1,'Vernod','Ponchy'))
    
print(parcours2('Vernod','Ponchy',1,liste_ligne)) 
    
    
    
    
    
    
    
    
    
    
                
                
                
    
