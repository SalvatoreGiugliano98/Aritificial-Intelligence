#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 13:15:38 2021

@author: salvatoregiugliano
"""

import math
import optimization as op
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def function(x):
    if x < 5.2:
        return 10
    elif x >=5.2 and x<= 20:
        return x*x
    elif x > 20:
        return math.cos(x) + 160*x
    return 0

def costf(x):

    return function(x[0])

def hist(x):
    res = []
    
    x = np.reshape(x,(x.shape[0]*x.shape[1]))
    x = sorted(x)
    res.append([x[0],1])
    i = 0
    while len(x) != 1:
        if x[0] == x[1]:
            res[i][1] += 1
            x = np.delete(x,0)
        else:
            res.append([x[1],1])
            x = np.delete(x,0)
            i += 1
    return res


plt.close('all')

domain = [(-100,100)]

f = []
for i in range(-1000,1001):
    f.append([i/10, function(i/10)])

df = pd.DataFrame(f,columns=('x','y'))
plt.plot(df['x'],df['y'],marker='',color='blue')


nRow = 12
exe = pow(nRow,2)

resultAnnealling = np.zeros((nRow,nRow))
resultHillclimb = np.zeros((nRow,nRow))
for i in range(0,nRow-1):
    for j in range(0,nRow-1):
        resultAnnealling[i,j] = op.annealingoptimize(domain,costf)[0]
        resultHillclimb[i,j] = op.hillclimb(domain,costf)[0]
        
plt.figure();

h = hist(resultAnnealling)

h = pd.DataFrame(h, columns=('x','y'))

x_pos = np.arange(len(h))
plt.bar(x_pos, h['y'], align='center')
plt.xticks(x_pos, h['x'])
plt.ylabel('Numero Occorrenze')
plt.xlabel('Valori')
plt.title('Risultati con Annelling')
plt.grid(axis='y')
plt.show()

h = hist(resultHillclimb)

h = pd.DataFrame(h, columns=('x','y'))

x_pos = np.arange(len(h))
plt.figure()
plt.bar(x_pos, h['y'], align='center')
plt.xticks(x_pos, h['x'],size=5)
plt.ylabel('Numero Occorrenze')
plt.xlabel('Valori')
plt.title('Rislultati con Hill Climb')
plt.grid(axis='y')
plt.show()


resultAnnealling = np.reshape(resultAnnealling,(1,(resultAnnealling.shape[0]*resultAnnealling.shape[1])))
hillclimb = np.reshape(resultHillclimb,(1,(resultHillclimb.shape[0]*resultHillclimb.shape[1])))