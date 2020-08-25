import numpy as np
import pandas as pd
import random 
k=int(input("How many chits do you want for each allele? ",))

a1=np.full(shape=k,fill_value=2,dtype=np.int)
b1=np.full(shape=k,fill_value=3,dtype=np.int)

#Creating empty sets for inputing data
v1 = []
v2 = []
v3 = []
v4 = []
v5 = []
v6 = []
v7 = []
v8 = []
v9 = []
v10 = []

rem = random.randrange(10,24,2) #This is the number of chits we remove
original_sample = np.concatenate([a1,b1]) 
reduced_sample = np.random.choice(original_sample,(2*k - rem),replace = False) #We randomly remove rem number of chits from the total sample space and put the alleles back into individual sets


for j in range(3): #No. of generations = 3
    s1=0
    s2=0
    s3=0
    s4=0
    s5=0
    s6=0
    s7=0
    s8=0
    s9=0
    s10=0
    a = list([])
    b = list([])
    for i in range(len(reduced_sample)):
        if reduced_sample[i] == 2:
            a.append(reduced_sample[i])
        else:
            b.append(reduced_sample[i])
    
    emi_a = k - len(a) 
    emi_b = k - len(b)
    c1=np.full(shape=emi_a,fill_value=5,dtype=np.int) #This is the set of crossed a chits
    d1=np.full(shape=emi_b,fill_value=7,dtype=np.int) #This is the set of crossed b chits
    c=list(c1)
    d=list(d1)
    modified_sample=np.concatenate([reduced_sample,c,d])      
    for i in range(k):
        sample_space = np.concatenate((a,b,c,d))
        res = np.random.choice(sample_space,2,replace = False) #Choosing two chits at random
        x = np.product(res)
        if x == 4:
            s1+=1
            a = np.delete(a,[0,1])
        elif x==6:
            s2+=1                  
            a = np.delete(a,[0])
            b = np.delete(b,[0])
        elif x==10 :
            s3+=1
            a = np.delete(a,[0])
            c = np.delete(c,[0])
        elif x == 14:
            s4+=1
            a = np.delete(a,[0])
            d = np.delete(d,[0])
        elif x==9:
            s5+=1                  
            b = np.delete(b,[0,1])
        elif x==15:
            s6+=1
            b = np.delete(b,[0])
            c = np.delete(c,[0])
        elif x == 21:
            s7+=1
            b = np.delete(b,[0])
            d = np.delete(d,[0])
        elif x==25:
            s8+=1                   
            c = np.delete(c,[0,1])
        elif x==35:
            s9+=1
            c = np.delete(c,[0])
            d = np.delete(d,[0])
        else :
            s10+=1
            d = np.delete(d,[0,1])
        
                 
    v1.append(s1)
    v2.append(s2)
    v3.append(s3)
    v4.append(s4)
    v5.append(s5)
    v6.append(s6)
    v7.append(s7)
    v8.append(s8)
    v9.append(s9)
    v10.append(s10)
    
Generations = {"aa":v1, "ab":v2, "bb":v5, "ac":v3, "ad":v4, "bc":v6, "bd":v7, "cc":v8, "cd":v9, "dd":v10}
                
chart = pd.DataFrame.from_dict(Generations)

print(chart)
print("Alleles mutated: ",rem, "\na mutated: ",emi_a,"\nb mutated: ",emi_b)             
                



    
