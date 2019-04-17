# -*- coding: utf-8 -*-
"""
Created on Mon May  7 18:44:15 2018

@author: mmaaz
"""
import numpy as np
np.set_printoptions(threshold=np.inf)

def main():
    
    print(StrToBWT('panamabananas$'))
    print(StrToBWT('banana$'))
    print(StrToBWT("abracadabra$"))
    print((StrToBWT('GCGTGCCTGGTCA$')))

def StrToBWT(Text):
    n=len(Text)
    
    A=np.zeros([n])
    for i in range(len(Text)):
       l= list(Text[-i:]+Text[:-i])
       A= np.vstack([A, l])
    A=np.delete(A, 0, axis=0)

        
    A=A[np.lexsort(np.fliplr(A).T)]
    #print(A)
    BWT=A[:,len(Text)-1]
    l=""
    for s in BWT:
        l=l+s    
    return (l)

if __name__=='__main__':
    main()