#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:14:03 2021

@author: salvatoregiugliano
"""

import numpy as np
import matplotlib.pyplot as plt
from termcolor import colored

coloriValidi = ['blue','red','green','yellow']
class Popolo:
    def __init__(self, province, score = 0):
        self.province = province
        self.score = score
    def getProvince(self):
        return self.province
    def setprovince(self,newprovince):
        self.province = newprovince
    def printMappa(self):
        print('La Mappa della regione deve essere colorata in questo modo:' )
        for key in self.province:
            print('Provincia di ', 
                  colored(self.province[key].nome,attrs=['dark','underline','bold']), 
                  ' => colore :', 
                  colored(coloriValidi[self.province[key].coloreAssegnato],
                          coloriValidi[self.province[key].coloreAssegnato]))
    def updateScore(self):
        self.score = setScore(self.province)
            

class Provincia:
    def __init__(self, nome, coloreAssegnato = None ,coloreValidi = np.arange(0,len(coloriValidi)-1) ):
        self.nome = nome
        self.coloreAssegnato = coloreAssegnato
        self.coloreValidi = coloreValidi
    def setColoreValidi(self,newColoreValidi):
        self.coloreValidi = newColoreValidi
    def setColoreAssegnato(self,coloreAssegnato):
        self.coloreAssegnato = coloreAssegnato
        

cromosoma = {"NA":0,"CE":0,"BN":0,"SA":0,"AV":0}
province = {'NA' : Provincia('NA'), 'CE' : Provincia('CE'),'BN': Provincia('BN'),'AV': Provincia('AV'),'SA':Provincia('SA')}

scorePop = []
scoreSol = 5

numeroPopolazioneCasuale = 4

def creaProvince():
    newProvince = dict.copy(province)
    for key in list(province.keys()):
        #newProvince[key] = (Provincia(key,np.random.randint(0,len(coloriValidi))))
        newProvince[key] = (Provincia(key,0)) #Da usare per controllare l'agloritmo genetico
    return newProvince

def setScore(provincia):
    score = 1
    if (provincia.get("CE").coloreAssegnato != provincia.get("NA").coloreAssegnato and 
        (provincia.get("CE").coloreAssegnato != provincia.get("BN").coloreAssegnato)):
        score +=1
    if ((provincia.get("BN").coloreAssegnato!= provincia.get("NA").coloreAssegnato) and
        (provincia.get("CE").coloreAssegnato != provincia.get("BN").coloreAssegnato) and
        (provincia.get("BN").coloreAssegnato) != provincia.get("AV").coloreAssegnato):
        score +=1
    if ((provincia.get("AV").coloreAssegnato != provincia.get("NA").coloreAssegnato)and 
        (provincia.get("AV").coloreAssegnato!=provincia.get("BN").coloreAssegnato) and 
        (provincia.get("AV").coloreAssegnato != provincia.get("SA").coloreAssegnato)):
        score +=1
    if ((provincia.get("SA").coloreAssegnato != provincia.get("NA").coloreAssegnato) and 
        (provincia.get("AV").coloreAssegnato != provincia.get("SA").coloreAssegnato)):
        score +=1
    return score


def generaPopolazioneCasuale():
    popolazione = []
    for i in range(numeroPopolazioneCasuale):
        prov = creaProvince()
        score = setScore(prov)
        scorePop.append(score)
        pop = Popolo(prov,score)
        popolazione.append(pop)
    return popolazione

def checkVincoli(popolazione):
    for mappa in popolazione:
        if (mappa.score == 5): 
            return True
    return False

def getMaxScore(popolazione):
    maxScore = max(scorePop)
    return maxScore

def getParents(popolazione):
    score = getMaxScore(popolazione)
    if (score < 4):
        return parentSelection1(popolazione)
    else:
        return parentSelection2(popolazione)

def parentSelection1(popolazione):
    result = []
    popol = list.copy(popolazione)
    scorePop1 = list.copy(scorePop)
    index = np.random.randint(0,len(popol))
    temp1 = popol[index]
    score1 = scorePop1[index]
    popol.pop(index)
    scorePop1.pop(index)
    index = np.random.randint(0,len(popol))
    temp2 = popol[index]
    score2 = scorePop1[index]
    popol.pop(index)
    scorePop1.pop(index)
    
    if (score1 < score2):
        result.append(temp2)
    else:
        result.append(temp1)
        
    index = np.random.randint(0,len(popol))
    temp1 = popol[index]
    score1 = scorePop1[index]
    popol.pop(index)
    scorePop1.pop(index)
    
    index = np.random.randint(0,len(popol))
    temp2 = popol[index]
    score2 = scorePop1[index]
    popol.pop(index)
    scorePop1.pop(index)
    if (score1 < score2):
        result.append(temp2)
    else:
        result.append(temp1)
        
    return result

def parentSelection2(popolazione):
    result = []
    popol = list.copy(popolazione)
    scorePop1 = list.copy(scorePop)
    index = scorePop1.index(max(scorePop1))
    result.append(popol[index])
    popol.pop(index)
    scorePop1.pop(index)
    index = scorePop1.index(max(scorePop1))
    result.append(popol[index])
    return result
    
def crossover(parents):
    child = dict.copy(parents[0].getProvince())
    childKey = list(child.keys())
    index = np.random.randint(0,len(childKey))
    for i in range(index,len(childKey)):
        key = childKey[i]
        value = parents[1].getProvince()[key].coloreAssegnato
        child[key].coloreAssegnato = value
    child = Popolo(child,setScore(child))
    scorePop.append(child.score)
    return child

def mutate(child):
    score = getMaxScore(child)
    if (score < 4):
        return mutate1(child)
    else:
        return mutate2(child)
    return child

def getAdiacente(key):
    adiacenti = []
    if key == list(province.keys())[0]: #NA
        adiacenti.append('CE')
        adiacenti.append('AV')
        adiacenti.append('BN')
        adiacenti.append('SA')
    elif key == list(province.keys())[1]: #CE
        adiacenti.append('NA')
        adiacenti.append('BN')
    elif key == list(province.keys())[2]: #BN
        adiacenti.append('AV')
        adiacenti.append('NA')
        adiacenti.append('CE')
    elif key == list(province.keys())[3]: #SA
        adiacenti.append('AV')
        adiacenti.append('NA')
    elif key == list(province.keys())[4]: #AV
        adiacenti.append('SA')
        adiacenti.append('NA')
        adiacenti.append('BN')
    return adiacenti

def mutate1(child):
    for element in child.getProvince():
        coloriAdiacenti = []
        test = child.getProvince()[element].coloreAssegnato
        for adiacenti in getAdiacente(element):
            test1 = child.getProvince()[adiacenti].coloreAssegnato
            if test == test1:
                i = coloriValidi[test]
                coloriAdiacenti.append(i)
        colValidi = child.getProvince()[element].coloreValidi
        colValidi = [item for item in colValidi if item not in coloriAdiacenti]
        child.getProvince()[element].setColoreValidi(colValidi)
        if coloriAdiacenti :
            newColor = np.random.randint(0,len(colValidi))
            child.getProvince()[element].coloreAssegnato = newColor
    child.updateScore()
    scorePop[len(scorePop)-1] = child.score
    return child

def mutate2(child):
    for element in child.getProvince():
        test = child.getProvince()[element].coloreAssegnato
        for adiacenti in getAdiacente(element):
            test1 = child.getProvince()[adiacenti].coloreAssegnato
            if test == test1:
                newColor = np.random.randint(0,len(coloriValidi))
                child.getProvince()[element].coloreAssegnato = newColor
    child.updateScore()
    scorePop[len(scorePop)-1] = child.score
    return child


def gaRun():
        parents = getParents(popolazione)
        child = crossover(parents)
        child = mutate(child)
        popolazione.append(child)


plt.close('all')        

popolazione = generaPopolazioneCasuale()
terminato = checkVincoli(popolazione)
if terminato == True:
    index = 0
    for pop in popolazione:
        if (pop.score == scoreSol):
            pop.printMappa()
else:
    numExec = 0
    while(terminato == False and numExec < 50):
        gaRun()
        numExec += 1
        terminato = checkVincoli(popolazione)
    popolazione[len(popolazione)-1].printMappa()


