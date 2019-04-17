# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 07:20:20 2018

@author: mmaaz
"""
import numpy as np
import pandas as pd


def main():
    # print(findKeyForLargestValue({'1':'380', '2':'10071', '3': '70', '4': '3230' }))
    fileName = 'genome-assembly.txt'
    reads = readDataFromFile(fileName)
    print(reads)
    print(meanLength(fileName))
    overlaps = allOverLaps(reads)
    print(overlaps)
    prettyPrint(overlaps)
    name = findFirstRead(overlaps)
    order = findOrder(name, overlaps, list())
    print(order)
    genome = assembleGenome(order, reads, overlaps)
    print(genome)


def readDataFromFile(fileName):
    geneList = {}

    for line in open(fileName):
        name, sequence = line.split(" ")
        geneList[name] = sequence.rstrip("\n")

    return geneList


def meanLength(fileName):
    return (sum([len(value) for value in readDataFromFile(fileName).values()])
            / len(readDataFromFile(fileName).values()))


def getOverLap(left, right):
    left = list(left)
    right = list(right)
    n = min(len(left), len(right))

    if (n == len(left)):
        # print(n)
        for i in range(n):
            if (left[i:] == right[:n - i]):
                return left[i:]
            else:
                continue

    else:
        N = len(left) - len(right) + 1
        # print (N)
        left_prime = left[N:]
        for i in range(n):
            if (left_prime[i:] == right[:n - i - 1]):
                return left_prime[i:]
            else:
                continue


def allOverLaps(reads):
    # takes the dict argument cming from readsDatfile, take its key to be the name of left string, and then
    # for all other strings compute its over lap
    ovDict = {}
    for key1, v1 in reads.items():
        nested = {}
        for key2, v2 in reads.items():
            if (key2 != key1):
                arr = np.array(getOverLap(v1, v2))
                length = arr.size
                nested[str(key2)] = length
        ovDict[str(key1)] = nested

    # print (ovDict['1'].values())
    return (ovDict)


def prettyPrint(overlaps):
    d = pd.DataFrame(columns=overlaps.keys(), index=overlaps.keys())
    for i in range(1, len(d) + 1):
        for j in range(1, len(d) + 1):
            if (i == j):
                d.loc[str(i), str(j)] = '-'
                continue
            else:
                d.loc[str(i), str(j)] = overlaps[str(i)][str(j)]
    print(d)


def findFirstRead(overlaps):
    d = pd.DataFrame(columns=overlaps.keys(), index=overlaps.keys())
    arr = list()
    for i in range(1, len(d) + 1):
        for j in range(1, len(d) + 1):
            if (i == j):
                d.loc[str(i), str(j)] = '-'
                continue
            else:
                d.loc[str(i), str(j)] = overlaps[str(i)][str(j)]
    for i in range(1, len(d) + 1):
        count = 0
        for j in range(1, len(d) + 1):
            if (i == j):
                continue
            else:
                if (int(d.loc[str(j)][str(i)]) > 2):
                    count += 1
        arr.append(count)
    ind_min = np.argmin(arr)

    return (str(ind_min + 1))


def findKeyForLargestValue(d):
    maxv = 0
    maxk = ''
    for k, v in d.items():
        if (int(d[k]) > (maxv)):
            maxk = k
            maxv = int(d[k])
    return maxk


def findOrder(name, overlaps, order):
    if (len(order) == len(overlaps) - 1):
        return order.append(name)
    else:
        k = findKeyForLargestValue(overlaps[name])
        order.append(name)
        (findOrder(k, overlaps, order))
        return order


def assembleGenome(readOrder, reads, overlaps):
    # take read name from readOrder
    # get its sequence from reads and assign it to s
    # for subsequent reads:
    # take name from read order
    # search it in previous read's dictionary to find the length of overlap
    # delete this number of characters from end of left string
    # append the new string
    rO = readOrder[0]
    seq = reads[rO]
    for i in range(1, len(readOrder)):
        r = readOrder[i]
        overlap_length = overlaps[str(rO)][str(r)]
        seq = seq[:-overlap_length] + reads[r]
        rO = r

    return seq


if __name__ == '__main__':
    main()
