# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:34:47 2019

@author: DELL
"""
import time
from itertools import islice

def fun2(k):#file conversion
    start=time.clock()
    csv_file = open("database10k.csv", "r")
    txt_file = open("out.txt", "w")
    txt2 = open("data.txt", "w")
    
    for line in islice(csv_file,0,k*1000):
        txt_file.writelines(line)

    txt_file.close()
    csv_file.close()
    txt_file = open("out.txt", "r")

    for line in txt_file:
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
        txt2.writelines(str)
    txt2.close()
    txt_file.close()
    txt2 = open("data.txt", "r")
    final_csv = open("final_data.csv", "w")

    for line in txt2:
        final_csv.writelines(line)
    end=time.clock()
    print("file conversion time:",(end-start))
    time1=end-start
    return time1

def main():
    time_fc=[]
    for i in range(10,101,10):
        time_fc.append(fun2(i))
    return time_fc
'''
t=[]
t=main()
t
'''
    
