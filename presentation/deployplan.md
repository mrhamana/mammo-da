# Detailed Statistical Analysis Plan for Breast Cancer Statistics by Country

This document outlines a detailed plan for performing statistical analysis on the `breast-country.csv` dataset using the implemented statistical tools, measures, and visualizations. The plan ensures that all available tools are utilized at least once on appropriate columns across the dataset.

## Dataset: `breast-country.csv` (Breast Cancer Statistics by Country)

**Description:** This dataset provides breast cancer statistics for individual countries.

**Columns to Analyze:**

*   **Categorical:** `Cancer label`, `Population code (ISO/UN)`, `Alpha-3 code`
*   **Numerical:** `ASR (World) per 100 000`

**Analysis Plan:**

1.  **Descriptive Statistics for ASR (World) per 100 000:**
    *   **Tools & Measures:** `mean`, `median`, `mode`, `minimum` (smallest), `maximum` (largest), `range` (using `largest - smallest`), `coff_range` (Coefficient of Range), `mean_dev` (MD Mean), `mean_dev_median` (MD Median), `standard_deviation`, `variance`, `coefficient_sd` (Coefficient of SD), `coefficient_variation` (CV), `iqr` (IQR), `quartile_deviation` (QD), `midrange`, `n_quartile` (Quartiles - Q1, Q2, Q3), `decile` (Deciles - e.g., D1, D9), `percentile` (Percentiles - e.g., P1, P99).
    *   **Purpose:** Understand the central tendency, spread, and range of breast cancer rates across countries.

2.  **Distribution Visualization for ASR (World) per 100 000:**
    *   **Visualization Tools:** `histo_graph` (Histogram), `normal_graph` (Normal Distribution Plot), `qq_plot` (Q-Q plot), `estimate_pdf` (using `normal_pdf` for PDF estimation).
    *   **Purpose:** Visualize the distribution shape of breast cancer rates and assess if it approximates a normal distribution.

3.  **Skewness and Kurtosis Analysis for ASR (World) per 100 000:**
    *   **Tools & Measures:** `skewness` (Coefficient of Skewness - Moments), `kurtosis` (Excess Kurtosis - Moments), `pearson_skewness` (Pearson Skewness), `bowley_skewness` (Bowley Skewness).
    *   **Purpose:** Quantify the asymmetry and peakedness of the distribution of breast cancer rates. Compare different skewness measures.

4.  **Moments Analysis for ASR (World) per 100 000:**
    *   **Tools & Measures:** `central_moments` (Central Moments - e.g., 3rd and 4th order), `raw_moments` (Raw Moments - e.g., 2nd order).
    *   **Purpose:** Calculate higher-order moments to further characterize the shape of the distribution of breast cancer rates.

5.  **Categorical Data Analysis (`Cancer label`):**
    *   **Tools & Measures:** `mode` (Mode).
    *   **Visualization Tool:** `bar_graph_sorted` (Sorted Bar Graph).
    *   **Purpose:** Determine the most frequent cancer label and visualize its distribution.

6. **Correlation Analysis (if applicable - requires another numerical column):**
    *   Since we primarily have one numerical column (`ASR (World) per 100 000`), correlation analysis within this dataset is limited.  If you were to merge this data with another dataset containing numerical features *per country*, you could then perform correlation analysis.  For example, if you had a "GDP per capita" column, you could analyze the correlation between GDP and `ASR (World)`.
    *   **Example (Hypothetical):**  `ASR (World)` vs. `GDP per capita`
    *   **Tools & Measures:** `correlation` (Correlation Coefficient), `covariance` (Covariance), `correlation_heatmap` (Correlation Heatmap).
    *   **Visualization Tool:** `scatter_plot` (Scatter plot) for specific pairs.
    *   **Purpose:** Explore the linear relationships between breast cancer rates and other potential factors (if available in a merged dataset).

7. **Regression Analysis (if applicable - requires another numerical column):**
    *   Similar to correlation analysis, regression analysis requires at least two numerical columns.
    *   **Example (Hypothetical):** Predict `ASR (World)` from `GDP per capita` (from a merged dataset).
    *   **Tools & Measures:** `regression_slope` (Regression Slope), `y_intercept` (Y-intercept), `r_squared` (R-squared).
    *   **Purpose:** Model the linear relationship and quantify the goodness of fit.

**Note:**
*   Ensure data is loaded and preprocessed correctly before applying these analyses.
*   Focus on interpreting the results and drawing meaningful conclusions from the statistical measures and visualizations.