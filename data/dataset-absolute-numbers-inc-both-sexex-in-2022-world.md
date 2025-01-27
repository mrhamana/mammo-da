# Dataset Documentation

## Overview
This project analyzes medical datasets to draw meaningful statistical insights. The primary focus is on breast cancer diagnosis data and global cancer statistics.

## Datasvets

### 1. Breast Cancer Diagnosis Data (`data.csv`)
- **Purpose**: Contains diagnostic measurements for breast cancer cases
- **Columns**:
  - `M`/`B`: Malignant (M) or Benign (B) classification
  - Numerical columns: Various diagnostic measurements (e.g., radius, texture, perimeter, etc.)
- **Usage**: Used in `functions.py` and `main.py` for statistical analysis and visualization

### 2. Global Cancer Statistics (`dataset-absolute-numbers-inc-both-sexes-in-2022-world.csv`)
- **Purpose**: Contains global cancer incidence data for 2022
- **Columns**:
  - `Label`: Cancer type
  - `Cancer code`: Unique identifier for cancer type
  - `Country code (ISO/UN)`: Numerical country code (900 = World)
  - `Alpha‑3 code`: ISO 3166-1 alpha-3 country code (N.A. for world data)
  - `Sex`: 0 = Both, 1 = Female, 2 = Male
  - `Type`: Data type indicator
  - `ASR (World)`: Age-Standardized Rate (World)
  - `Crude rate`: Crude incidence rate
  - `Cumulative risk`: Cumulative risk of cancer
  - `Total`: Total number of cases

## Statistical Tools
The project includes various statistical functions implemented in `functions.py`:
- Central tendency: `mean()`, `median()`
- Dispersion: `range()`, `coff_range()`
- Correlation analysis: `correlation()`
- Central moments: `central_moments()`
- Data visualization: Scatter plots using matplotlib

## Visualization: 
The project shows the data with appropriate parameters in:
- Bar graph (ordered)
- Central tendency 
- Skewness 

## Code References
The statistical analysis is performed using the following code: