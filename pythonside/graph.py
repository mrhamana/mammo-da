import matplotlib.pyplot as plt
import numpy as np
import functions as fn
import scipy.stats as stats
from scipy import stats


def histo_graph(data, intervals=20, header=None):

    bin_edges, frequencies = fn.frequency(data, groups=intervals)

    plt.figure(figsize=(10, 10))
    plt.bar(bin_edges[:-1], frequencies,
            width=np.diff(bin_edges), align='edge', edgecolor='black')

    plt.xlabel('Group')
    plt.ylabel('Frequency')
    plt.title('Frequency Distribution of {}'.format(header))
    plt.show()


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
    plt.boxplot(data, orientation='horizontal')
    plt.show()


def normal_graph(data, std_dev_range=3, title=None, xlabel=None, ylabel=None, figsize=None):
    mean_data = np.mean(data)
    std_data = fn.central_moments(2, data)**(1/2)
    
    if figsize: plt.figure(figsize=figsize)
    
    x = np.linspace(mean_data - std_dev_range*std_data, 
                    mean_data + std_dev_range*std_data, 
                    1000)
    y = stats.norm.pdf(x, mean_data, std_data)
    
    plt.plot(x, y, 'b-', lw=2)
    plt.title(title or 'Normal Distribution Fit')
    plt.xlabel(xlabel or 'Values')
    plt.ylabel(ylabel or 'Probability Density')
    plt.grid(True)
    plt.show()


def estimate_pdf(data, num_points=1000, title=None, xlabel=None, ylabel=None, figsize=None, plot=True):
    # Calculate distribution characteristics
    skewness_val = fn.skewness(data)
    kurtosis_val = fn.kurtosis(data)

    # Distribution fitting logic (keep your existing code)
    if np.abs(skewness_val) < 0.1 and np.abs(kurtosis_val) < 0.1:
        dist_name = "normal"
        params = stats.norm.fit(data)
        def pdf_func(x): return stats.norm.pdf(x, *params)
    elif skewness_val > 0:
        dist_name = "gamma"
        params = stats.gamma.fit(data)
        def pdf_func(x): return stats.gamma.pdf(x, *params)
    elif skewness_val < 0:
        dist_name = "lognorm"
        params = stats.lognorm.fit(data)
        def pdf_func(x): return stats.lognorm.pdf(x, *params)
    else:
        dist_name = "t"
        params = stats.t.fit(data)
        def pdf_func(x): return stats.t.pdf(x, *params)

    # Generate PDF points
    x = np.linspace(min(data), max(data), num_points)
    pdf_fitted = pdf_func(x)

    if plot:
        # Configure plot appearance
        if figsize:
            plt.figure(figsize=figsize)
        plt.plot(x, pdf_fitted, 'r-',
                 label=f"Fitted {dist_name.capitalize()} PDF")

        # Add labels if provided
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)

        plt.legend()
        plt.show()

    return x, pdf_fitted  # Return values for further analysis


def scatter_plot(x, y, xlabel=None, ylabel=None, title=None):
    """Create a scatter plot with optional labels."""
    plt.figure(figsize=(10, 8))
    plt.scatter(x, y, alpha=0.5)
    plt.xlabel(xlabel if xlabel else 'X')
    plt.ylabel(ylabel if ylabel else 'Y')
    plt.title(title if title else 'Scatter Plot')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()


def qq_plot(data, dist='norm', title=None, xlabel=None, ylabel=None, figsize=None):
    """Create a Q-Q plot to check for normality."""
    if figsize:
        plt.figure(figsize=figsize)
        
    stats.probplot(data, dist=dist, plot=plt)
    
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
        
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()


def correlation_heatmap(data, labels=None):
    """Create a correlation heatmap."""
    plt.figure(figsize=(10, 8))
    plt.imshow(data, cmap='coolwarm', aspect='auto')
    plt.colorbar()

    if labels:
        plt.xticks(range(len(labels)), labels, rotation=45)
        plt.yticks(range(len(labels)), labels)

    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.show()
