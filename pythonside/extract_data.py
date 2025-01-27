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
