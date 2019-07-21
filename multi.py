import threading
#import random
import time
from itertools import islice
#import Multithreading as m

def csv_txt(csv,txt,j,i,lock):
    lock.acquire()
    o1=open(csv,"r")
    o2=open(txt,"a+")
    #print("csv_text")
    for line in islice(o1,i*j, ((i*j)+i)):
        o2.writelines(line)

    o1.close()
    o2.close()
    lock.release()

def txt_csv(txt,csv,j,i,lock):
    lock.acquire()
    o1=open(txt,"r")
    o2=open(csv,"a+")
    #print("txt_csv")
    for line in islice(o1,i*j, ((i*j)+i)):
        o2.writelines(line)

    o1.close()
    o2.close()
    lock.release()

def transform(readfile,writefile,j,i,lock):
    lock.acquire()
    o1=open(readfile,"r")
    o2=open(writefile,"a+")
    #print("transform")
    #print("object o1",o1.writelines)
    #print("i",i,"j",j)
    for line in islice(o1,i*j, ((i*j)+i)):
        #print("r1")
        arr = line.split(",")
        #print(arr)
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
        #print(str)
        o2.writelines(str)

    o1.close()
    o2.close()
    lock.release()
       
   


def fun3():#multithreading
    #conversion some portion of csv to txt
    #calling to function transform(readfile,writefile)   writefile in append mode
    #conversion some portion of txt to csv   csv file in append mode
    time_mt=[]
    for i in range(1,11):
        start1=time.clock()
        initial_txt = open("out.txt", "w")
        final_txt = open("data.txt", "w")
        final_csv = open("final_data.csv", "w")

        initial_txt.write("")
        final_txt.write("")
        final_csv.write("")
        initial_txt.close()
        final_txt.close()
        final_csv.close()

        lock=threading.Lock()
        rand=i*10000
        print("random no:",rand)
        for j in range(int(100000/rand)):
            t1 = threading.Thread(target=csv_txt, args=("Database10k.csv", "out.txt", j,rand,lock))
            t2 = threading.Thread(target=transform, args=("out.txt", "data.txt", j,rand,lock))
            t3 = threading.Thread(target=txt_csv, args=("data.txt","final_data.csv", j,rand,lock))
            t1.start()
            t2.start()
            t3.start()
            
            t1.join()
            t2.join()
            t3.join()
        end1=time.clock()
        print("Multithreading time:",(end1-start1))
        time_mt.append(end1-start1)
        
    return time_mt
    

def mt_record(i,k):#multithreading
    #conversion some portion of csv to txt
    #calling to function transform(readfile,writefile)   writefile in append mode
    #conversion some portion of txt to csv   csv file in append mode
    start1=time.clock()
    initial_txt = open("out.txt", "w")
    final_txt = open("data.txt", "w")
    final_csv = open("final_data.csv", "w")

    initial_txt.write("")
    final_txt.write("")
    final_csv.write("")
    initial_txt.close()
    final_txt.close()
    final_csv.close()

    lock=threading.Lock()
    rand=k
    #print("random no:",rand)
    for j in range(int(i*1000/rand)):
        t1 = threading.Thread(target=csv_txt, args=("Database10k.csv", "out.txt", j,rand,lock))
        t2 = threading.Thread(target=transform, args=("out.txt", "data.txt", j,rand,lock))
        t3 = threading.Thread(target=txt_csv, args=("data.txt", "final_data.csv", j,rand,lock))
        t1.start()
        t1.join()
        
        t2.start()
        t2.join()
        
        t3.start()   
        t3.join()

    end1=time.clock()
    print("Multithreading time:",(end1-start1))
    return (end1-start1)
    
'''
records=fun3()*10000+10000
records

time_mt=[]
for i in range(10,101,10):
    time_mt.append(mt_record(i,records))
    
time_mt
'''
def main():
    time_opt=[]
    time_opt=fun3()
    records=(time_opt.index(min(time_opt)))*10000+10000
    records
    time_mt=[]
    for i in range(10,101,10):
        time_mt.append(mt_record(i,records))
    return time_opt,time_mt


