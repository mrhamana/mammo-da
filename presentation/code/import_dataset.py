import os
import pandas as pd

# Create the tables directory if it doesn't exist
tables_dir = 'presentation/tables'
os.makedirs(tables_dir, exist_ok=True)

# Load the Breast Cancer Cell Data and generate a LaTeX preview table
df_cell = pd.read_csv('data/breast-cancer-cell-data.csv')
sample_cell = df_cell.head(5)
sample_cell.to_latex(
    os.path.join(tables_dir, 'breast_cancer_cell_sample.tex'),
    index=False,
    escape=True
)

# Load the Global Cancer Data and generate a LaTeX preview table
df_global = pd.read_csv('data/cancers-global.csv')
sample_global = df_global.head(5)
sample_global.to_latex(
    os.path.join(tables_dir, 'cancers_global_sample.tex'),
    index=False,
    escape=True
)

# Load the Breast Cancer by Country Data and generate a LaTeX preview table
df_country = pd.read_csv('data/breast-country.csv')
sample_country = df_country.head(5)
sample_country.to_latex(
    os.path.join(tables_dir, 'breast_country_sample.tex'),
    index=False,
    escape=True
)

# Load the Breast Cancer Mortality Data and generate a LaTeX preview table
df_mortality = pd.read_csv('data/breast-continent-mort.csv')
sample_mortality = df_mortality.head(5)
sample_mortality.to_latex(
    os.path.join(tables_dir, 'breast_cancer_continent_mortality_sample.tex'),
    index=False,
    escape=True
)