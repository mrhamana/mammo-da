import numpy as np
import matplotlib.pylab as plt
def extractinfo(column_index, seperator=','):
    
    lines = open("../data/wdbc.data",'r')
    data=[]
    
    for line in lines:
        val=line.strip().split(seperator)[column_index]
        data.append(float(val))
        
    return data
        
    
    
def malignant(column_index,seperator=","):
    
    if column_index==1:
        return None
    
    lines = open("../data/wdbc.data",'r')
    ans=[]
    for line in lines:
        val=line.strip().split(seperator)
        if val[1]=="M":
            ans.append(float(val[column_index]))
            
    return ans


def benign(column_index,seperator=","):
    
    if column_index==1:
        return None
    
    lines = open("../data/wdbc.data",'r')
    ans=[]
    for line in lines:
        val=line.strip().split(seperator)
        if val[1]=="B":
            ans.append(float(val[column_index]))
            
    return ans

def mean(x):
    return sum(x)/len(x)

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

