import numpy as np
from math import floor, ceil, sqrt
from scipy.stats import norm


def mean(x):
    return sum(x) / len(x)


def median(x):
    n = len(x)
    if n % 2 == 1:
        return x[n // 2]
    else:
        return (x[floor((n - 1) / 2)] + x[ceil((n - 1) / 2)]) / 2


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


def coff_range(x):
    num = largest(x) - smallest(x)
    den = largest(x) + smallest(x)

    return num / den


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


def skewness(x):
    num = central_moments(3, x)
    den = central_moments(2, x)**(3/2)
    return num/den


def kurtosis(x):
    num = central_moments(4, x)
    den = central_moments(2, x)**2
    return (num/den)-3


def standard_deviation(x):
    """Calculates the standard deviation of a list of numbers."""
    n = len(x)
    if n < 2:
        return 0  # Standard deviation is not defined for less than 2 data points

    mu = mean(x)
    return sqrt(sum([(i - mu) ** 2 for i in x]) / (n - 1))


def variance(x):
    """Calculates the variance of a list of numbers."""
    n = len(x)
    if n < 2:
        return 0  # Variance is not defined for less than 2 data points

    mu = mean(x)
    return sum([(i - mu) ** 2 for i in x]) / (n - 1)


def covariance(x, y):
    """Calculates the covariance between two lists of numbers."""
    n = len(x)
    if n < 2 or n != len(y):
        return np.nan  # Covariance is not defined for less than 2 data points or unequal lengths

    mean_x = mean(x)
    mean_y = mean(y)
    return sum([(x[i] - mean_x) * (y[i] - mean_y) for i in range(n)]) / (n - 1)


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
