# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:28:15 2018

@author: mmaaz
"""

import csv
import pandas as pd
import numpy as np
from complete import complete
np.set_printoptions(threshold=np.inf)

def main():
    directory=  "C:/Users/mmaaz/Documents/Programming/Introduction to Bioinformatics Algorithms/Ass_1/specdata"
    corr(directory, 400)
    

def corr(directory, threshold):
    
    #open only those files whose nobs >threshold
    corrVect= []
    d= complete(directory, id=range(1,333))
    for i in range(0, len(d)):
        if (d.loc[i]['nobs']> threshold):
            n= d.loc[i]['id']
            with open(directory+ "/{num:0>3}.csv".format(num=str(n))) as csvfile:
    
                reader = csv.reader(csvfile, delimiter='\n')
                next(reader)
                
                sulf_vect= []
                nit_vect=[]
            
                for row in reader:
                    items= row[0].split(",");
            
                    if(not items[1] == "NA" and not items[2]=="NA"):
                        sulf_vect.append(float(items[1]))
                        nit_vect.append(float(items[2]))
                        
                c= np.corrcoef(sulf_vect, nit_vect)
                c= c[0][1]
                c = float("{0:.5f}".format(c))

                corrVect.append(c)                
            
    print(corrVect[:6])
            
        
if __name__=='__main__':
        main()
    

