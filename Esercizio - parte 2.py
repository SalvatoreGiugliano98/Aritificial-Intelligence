#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:04:28 2021

@author: salvatoregiugliano
"""
import treepredict
import numpy as np
import  re # usato per dividere le rige del file in un array multidimensionale 

f2 = open('abalone.data',"r")

l1=[]
    
for line in f2:
    line = line.rstrip("\n")
    df = re.split(',', line)
    l1.append(df)
    
trainingSet = 10/100 #10%
l2=[]

testData = np.copy(l1)

for i in range(0,int(len(l1)*trainingSet)):
    l2.append(l1[0])
    l1.pop(0)


tree = treepredict.buildtree(l2)
treepredict.drawtree(tree,jpeg = 'EX 1 - Punto 2.jpeg')

res = []
trueRes = 0
falseRes = 0

for i in range(0,int(len(testData))-1):
    if i < len(l1):
        l1[i] = testData[i]
    else:
        l1.append(testData[i])
        
l1 = np.delete(l1, 8, 1)



for i in range(0,len(l1)-1):
    x = treepredict.mdclassify(l1[i], tree)
    an_array = np.array(list(x.items()))
    if testData[i][8] == an_array[0][0]:
        res.append([True,i,str(an_array[0][0]),str(testData[i][8])])
        trueRes = trueRes + 1
    else:
        res.append([False,i,str(an_array[0][0]),str(testData[i][8])])
        falseRes = falseRes + 1


