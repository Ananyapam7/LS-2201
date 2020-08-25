import numpy as np
import pandas as pd
k=int(input("Input sample size of each type of allele: ",))

a1 = [0]
b1 = [1]

a2 =  [a for a in a1 for i in range(k)] 
b2 =  [b for b in b1 for i in range(k)] 

a = np.array(a2)
b = np.array(b2)

s1=0
s2=0
s3=0

m=[]
n=[]
o=[]


for j in range(3):  
    
    s1=0
    s2=0
    s3=0
    
    for i in range(k):
        sample_space = np.concatenate((a,b),0)
        res=np.random.choice(sample_space,2)
        x = sum(res)
        if x == 0:
            s1+=1
            np.delete(a,[0,1])
        elif x==1:
            s2+=1
            np.delete(a,[0])
            np.delete(b,[0])
        else:
            s3+=1
            np.delete(b,[0,1])
            
    
            
    m.append(s1)
    n.append(s2)
    o.append(s3)
    
Generations = {"aa":m, "ab":n, "bb":o}
                
chart = pd.DataFrame.from_dict(Generations)

print(chart)
             
                



    
