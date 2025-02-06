import os
import pandas as pd

# Create the tables directory if it doesn't exist
tables_dir = 'presentation/tables'
os.makedirs(tables_dir, exist_ok=True)

# Load the Breast Cancer by Country Data and generate a LaTeX preview table
df_country = pd.read_csv('data/breast-country.csv')
sample_country = df_country.head(5)
sample_country.to_latex(
    os.path.join(tables_dir, 'breast_country_sample.tex'),
    index=False,
    escape=True
)