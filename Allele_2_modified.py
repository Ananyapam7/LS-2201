import numpy as np
import pandas as pd
import random 
k=int(input("How many chits do you want for each allele? ",))

a1 =  np.zeros(k, dtype = int)
b1 =  np.ones(k, dtype = int)

#Creating empty sets for inputing data
m = []
n = []
o = []
p = []
q = []
r = []
s = []
rem = random.randrange(10,24,2) #This is the number of chits we remove
original_sample = np.concatenate([a1,b1]) 
reduced_sample = np.random.choice(original_sample,(2*k - rem),replace = False) #We randomly remove rem number of chits from the total sample space and put the alleles back into individual sets


for j in range(3): #No. of generations = 3
    s1=0
    s2=0
    s3=0
    a = []
    b = []
    for i in range(len(reduced_sample)):
        if reduced_sample[i] == 0:
            a.append(reduced_sample[i])
        else:
            b.append(reduced_sample[i])
    emi_a = k - len(a) #Counting the number of each allele removed 
    emi_b = k - len(b)
            
    for i in range(int(len(reduced_sample)/2)):
        sample_space = np.concatenate((a,b))
        res = np.random.choice(sample_space,2,replace = False ) #Choosing two chits at random
        x = sum(res)
        if x == 0:
            s1+=1
            a = np.delete(a,[0,1])
        elif x==1:
            s2+=1                   #Separating the combination of chits according to their sum of the numbers representing alleles
            a = np.delete(a,[0])
            b = np.delete(b,[0])
        else:
            s3+=1
            b = np.delete(b,[0,1])
                 
    m.append(s1)
    n.append(s2)
    o.append(s3)
    p.append(rem)
    q.append(emi_a)
    r.append(emi_b)
    s.append(int((len(reduced_sample))/2))
Generations = {"aa":m, "ab":n, "bb":o, "Alleles removed":p, "a removed":q, "b removed":r, "Number of trials":s}
                
chart = pd.DataFrame.from_dict(Generations)

print(chart)
             
                



    
