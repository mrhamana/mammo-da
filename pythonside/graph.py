import matplotlib.pyplot as plt
import numpy as np
import functions as fn
import scipy.stats as stats

def histo_graph(data,intervals=20,header=None):
    
    bin_edges, frequencies = fn.frequency(data, groups=intervals)

    
    plt.figure(figsize=(10, 10))
    plt.bar(bin_edges[:-1], frequencies, width=np.diff(bin_edges), align='edge', edgecolor='black')

    plt.xlabel('Group')
    plt.ylabel('Frequency')
    plt.title('Frequency Distribution of {}'.format(header))
    plt.show()

import matplotlib.pyplot as plt

def plot_sorted_horizontal_bar_graph(data, max_bars=20):
    label, my_list = data
    sorted_data = sorted(my_list, key=lambda x: x[1], reverse=False)
    
   
    if len(sorted_data) > max_bars:
        sorted_data = sorted_data[-max_bars:] 
    
    labels = [item[0] for item in sorted_data]
    values = [item[1] for item in sorted_data]

    plt.figure(figsize=(10, min(0.5 * len(labels), 12)))  
    plt.barh(labels, values, color='skyblue')

    plt.xlabel(label[1])
    plt.title('Bar Graph')

    plt.xticks(rotation=45) 
    plt.tight_layout()
    plt.show()


def boxplot(data):
    plt.boxplot(data,orientation='horizontal')
    plt.show()
    
def normal_graph(data,n):
    mean_data = np.mean(data)
    std_data = fn.central_moments(2,data)**(1/2)
    x = np.arange(-n+mean_data, +n+mean_data, 0.1)
    const = np.sqrt(2 * np.pi * std_data**2)
    num = np.exp(-(x - mean_data)**2 / (2 * std_data**2))
    y = num / const
    plt.plot(x, y)
    plt.title('Normal Distribution')
    plt.xlabel('x')
    
    plt.ylabel('Probability Density')
    plt.show()
    
def estimate_pdf(data, plot=True):
    skewness = fn.skewness(data)
    kurtosis = fn.kurtosis(data) 
    
    
    if np.abs(skewness) < 0.1 and np.abs(kurtosis) < 0.1:
        dist_name = "normal"
        params = stats.norm.fit(data)
        pdf_func = lambda x: stats.norm.pdf(x, *params)
    elif skewness > 0:
        dist_name = "gamma"
        params = stats.gamma.fit(data)
        pdf_func = lambda x: stats.gamma.pdf(x, *params)
    elif skewness < 0:
        dist_name = "lognorm"
        params = stats.lognorm.fit(data)
        pdf_func = lambda x: stats.lognorm.pdf(x, *params)
    else:
        dist_name = "t"
        params = stats.t.fit(data)
        pdf_func = lambda x: stats.t.pdf(x, *params)
    
    
    x = np.linspace(min(data), max(data), 1000)
    pdf_fitted = pdf_func(x)
    
    if plot:
        plt.plot(x, pdf_fitted, 'r-', label=f"Fitted {dist_name.capitalize()} PDF")
        plt.legend()
        plt.show()
    