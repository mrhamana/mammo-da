import matplotlib.pyplot as plt
import numpy as np
from functions import frequency
import extract_data as ed

def histo_graph(file,intervals=20,column_number=3):
    header=ed.extractinfo(file,column_number,',')[0]
    y=ed.extractinfo(file,column_number,',')[1:]
   
    y=[float(i) for i in y]
  

    bin_edges, frequencies = frequency(y, groups=intervals)

    print(bin_edges,frequencies)
    plt.figure(figsize=(10, 10))
    plt.bar(bin_edges[:-1], frequencies, width=np.diff(bin_edges), align='edge', edgecolor='black')

    plt.xlabel('Group')
    plt.ylabel('Frequency')
    plt.title('Frequency Distribution of {}'.format(header))
    plt.show()
