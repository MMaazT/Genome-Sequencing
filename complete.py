# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:39:03 2018

@author: mmaaz
"""

import csv
import pandas as pd

def main():
    directory=  "C:/Users/mmaaz/Documents/Programming/Introduction to Bioinformatics Algorithms/Ass_1/specdata"
    
    #print(complete(directory,[30, 29, 28, 27, 26, 25]))
    print(complete(directory))

    
def complete(directory, id=range(1,333)):
    i=0
    idList = {}
    
    for i in id:
        idList[str(i)] = 0
        with open(directory+ "/{0:03}.csv".format(i), newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\n')
            next(reader)
            
            for row in reader:
                items= row[0].split(",");
            
                if(not items[1] == "NA" and not items[2]=="NA"):
                    idList[str(i)] += 1
                
             #Store with id numer in data frame
    d= pd.DataFrame(data={"id":list(idList.keys()),"nobs":list(idList.values())})
    #print(d)
    return d
if __name__ == '__main__':
    main()
