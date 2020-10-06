#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 21:52:12 2020

@author: MussaYousef
"""

#Create an array of int ranging from 5-15
import numpy as np

a = np.arange(5,16,1)
print(a)
#Create an array containing 7 evenly spaced numbers between 0 and 23
b = np.arange(0,23,3)
print(b)

# Numpy has several routines for generating artificial data following a particular structure. Check this page for different types. And generate an artificial numpy array with values between -1 and 1 that follow a uniform data distribution.

c = np.random.uniform(-1,1,100)

print(c)

#Visualise the array in an histogram in matplotlib.

import matplotlib.pyplot as plt

print(plt.hist(c)) 

## Calculate the Euclidean distance as a calculator

from math import sqrt

p=np.random.rand(10)

q=np.random.rand(10)

print(p,q)

ed= np.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2+(p[2]-q[2])**2+(p[3]-q[3])**2+(p[4]-q[4])**2)+(p[5]-q[5])**2+(p[6]-q[6])**2+(p[7]-q[7])**2+(p[8]-q[8])**2+(p[9]-q[9])**2

print(ed)

## calculating the Euclidean distance using arithmetic operators 

euclideanDist = 0
for i in range (0, 10):
    euclideanDist += (p[i]-q[i])**2
    euclideanDist = sqrt(euclideanDist)
print(euclideanDist)


