import matplotlib.pyplot as plt

def plot_sorted_horizontal_bar_graph(data):
    
    sorted_data = sorted(data, key=lambda x: x[1], reverse=False)
    
    
    labels = [item[0] for item in sorted_data]
    values = [item[1] for item in sorted_data]
    
   
    
    plt.barh(labels, values, color='skyblue')  
    
    
    plt.xlabel('Values')
    plt.ylabel('Labels')
    plt.title('Horizontal Bar Graph Sorted in Descending Order')
    
    
    plt.tight_layout()  
    plt.show()


data = [["A", 10], ["B", 30], ["C", 20], ["D", 50], ["E", 40]]
plot_sorted_horizontal_bar_graph(data)