# -*- coding: utf-8 -*-
"""
Created on Wed May  9 20:16:20 2018

@author: mmaaz
"""

import numpy as np
np.set_printoptions(threshold=np.inf)


def main():
    
    print (InvBWT("TTCCTAACG$A"))
    print (InvBWT("smnpbnnaaaaa$a"))
    print (InvBWT("annb$aa"))
    print(InvBWT("ard$rcaaaabb"))
    print(InvBWT("ACTGGCT$TGCGGC"))
    
    
    

def InvBWT(Transform):
    Constant=np.array(list(Transform))
    T=Constant[Constant[:len(Transform)].argsort()]
    
    T= np.vstack([Constant, T])
    T=T.transpose()
    T=T[T[:,0].argsort()]
   
    for i in range(len(Transform)-2):
        T=T.transpose()
        T= np.vstack([Constant, T])
        T=T.transpose()
        T=T[T[:,0].argsort()]
     
    #print(T)
    T=T.transpose()[:,0]
    String_Inv=""
    for s in T:
        String_Inv+=s
    
    String_Inv=String_Inv.replace("$", "");
    String_Inv+="$"

    return String_Inv 
     
    
if __name__=='__main__':
    main()
    