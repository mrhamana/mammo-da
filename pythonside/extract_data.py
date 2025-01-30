def extractinfo(file, list, seperator=","):

    lines = open(file, "r")
    data = []
    count=0
    for line in lines:
        if not count==0:
            
            val = line.strip().split(seperator)[list[0]]
            data.append(float(val))

        count+=1
    return list[1],data

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
        temp1=''
        temp2=''
        if line[d1][-2:]=='\n':
            temp1=line[d1][:-2]
        else:
            temp1=line[d1]
            
        if line[d2][:-2]=='\n':
            temp2=line[d2][:-2]
        else:
            temp2=line[d2]
            
        try:
            temp1=float(temp1)
        except ValueError:
            pass
        
        try:
            temp2=float(temp2)
        except ValueError:
            pass
        
        ans.append([temp1,temp2])
    return ans[0],ans[1:]
        
            
        
    

