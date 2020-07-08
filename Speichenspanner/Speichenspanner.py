# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:20:06 2020

@author: T.Schulz
"""
from numpy import pi

class Saite():
    def __init__(self,  
                 Durchmesser,       # mm
                 Länge,             # mm
                 Material = 1,      # {1 : "Stahl", 2 : "Alu", 3 : "Carbon"}
                 Frequenz = 500):    # Hz
        self.Durchmesser = Durchmesser / 1000
        self.Länge = Länge / 1000
        dictMaterial = {1 : "Stahl", 2 : "Alu", 3 : "Carbon"}
        self.Material = dictMaterial[Material]
        self.Frequenz = Frequenz
        dictDichte = {"Stahl" : 7.86, "Alu" : 2.7, "Carbon" : 2.0 } #g/cm³
        self.Dichte = dictDichte[self.Material]*1000                #kg/m³
        
    def Spannkraft(self):
        F = pi * self.Dichte * (self.Frequenz*self.Durchmesser*self.Länge)**2
        return F
    
    def dDichte(self):
        dDichte = pi*(self.Frequenz*self.Durchmesser*self.Länge)**2
        return dDichte
    
    def dFrequenz(self):
        dFrequenz = 2*pi*self.Dichte*self.Frequenz*self.Durchmesser**2*self.Länge**2
        return dFrequenz
    
    def dDurchmesser(self):
        dDurchmesser = 2*pi*self.Dichte*self.Frequenz**2*self.Durchmesser*self.Länge**2
        return dDurchmesser
    
    def dLänge(self):
        dLänge = 2*pi*self.Dichte*self.Frequenz**2*self.Durchmesser**2*self.Länge
        return dLänge
    
if __name__ == "__main__":
    Speiche = Saite(1.8,270)
    print(f"Frequenz (Hz): {Speiche.Frequenz}")
    print(f"Spannkraft (N): {Speiche.Spannkraft()}")
    print(f"dDichte: {Speiche.dDichte()}")
    print(f"dFrequenz: {Speiche.dFrequenz()}")
    print(f"dDurchmesser: {Speiche.dDurchmesser()}")
    print(f"dLänge: {Speiche.dLänge()}")