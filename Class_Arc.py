# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:54:07 2019

@author: Théo
"""

class Arc :
    def __init__(self,arret_dep,arret_arr):
        self.arret_dep = arret_dep
        self.arret_arr = arret_arr
        self.temps_aller = []
        self.temps_retour = []
        self.temps_allerV = []
        self.temps_retourV = []
    
    ##setters##
    def setTemps_aller (self,aller):
        self.temps_aller  = aller
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