# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 14:30:08 2018

@author: mmaaz

"""
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 22:21:28 2017

@author: mmaaz

"""
import csv


def main():
    directory=  "C:/Users/mmaaz/Documents/Programming/Introduction to Bioinformatics Algorithms/Ass_1/pmdata"
    
    pollutantmean(directory, "nitrate", [23])
    
    
def pollutantmean(directory, pollutant, id=range(1,11)):
    sum=0
    quant=0
    i=0;
    for i in id:
        with open(directory+ "/{0:03}.csv".format(i), newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\n')
            next(reader)
            for row in reader:
                items= row[0].split(",");
            
                if(pollutant== "sulfate" and not items[1] == "NA"):
                    sum+= float(items[1])
                    quant+=1
                
                elif(pollutant=="nitrate" and not items[2]=="NA"):
                    sum+=float(items[2])
                    quant+=1
                
    print("{:.3f}".format(sum/ quant))
if __name__ == '__main__':
    main()

