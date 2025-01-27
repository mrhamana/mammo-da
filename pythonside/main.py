from functions import frequency
import extract_data as ed
import matplotlib.pyplot as plt

y=ed.extractinfo('../data/breast-cancer-cell-data.csv',5,',')[1:]


y=[float(i) for i in y]

freq=frequency(y)

plt.hist(freq )

plt.show()