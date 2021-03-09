import math

n=69
m=24

def f13(n,m):
    
    summ=0
    total=0
    for i in range (1,n+1):
        for j in range (1,m+1):
            summ+=40*pow(j,5)+62*pow(j,6)
            
    for i in range(1,n+1):
        total+=pow(i,6)-60*pow(i,7)
        
    res=28*summ-85*total
    return res

f13(n,m)
