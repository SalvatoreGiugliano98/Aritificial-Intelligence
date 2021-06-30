#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:11:41 2021

@author: salvatoregiugliano
"""

import optimization

s = [1,4,3,2,7,3,6,3,2,4,5,3]

optimization.printschedule(s)
cost = optimization.schedulecost(s)
print('costo:', cost)


domain = [(0,8)]*(len(optimization.people)*2)

s = optimization.randomoptimize(domain, optimization.schedulecost)
optimization.printschedule(s)
cost = optimization.schedulecost(s)
print('Random costo:', cost)

s = optimization.hillclimb(domain, optimization.schedulecost)
optimization.printschedule(s)
cost = optimization.schedulecost(s)
print('Hill Climb costo:', cost)

s = optimization.annealingoptimize(domain, optimization.schedulecost)
optimization.printschedule(s)
cost = optimization.schedulecost(s)
print('Annealing costo:', cost)

s = optimization.geneticoptimize(domain, optimization.schedulecost)
optimization.printschedule(s)
cost = optimization.schedulecost(s)
print('Genetic costo finale:', cost)