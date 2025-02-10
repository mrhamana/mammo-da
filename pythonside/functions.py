import numpy as np
from math import floor, ceil, sqrt
from scipy.stats import norm
from collections import Counter


def mean(x):
    return sum(x) / len(x)


def median(x):
    n = len(x)
    if n % 2 == 1:
        return x[n // 2]
    else:
        return (x[floor((n - 1) / 2)] + x[ceil((n - 1) / 2)]) / 2


def mode(x):
    """Calculate the mode (most frequent value) of a list."""
    from collections import Counter
    counts = Counter(x)
    max_count = max(counts.values())
    return [k for k, v in counts.items() if v == max_count]


def smallest(x):
    small = float("inf")

    for i in x:
        if i < small:
            small = i

    return small


def largest(x):
    biggest = float("-inf")
    for i in x:
        if i > biggest:
            biggest = i

    return biggest


def coff_range(largest, smallest):
    return (largest-smallest)/(largest+smallest)


def mean_dev(x):
    ans = 0
    for i in x:

        ans += abs(i - mean(x))

    return ans / len(x)


def meanroot(x):
    ans = 0

    for i in x:
        ans = ans + (i - mean(x)) ** (2)

    return ans


def correlation(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    numerator = np.sum([(i - mean_x) * (j - mean_y) for i, j in zip(x, y)])
    denominator = np.sqrt(
        np.sum([(i - mean_x) ** 2 for i in x]) *
        np.sum([(j - mean_y) ** 2 for j in y])
    )

    if denominator == 0:
        return np.nan

    corr = numerator / denominator
    print("The corrolation of the function is {}".format(corr))

    return corr


def y_intercept(x, y):
    y = mean(y) - correlation(x, y) * mean(x)
    print("The y intercept of the data is {}".format(y))
    return y


def central_moments(n, x):
    ans = 0

    for i in x:
        ans = ans + (i - mean(x)) ** (n)

    return ans / len(x)


def frequency(x, groups=50):
    if len(x) == 0:
        return np.zeros(groups, dtype=int)
    lowest = min(x)
    highest = max(x)
    bin_edges = np.linspace(lowest, highest, groups + 1)
    bins = np.digitize(x, bin_edges) - 1
    bins = np.clip(bins, 0, groups - 1)
    ans = np.bincount(bins, minlength=groups)

    return bin_edges, ans


def n_quartile(data, p):
    data.sort()
    n = len(data)

    position = (p*(n + 1)) / 4

    if position.is_integer():
        return data[int(position) - 1]

    lower_index = int(position) - 1
    upper_index = lower_index + 1
    weight = position - lower_index - 1

    return data[lower_index] + weight * (data[upper_index] - data[lower_index])


# From lines 15-21 of descriptive-statistics.ipynb imports
def skewness(data):
    """Calculate moment coefficient of skewness"""
    mu3 = central_moments(3, data)
    sigma = central_moments(2, data)**0.5
    return mu3 / sigma**3


def kurtosis(data):
    """Calculate excess kurtosis using moments"""
    mu4 = central_moments(4, data)
    sigma = central_moments(2, data)**0.5
    return (mu4 / sigma**4) - 3  # Subtract 3 for excess kurtosis


def pearson_skewness(data):
    mean_val = mean(data)
    median_val = median(data)
    sigma = central_moments(2, data)**0.5
    return 3 * (mean_val - median_val) / sigma


def bowley_skewness(data):
    q1 = n_quartile(sorted(data), 0.25)
    q3 = n_quartile(sorted(data), 0.75)
    median_val = median(data)
    return (q1 + q3 - 2*median_val) / (q3 - q1)


def standard_deviation(x):
    """Calculates the standard deviation of a list of numbers."""
    n = len(x)
    if n < 2:
        return 0  # Standard deviation is not defined for less than 2 data points

    mu = mean(x)
    return sqrt(sum([(i - mu) ** 2 for i in x]) / (n - 1))


def variance(x):
    """Population variance to match covariance changes"""
    n = len(x)
    if n < 1:
        return np.nan
    mean_x = mean(x)
    return sum((xi - mean_x)**2 for xi in x) / n


def coefficient_sd(x, mean_x):
    """Calculate the coefficient of standard deviation."""
    return standard_deviation(x) / mean_x


def coefficient_variation(x, mean_x):
    """Calculate the coefficient of variation as percentage."""
    return (standard_deviation(x) / mean_x) * 100


def midrange(x):
    """Calculate the midrange of a dataset."""
    return (largest(x) + smallest(x)) / 2


def iqr(x):
    """Calculate the interquartile range."""
    return n_quartile(x, 3) - n_quartile(x, 1)


def quartile_deviation(x):
    """Calculate the quartile deviation."""
    return iqr(x) / 2


def decile(data, n):
    """Calculate the nth decile."""
    if not 1 <= n <= 9:
        raise ValueError("n must be between 1 and 9")
    return percentile(data, n * 10)


def raw_moments(n, x):
    """Calculate the nth raw moment."""
    return sum(i ** n for i in x) / len(x)


def regression_slope(x, y):
    """Calculate regression slope."""
    return covariance(x, y) / variance(x) 


def r_squared(x, y):
    """Calculate R-squared value."""
    corr = correlation(x, y)
    return corr * corr


def covariance(x, y):
    """Calculates the covariance between two lists of numbers."""
    n = len(x)
    if n < 2 or n != len(y):
        return np.nan
    
    # Use population covariance (n instead of n-1) to match regression_slope
    mean_x = mean(x)
    mean_y = mean(y)
    return sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / n  # Changed to n


def percentile(data, p):
    """Calculates the p-th percentile of a sorted list of numbers."""
    data.sort()
    n = len(data)
    if not 0 <= p <= 100:
        raise ValueError("Percentile must be between 0 and 100")

    rank = (p / 100) * (n - 1)
    i = int(rank)
    decimal_part = rank - i

    if i == n - 1:
        return data[i]

    return data[i] + decimal_part * (data[i + 1] - data[i])


def z_score(x, value):
    """Calculates the z-score of a value in a list of numbers."""
    std_dev = standard_deviation(x)
    if std_dev == 0:
        return np.nan  # Z-score is not defined if standard deviation is zero

    mu = mean(x)
    return (value - mu) / std_dev


def confidence_interval(x, confidence=0.95):
    """Calculates the confidence interval for a list of numbers."""
    n = len(x)
    if n < 2:
        return np.nan, np.nan  # Confidence interval is not defined for less than 2 data points

    mu = mean(x)
    std_dev = standard_deviation(x)
    z = norm.ppf((1 + confidence) / 2)
    margin_of_error = z * (std_dev / sqrt(n))
    return mu - margin_of_error, mu + margin_of_error


def normal_pdf(x, mu, sigma):
    """Calculate normal probability density function."""
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)


def pmf(x, values, probabilities):
    """Calculate probability mass function."""
    if len(values) != len(probabilities):
        raise ValueError("Values and probabilities must have same length")
    if abs(sum(probabilities) - 1) > 1e-9:
        raise ValueError("Probabilities must sum to 1")

    for i, val in enumerate(values):
        if val == x:
            return probabilities[i]
    return 0


def cdf(x, data):
    """Calculate empirical cumulative distribution function."""
    data = sorted(data)
    n = len(data)
    count = sum(1 for value in data if value <= x)
    return count / n


def expected_value(values, probabilities=None):
    """Calculate expected value of a discrete distribution."""
    if probabilities is None:
        # If no probabilities given, assume uniform distribution
        probabilities = [1/len(values)] * len(values)
    return sum(x * p for x, p in zip(values, probabilities))


def chebyshev_inequality(k):
    """Calculate Chebyshev's inequality bound."""
    if k <= 0:
        raise ValueError("k must be positive")
    return 1 / (k * k)

def r_squared(x, y):
    """Calculates the R-squared value."""
    corr = correlation(x, y)
    return corr**2