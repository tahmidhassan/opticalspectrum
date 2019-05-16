# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:38:01 2019

Transmission Spectrum captured through Newport Meter / SANTEC TSL-510

@author: Tahmid Hassan Talukdar
"""

import numpy as np
import matplotlib.pyplot as plt

Fs = 1000; 
Ts = 1/Fs;
dt = np.arange(0,2-Ts,Ts)


import csv 

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    lambdas = []
    R = []
    
    for row in readCSV:
        a = row[0]
        lambdas.append(a)
        b = row[1]
        R.append(b)

x = np.zeros(len(lambdas)-13)       
y = np.zeros(len(lambdas)-13)

for i in range(13, len(lambdas)):
    x[i-13] = float(lambdas[i])
    y[i-13] = float(R[i])

plt.plot(x,y)

