# Detailed Statistical Analysis Plan for Breast Cancer Datasets

This document outlines a detailed plan for performing statistical analysis on four breast cancer-related datasets using the implemented statistical tools, measures, and visualizations. The plan ensures that all available tools are utilized at least once on appropriate columns across the datasets.

## Dataset 1: `breast-cancer-cell-data.csv` (Breast Cancer Cell Features)

**Description:** This dataset contains features extracted from images of breast cancer cells. It includes numerical features describing cell nuclei characteristics and a categorical diagnosis label (Benign/Malignant).

**Columns to Analyze:**
*   **Numerical Features (Example Columns):** `radius_mean`, `texture_mean`, `perimeter_mean`, `area_mean`, `smoothness_mean`, `compactness_mean`, `concavity_mean`, `concave points_mean`, `symmetry_mean`, `fractal_dimension_mean`, and their `_se` and `_worst` counterparts.
*   **Categorical Feature:** `diagnosis` (or similar label column).

**Analysis Plan:**

1.  **Descriptive Statistics for Numerical Features (e.g., `radius_mean`):**
    *   **Tools & Measures:** `mean`, `median`, `mode`, `minimum` (smallest), `maximum` (largest), `range` (using `largest - smallest`), `coff_range` (Coefficient of Range), `mean_dev` (MD Mean), `mean_dev_median` (MD Median), `standard_deviation`, `variance`, `coefficient_sd` (Coefficient of SD), `coefficient_variation` (CV), `iqr` (IQR), `quartile_deviation` (QD), `midrange`, `n_quartile` (Quartiles - Q1, Q2, Q3), `decile` (Deciles - e.g., D1, D9), `percentile` (Percentiles - e.g., P1, P99).
    *   **Purpose:** Understand the central tendency, spread, and range of cell nucleus radius.

2.  **Distribution Visualization for Numerical Features (e.g., `texture_mean`):**
    *   **Visualization Tools:** `histo_graph` (Histogram), `normal_graph` (Normal Distribution Plot), `qq_plot` (Q-Q plot), `estimate_pdf` (using `normal_pdf` for PDF estimation).
    *   **Purpose:** Visualize the distribution shape of cell texture and assess if it approximates a normal distribution.

3.  **Boxplot Analysis for Numerical Features (e.g., all `_mean` features):**
    *   **Visualization Tool:** `boxplot` (Boxplots).
    *   **Purpose:** Compare the distributions of multiple `_mean` features side-by-side, identify potential outliers, and visualize quartiles and median.

4.  **Skewness and Kurtosis Analysis (e.g., `smoothness_mean`):**
    *   **Tools & Measures:** `skewness` (Coefficient of Skewness - Moments), `kurtosis` (Excess Kurtosis - Moments), `pearson_skewness` (Pearson Skewness), `bowley_skewness` (Bowley Skewness).
    *   **Purpose:** Quantify the asymmetry and peakedness of the distribution of cell smoothness. Compare different skewness measures.

5.  **Moments Analysis (e.g., `compactness_mean`):**
    *   **Tools & Measures:** `central_moments` (Central Moments - e.g., 3rd and 4th order), `raw_moments` (Raw Moments - e.g., 2nd order).
    *   **Purpose:** Calculate higher-order moments to further characterize the shape of the distribution of cell compactness.

6.  **Correlation Analysis (e.g., `radius_mean` vs. `perimeter_mean` and all `_mean` features):**
    *   **Tools & Measures:** `correlation` (Correlation Coefficient), `covariance` (Covariance), `correlation_heatmap` (Correlation Heatmap).
    *   **Visualization Tool:** `scatter_plot` (Scatter plot) for specific pairs.
    *   **Purpose:** Explore the linear relationships between cell radius and perimeter, and visualize the correlation matrix for all `_mean` features to identify feature dependencies.

7.  **Regression Analysis (e.g., Predict `perimeter_mean` from `radius_mean`):**
    *   **Tools & Measures:** `regression_slope` (Regression Slope), `y_intercept` (Y-intercept), `r_squared` (R-squared).
    *   **Purpose:** Model the linear relationship between cell radius and perimeter and quantify the goodness of fit of the linear model.

8.  **Categorical Data Analysis (`diagnosis`):**
    *   **Tools & Measures:** `mode` (Mode).
    *   **Visualization Tool:** `bar_graph_sorted` (Sorted Bar Graph).
    *   **Purpose:** Determine the most frequent diagnosis category and visualize the distribution of diagnoses (Benign vs. Malignant).

## Dataset 2: `cancers_global_sample_part*.tex` (Global Cancer Statistics)

**Description:** This dataset contains global cancer statistics, potentially including cancer types, regions, and numerical data like cases or mortality rates.

**Columns to Analyze (Example Columns - Adapt to actual column names):**
*   **Categorical:** `Country`, `Region`, `Cancer_Type`.
*   **Numerical:** `Number_of_Cases`, `Mortality_Rate`.

**Analysis Plan:**

1.  **Descriptive Statistics for Global Mortality Rates (`Mortality_Rate`):**
    *   **Tools & Measures:** `mean`, `median`, `standard_deviation`, `variance`, `range`, `iqr`, `percentile` (e.g., P90).
    *   **Purpose:** Understand the distribution of cancer mortality rates globally.

2.  **Visualization of Global Mortality Rates:**
    *   **Visualization Tools:** `histo_graph`, `boxplot`.
    *   **Purpose:** Visualize the distribution of global mortality rates and identify potential outliers (countries with very high or low rates).

3.  **Sorted Bar Graph for Cancer Types (`Cancer_Type` and `Number_of_Cases`):**
    *   **Visualization Tool:** `bar_graph_sorted` (Sorted Bar Graph).
    *   **Purpose:** Visualize the number of cases for different cancer types, sorted to easily see the most and least frequent cancers globally.

4.  **Mode of Regions (`Region`):**
    *   **Tools & Measures:** `mode`.
    *   **Purpose:** Find the most frequently represented region in the dataset.

## Dataset 3: `breast_country_sample_part*.tex` (Breast Cancer Statistics by Country)

**Description:** This dataset focuses specifically on breast cancer statistics, broken down by country.

**Columns to Analyze (Example Columns - Adapt to actual column names):**
*   **Categorical:** `Country`.
*   **Numerical:** `Breast_Cancer_Incidence_Rate`, `Breast_Cancer_Mortality_Rate`.

**Analysis Plan:**

1.  **Descriptive Statistics for Breast Cancer Incidence Rates (`Breast_Cancer_Incidence_Rate`):**
    *   **Tools & Measures:** `mean`, `median`, `coefficient_variation`, `midrange`, `decile` (e.g., D5 - median decile).
    *   **Purpose:** Analyze the central tendency and variability of breast cancer incidence rates across countries.

2.  **Boxplot of Breast Cancer Mortality Rates (`Breast_Cancer_Mortality_Rate`):**
    *   **Visualization Tool:** `boxplot`.
    *   **Purpose:** Visualize the distribution of breast cancer mortality rates across countries and identify countries with particularly high or low mortality.

3.  **Sorted Bar Graph for Countries by Mortality Rate (`Country` and `Breast_Cancer_Mortality_Rate`):**
    *   **Visualization Tool:** `bar_graph_sorted`.
    *   **Purpose:** Rank countries by breast cancer mortality rate, allowing for easy comparison and identification of countries with the highest and lowest rates.

## Dataset 4: `breast_cancer_continent_mortality_sample_part*.tex` (Breast Cancer Mortality by Continent)

**Description:** This dataset focuses on breast cancer mortality rates, aggregated by continent.

**Columns to Analyze (Example Columns - Adapt to actual column names):**
*   **Categorical:** `Continent`.
*   **Numerical:** `Breast_Cancer_Mortality_Rate`.

**Analysis Plan:**

1.  **Descriptive Statistics for Breast Cancer Mortality Rates by Continent (`Breast_Cancer_Mortality_Rate`):**
    *   **Tools & Measures:** `mean`, `median`, `range`, `mean_dev`, `quartile_deviation`, `coefficient_sd`.
    *   **Purpose:** Analyze the central tendency and spread of breast cancer mortality rates across continents.

2.  **Bar Graph for Continent Mortality Rates (`Continent` and `Breast_Cancer_Mortality_Rate`):**
    *   **Visualization Tool:** `bar_graph_sorted`.
    *   **Purpose:** Compare breast cancer mortality rates across different continents visually.

3.  **Mode of Continents (`Continent`):**
    *   **Tools & Measures:** `mode`.
    *   **Purpose:** Determine the most frequently listed continent (though this might not be very informative in this specific dataset, it fulfills the requirement of using 'mode').

**Note:**

*   Adapt column names in this plan to match the actual column names in your CSV files.
*   Ensure data is loaded and preprocessed correctly before applying these analyses.
*   Focus on interpreting the results and drawing meaningful conclusions from the statistical measures and visualizations.