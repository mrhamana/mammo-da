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


def normal_graph(data, n):
    mean_data = np.mean(data)
    std_data = fn.central_moments(2, data)**(1/2)
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
        def pdf_func(x): return stats.norm.pdf(x, *params)
    elif skewness > 0:
        dist_name = "gamma"
        params = stats.gamma.fit(data)
        def pdf_func(x): return stats.gamma.pdf(x, *params)
    elif skewness < 0:
        dist_name = "lognorm"
        params = stats.lognorm.fit(data)
        def pdf_func(x): return stats.lognorm.pdf(x, *params)
    else:
        dist_name = "t"
        params = stats.t.fit(data)
        def pdf_func(x): return stats.t.pdf(x, *params)

    x = np.linspace(min(data), max(data), 1000)
    pdf_fitted = pdf_func(x)

    if plot:
        plt.plot(x, pdf_fitted, 'r-',
                 label=f"Fitted {dist_name.capitalize()} PDF")
        plt.legend()
        plt.show()


def scatter_plot(x, y, xlabel=None, ylabel=None, title=None):
    """Create a scatter plot with optional labels."""
    plt.figure(figsize=(10, 8))
    plt.scatter(x, y, alpha=0.5)
    plt.xlabel(xlabel if xlabel else 'X')
    plt.ylabel(ylabel if ylabel else 'Y')
    plt.title(title if title else 'Scatter Plot')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()


def qq_plot(data, dist='norm'):
    """Create a Q-Q plot to check for normality."""
    plt.figure(figsize=(10, 8))
    stats.probplot(data, dist=dist, plot=plt)
    plt.title('Q-Q Plot')
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
