#!/usr/bin/env python3
import subprocess
import re
import os
import sys
#import matplotlib.pyplot as plt
#import  numpy as np
#import time

datas=[[2, 0], [3, 0], [1, 0], [5, 0] , [9, 0], [8, 0], [6, 0]]

sortedData=['blank' for element in datas]
print(sortedData)
for data in datas:
    i=0
    for j in range(datas.index(data)+1, len(datas)):
        if float(data[0]) - float(datas[j][0]) < 0:
           i+=1
           
    for k in range(0, datas.index(data)):
        if float(data[0]) - float(datas[k][0]) < 0:
           i+=1      
    if sortedData[i]=='blank':
        sortedData[i]=(data[0])
    else:
       sortedData.insert(i, data[0])
while len(sortedData) != 0 and 'blank' in sortedData:
    sortedData.remove('blank')
print(sortedData)

