import numpy as np
import functions as f


x=f.malignant("../data/data.csv",8,',')
y=f.benign("../data/data.csv",8,',')

print(len(x),len(y))

n=min(len(x),len(y))

x=x[:n]
y=y[:n]

f.plt.scatter(x,y)
f.plt.show()