#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 22:16:46 2019

@author: antonio
"""

#rubrica = {"Giorgio Bianchi": [["casa", "0815606060"], ["ufficio", "081435234"], ["cell", "3477689560"]],
#           "Marco Rossi": [["casa", "0815657734"], ["cell", "3389012367"]]}

rubrica = dict()

def ricerca(nominativo):
    return rubrica[nominativo] if nominativo in rubrica else "Nominativo non presente"


def ricerca_cell(nominativo):
    if nominativo in rubrica:
        trovato = False
        i = 0
        
        while i < len(rubrica[nominativo]) and not trovato:
            elem = rubrica[nominativo][i]

            if elem[0] == "cell":
                trovato = True
            else:
                 i +=1
            
        if trovato:
            return rubrica[nominativo][i][1]
        else:
            return "Cellulare non trovato"
    else:
        return "Nominativo non trovato"


def modifica_cell(nominativo, cell):
    if nominativo in rubrica:
        trovato = False
        i = 0
        
        while i < len(rubrica[nominativo]) and not trovato:
            elem = rubrica[nominativo][i]

            if elem[0] == "cell":
                trovato = True
            else:
                 i +=1
            
        if trovato:
            rubrica[nominativo][i][1] = cell
        else:
            print("Cellulare non trovato")
    else:
        print("Nominativo non trovato")

def nuovo_contatto(nominativo,casa,ufficio,cellulare):
    riferimenti = list()
    
    if casa != "":
        riferimenti.append(["casa", casa])

    if ufficio != "":
        riferimenti.append(["ufficio", ufficio])

    if cellulare != "":
        riferimenti.append(["cell", cellulare])
        
    rubrica[nominativo] = riferimenti
    

nuovo_contatto("Giulio Verdi","0815606060","0815606060","3389567678")
print(rubrica)
print(ricerca_cell("Giulio Verdi"))

print("Fine")