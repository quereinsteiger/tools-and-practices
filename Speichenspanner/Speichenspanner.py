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
        F = pi * self.Dichte * (self.Frequenz*self.Durchmesser*self.Länge)**2  # [F] = N
        
        return F
    
    def dDichte(self, dDichte_erwartet = 0):
        vDichte = pi*(self.Frequenz*self.Durchmesser*self.Länge)**2            # [dDichte] = N/(kg/m³) 
        dDichte =vDichte * dDichte_erwartet
        return dDichte
    
    def dFrequenz(self, dFrequenz_erwartet = 5):
        vFrequenz = 2*pi*self.Dichte*self.Frequenz*self.Durchmesser**2*self.Länge**2    # [dFrequenz] = N/Hz
        dFrequenz = vFrequenz * dFrequenz_erwartet
        return dFrequenz
    
    def dDurchmesser(self, dDurchmesser_erwartet = 0.03):
        vDurchmesser = 2*pi*self.Dichte*self.Frequenz**2*self.Durchmesser*self.Länge**2 # [dDurchmesser] = N/m
        dDurchmesser = vDurchmesser * dDurchmesser_erwartet / 1000
        return dDurchmesser
    
    def dLänge(self, dLänge_erwartet = 2):
        vLänge = 2*pi*self.Dichte*self.Frequenz**2*self.Durchmesser**2*self.Länge # [dLänge] = N/m
        dLänge = vLänge * dLänge_erwartet / 1000
        return dLänge
    
if __name__ == "__main__":
    Speiche = Saite(1.8,270)
    print(f"Frequenz (Hz): {Speiche.Frequenz}")
    print(f"Spannkraft (N): {Speiche.Spannkraft()}")
    print(f"dDichte: {Speiche.dDichte()}")
    print(f"dFrequenz: {Speiche.dFrequenz()}")
    print(f"dDurchmesser: {Speiche.dDurchmesser()}")
    print(f"dLänge: {Speiche.dLänge()}")