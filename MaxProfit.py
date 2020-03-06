# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:32:17 2020

@author: wmy
"""
# exempt 01

S=[1,2,9,4,5,6,7,10]
minPrice=S[0]
N=0
profit=0
selDay=0
buyDay=0

for N in range(len(S)):
    if (S[N]<minPrice):
        minPrice =S[N]
        buyDay=N
    
    if (S[N]-minPrice>profit):
        profit =S[N]-minPrice
        selDay=N

print ("at {0} to buy,at {1} to sell,the maxprofit is {2}". format(buyDay+1,selDay+1,profit))