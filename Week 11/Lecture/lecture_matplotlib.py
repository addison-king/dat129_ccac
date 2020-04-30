# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:12:06 2020

@author: falconfoe
"""
import matplotlib.pyplot as plt
import numpy as np



def main():
    
    hours = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    
    
    plt.plot(hours,
        [0,0,0,0,0,0,33,66,100,100,90,80,70,60,50,40,30,20,10,0,0,0,0,0],
        label='Brandyn')
    
    plt.plot(hours,
        [0,0,0,0,0,0,0,0,0,10,20,30,40,60,80,100,100,70,50,50,75,33,0,0],
        label='Laura')
    
    
    
    plt.ylabel('Energy Percentage')
    plt.xlabel('Hour')
    plt.title('Daily Energy Amounts')
    plt.xticks(np.arange(min(hours), max(hours)+2, 2.0))
    plt.legend()
    print()

if __name__ == "__main__":
    main()