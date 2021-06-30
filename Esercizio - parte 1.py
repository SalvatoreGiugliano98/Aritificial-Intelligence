#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 16:07:49 2021

@author: salvatoregiugliano
"""

import treepredict
import numpy as np
import re




gini = treepredict.giniimpurity(treepredict.my_data)
entropy = treepredict.entropy(treepredict.my_data)

print('Entropy :', entropy ,' \nGini Impurity:', gini)

set1,set2 = treepredict.divideset(treepredict.my_data,2,'yes')
print('Set 1: ' , set1 , ' \n\nSet 2:', set2)

gini = treepredict.giniimpurity(set1)
entropy = treepredict.entropy(set1)

print('Entropy on set1:', entropy ,' \nGini Impurity on set1:', gini)
gini = treepredict.giniimpurity(set2)
entropy = treepredict.entropy(set2)

print('Entropy on set2:', entropy ,' \nGini Impurity on set2:', gini)

tree = treepredict.buildtree(treepredict.my_data)

treepredict.printtree(tree)

treepredict.drawtree(tree,jpeg='treeview.jpg')

x = treepredict.classify(['google','USA','yes','None'], tree)

print(x)

