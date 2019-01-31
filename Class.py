# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:33:54 2019

@author: Théo
"""

class arret :
    def __init__(self,name):
        self.name = name
        self.heure_aller = []
        self.heure_retour = []
        self.heure_allerV = []
        self.heure_retourV = []
        self.liste_lignes =[]  #liste des lignes qui passent par cette arret
        
    ##setters##

    def setHeure_aller(self,heure_aller): #heure--> liste 
        self.heure_aller = heure_aller
    def setHeure_retour(self,heure_retour):
        self.heure_retour = heure_retour
    def setHeure_allerV(self,heure_allerV): #heure--> liste 
        self.heure_allerV = heure_allerV
    def setHeure_retourV(self,heure_retourV):
        self.heure_retourV = heure_retourV
        
    def setLigne (self,num_ligne):
        self.liste_lignes.append(num_ligne)
    
    
    ##getters##
    def getName(self):
        return self.name
    def getLignes(self):
        return self.lignes
    def getHeure_aller(self):
        return self.heure_aller
    def getHeure_retour(self):
        return self.heure_retour
    def getHeure_allerV(self):
        return self.heure_allerV
    def getHeure_retourV(self):
        return self.heure_retourV
    def getLignes (self):
        return self.liste_lignes
        
class arc :
    def __init__(self,arret_dep,arret_arr):
        self.arret_dep = arret_dep
        self.arret_arr = arret_arr
        self.temps_aller = []
        self.temps_retour = []
        self.temps_allerV = []
        self.temps_retourV = []
    
    ##setters##
    def setTemps_aller (self,aller):
        self.temps_aller = aller
    def setTemps_retour (self,retour):
        self.temps_retour = retour
    def setTemps_allerV (self,allerV):
        self.temps_allerV = allerV
    def setTemps_retourV (self,retourV):
        self.temps_retourV = retourV
        
    ##getters##
    def getArret_dep (self):
        return self.arret_dep
    def getArret_arr (self):
        return self.arret_arr
    
    
    def getTemps_aller(self):
        return self.temps_aller
    def getTemps_retour(self) :
        return self.temps_retour
    def getTemps_allerV(self):
        return self.temps_allerV
    def getTemps_retourV(self):
        return self.temps_retourV
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    