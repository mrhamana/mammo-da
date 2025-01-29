import sys

def extractinfo(file, column_index, seperator=","):

    lines = open(file, "r")
    data = []

    for line in lines:
        val = line.strip().split(seperator)[column_index]
        data.append(val)

    return data

def titles(file,row=0):
    lines=open(file,'r')
    count=0
    
    for line in lines:
        val = line.strip().split(',')
        
        
        if count==row:
            break
        
        count+=1

    return val

def malignant(file, column_index, seperator=","):

    if column_index == 1:
        return None

    lines = open(file, "r")
    ans = []
    for line in lines:
        val = line.strip().split(seperator)
        if val[1] == "M":
            ans.append(float(val[column_index]))

    return ans


def benign(file, column_index, seperator=","):

    if column_index == 1:
        return None

    lines = open(file, "r")
    ans = []
    for line in lines:
        val = line.strip().split(seperator)
        if val[1] == "B":
            ans.append(float(val[column_index]))

    return ans

def pair_vals(file,d1,d2):
    ans=[]
    
    lines=open(file,'r')
    
    for line in lines:
        line= line.split(',')
        ans.append([line[d1],line[d2]])
        
    return ans[0],ans[1:]

