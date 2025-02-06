# mammo-da
This is an ongoing project that aims to use the dataset with the statistical tools to draw meaningful insights.

Authors:
1. Shiva Sagar Yadav
2. Aman Sapkota
3. Namit Adhikari
4. Saugat Khatiwada

# Statistical Measures and Concepts

## Descriptive Statistics

1.  **Mean:** $\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$
2.  **Median:** Middle value (sorted)
    *   Odd: $(n+1)/2$
    *   Even: Average of $n/2$ and $(n/2)+1$
3.  **Mode:** Most frequent value
4.  **Minimum/S:** $S = \min(x_1, x_2, ..., x_n)$
5.  **Maximum/L:** $L = \max(x_1, x_2, ..., x_n)$
6.  **Range:** $R = L - S$
7.  **Coefficient of Range:** $\frac{L - S}{L + S}$
8.  **MD Mean:** $\frac{1}{n} \sum_{i=1}^{n} |x_i - \bar{x}|$
9.  **MD Median:** $\frac{1}{n} \sum_{i=1}^{n} |x_i - \text{median}|$
10. **Standard Deviation:** $s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$
11. **Variance:** $s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$
12. **Coefficient of SD:** $\frac{s}{\bar{x}}$
13. **CV:** $\frac{s}{\bar{x}} \times 100\%$
14. **IQR:** $Q_3 - Q_1$
15. **QD:** $\frac{Q_3 - Q_1}{2}$
16. **Midrange:** $\frac{L + S}{2}$
17. **Quartiles:** $Q_1, Q_2, Q_3$
   *   Q1: 25th percentile
   *   Q2: 50th percentile (median)
   *   Q3: 75th percentile
18. **Deciles:** $D_1$ to $D_9$
19. **Percentiles:** $P_1$ to $P_{99}$

## Statistical Formulas

1.  **Central Moments ($\mu_r$):** $\mu_r = \frac{1}{n} \sum_{i=1}^{n} (x_i - A)^r$
2.  **Raw Moments ($\mu'_r$):** $\mu'_r = \frac{1}{n} \sum_{i=1}^{n} x_i^r$
3.  **Skewness (Moments):** $\gamma_1 = \frac{\mu_3}{\mu_2^{3/2}}$
4.   **Kurtosis (Percentiles):** $K = \frac{0.5(Q_3 - Q_1)}{P_{90} - P_{10}}$
5.  **Excess Kurtosis (Moments):** $\gamma_2 = \frac{\mu_4}{\mu_2^2} - 3$
6.  **Covariance:** $\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})$
7.  **Pearson Skewness:** $\frac{\bar{x} - \text{Mode}}{s}$ or $\frac{3(\bar{x} - \text{Median})}{s}$
8.  **Bowley Skewness:** $\frac{Q_3 + Q_1 - 2Q_2}{Q_3 - Q_1}$
9.  **Correlation:** $r = \frac{\text{Cov}(X, Y)}{s_X s_Y}$
10.  **Regression byx:** $b_{yx} = \frac{\text{Cov}(X,Y)}{\text{Var}(X)}$
11. **Regression bxy:** $b_{xy} = \frac{\text{Cov}(X,Y)}{\text{Var}(Y)}$
12. **Chebyshev's Inequality:** $P(|X-\mu| \geq k\sigma) \leq \frac{1}{k^2}$
13. **Normal PDF:** $f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2}(\frac{x - \mu}{\sigma})^2}$

## Statistical Concepts and Tools

1.  **PMF:** $P(X = x)$
2.  **PDF:** $f(x)$
3.  **CDF:** $F(x) = P(X \leq x)$
4. **Expected Value:** $E(X) = \sum xP(x)$ or $E(X) = \int xf(x)dx$
5. **Variance** $Var(X) = E[(X - E(X))^2]$
6.  **R-squared:** $R^2 = \frac{\text{Explained Variance}}{\text{Total Variance}}$

## Inferential Statistics
1.  **Regression Analysis** 

## Visualization tools:
1. **Histogram**
2. **Boxplots**
3. **Sorted Bar Graph**
4. **Normal graph**
5. **Scatter plot**
6. **Q-Q plot (Quantile-quantile plot)**
7. **Correlation Heatmap**

## Code Structure

The project includes the following key files:

*   `main.ipynb`: Jupyter Notebook containing the main analysis code.
*   `functions.py`: Python file containing statistical functions.
*   `extract_data.py`: Python file containing functions to extract data from the CSV files.
*   `graph.py`: Python file containing functions to generate graphs.

## How to Run

1.  Ensure you have Python and Jupyter Notebook installed.
2.  Clone the repository.
3.  Navigate to the project directory.
4.  Run `jupyter notebook main.ipynb` to open the notebook.
5.  Execute the cells in the notebook to perform the analysis.