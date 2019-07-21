# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:35:09 2019

@author: DELL
"""
import time
from itertools import islice

def fun2(k):
    start=time.clock()
    dataFile=open("database10k.csv","r")
    final=open("final_data.csv",'w')
    for line in islice(dataFile,0,k*1000):
        arr = line.split(",")
        del (arr[1])
        if arr[3] != "Phone No":
            arr[3] = "+91" + arr[3]
        if arr[4] != "Gender\n":
            if arr[4] == "M\n":
                arr[4] = "1"
            else:
                arr[4] = "0"
        str = ','.join(arr)
        str = str + "\n"
        final.writelines(str)
    
    dataFile.close()
    final.close()            
    end=time.clock()
    print("Direct Conversion time:",(end-start))
    return (end-start)

def main():
    time_dc=[]
    for i in range(10,101,10):
        time_dc.append(fun2(i))
    return time_dc
'''
t=[]
t=main()
t
'''