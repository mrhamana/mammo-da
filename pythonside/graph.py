import matplotlib.pyplot as plt
import numpy as np
from functions import frequency,deviation,mean
import extract_data as ed

def histo_graph(file,intervals=20,column_number=3):
    header=ed.extractinfo(file,column_number,',')[0]
    y=ed.extractinfo(file,column_number,',')[1:]
   
    y=[float(i) for i in y]
  

    bin_edges, frequencies = frequency(y, groups=intervals)

    
    plt.figure(figsize=(10, 10))
    plt.bar(bin_edges[:-1], frequencies, width=np.diff(bin_edges), align='edge', edgecolor='black')

    plt.xlabel('Group')
    plt.ylabel('Frequency')
    plt.title('Frequency Distribution of {}'.format(header))
    plt.show()

def plot_sorted_horizontal_bar_graph(data):
    label,my_list=data
    sorted_data = sorted(my_list, key=lambda x: x[1], reverse=False)
    labels = [item[0] for item in sorted_data]
    values = [item[1] for item in sorted_data]
    plt.barh(labels, values, color='skyblue')  
    plt.xlabel(label[1])
    
    plt.title('Bar Graph ')
    
    
    plt.tight_layout()  
    plt.show()

def boxplot(data):
    plt.boxplot(data,orientation='horizontal')
    plt.show()
    
def normal_graph(data):
    mean_data = np.mean(data)
    std_data = deviation(data)
    x = np.arange(-10+mean_data, +10+mean_data, 0.1)
    const = np.sqrt(2 * np.pi * std_data**2)
    num = np.exp(-(x - mean_data)**2 / (2 * std_data**2))
    y = num / const
    plt.plot(x, y)
    plt.title('Normal Distribution')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.show()
    
