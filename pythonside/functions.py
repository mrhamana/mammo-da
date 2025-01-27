import numpy as np
import matplotlib.pyplot as plt
from math import floor ,ceil

def extractinfo(file,column_index, seperator=','):
    
    lines = open(file,'r')
    data=[]
    
    for line in lines:
        val=line.strip().split(seperator)[column_index]
        data.append(float(val))
        
    return data
        
    
    
def malignant(file,column_index,seperator=","):
    
    if column_index==1:
        return None
    
    lines = open(file,'r')
    ans=[]
    for line in lines:
        val=line.strip().split(seperator)
        if val[1]=="M":
            ans.append(float(val[column_index]))
            
    return ans


def benign(file,column_index,seperator=","):
    
    if column_index==1:
        return None
    
    lines = open(file,'r')
    ans=[]
    for line in lines:
        val=line.strip().split(seperator)
        if val[1]=="B":
            ans.append(float(val[column_index]))
            
    return ans

def mean(x):
    return sum(x)/len(x)

def median(x):
    n=len(x)
    
    if n %2 ==1:
        return x[n//2]
    else:
        return (x[floor((n-1)/2)]+x[ceil((n-1)/2)])/2
    

def smallest(x):
    small=float('inf')
    
    for i in x:
        if i<small:
            small=i

    return small

def largest(x):
    biggest=float('-inf')
    for i in x:
        if i>biggest:
            biggest=i
            
    return biggest

def range(x):
    return largest(x)-smallest(x)

def coff_range(x):
    num=largest(x)-smallest(x)
    den=largest(x)+smallest(x)
    
    return num/den

def meanroot(x):
    ans=0
    
    for i in x:
        ans=ans+(i-mean(x))**(2)
        
    return ans

def correlation(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    numerator = np.sum([(i - mean_x) * (j - mean_y) for i, j in zip(x, y)])
    denominator = np.sqrt(np.sum([(i - mean_x) ** 2 for i in x]) * np.sum([(j - mean_y) ** 2 for j in y]))

    if denominator == 0:
        return np.nan  

    corr=numerator / denominator
    print("The corrolation of the function is {}".format(corr))
    
    return corr
    

def y_intercept(x,y):
    y=mean(y)-correlation(x,y)*mean(x)
    print("The y intercept of the data is {}".format(y))
    return y

def central_moments(n,x):
    ans=0
    
    for i in x:
        ans=ans+(x-mean(x))**(n)
        
    return ans/len(x)


x=[-10,-69,1,2]
print(largest(x))