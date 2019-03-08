# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:53:14 2019

@author: Théo
"""

class Arret :
    def __init__(self,name,splited = False):
        self.name = name
        self.splited = splited
        self.heure_aller = []
        self.heure_retour = []
        self.heure_allerV = []
        self.heure_retourV = []
        
    ##Setters##

    def setHeure_aller(self,heure_aller): #heure--> liste 
        self.heure_aller = heure_aller
    def setHeure_retour(self,heure_retour):
        self.heure_retour = heure_retour
    def setHeure_allerV(self,heure_allerV): #heure--> liste 
        self.heure_allerV = heure_allerV
    def setHeure_retourV(self,heure_retourV):
        self.heure_retourV = heure_retourV
        
    
    ##Getters##
    def getName(self):
        return self.name
    def getHeure_aller(self):
        return self.heure_aller
    def getHeure_retour(self):
        return self.heure_retour
    def getHeure_allerV(self):
        return self.heure_allerV
    def getHeure_retourV(self):
        return self.heure_retourV
