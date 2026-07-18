import pandas as pd

# Load dataset
df = pd.read_csv('messy_customers.csv')

# Inspect the first few rows
print("--- [Data Preview] ---")
print(df.head())

# Check data types and overview
print("\n--- [Data Info] ---")
print(df.info())

# Count missing values per column
print("\n--- [Missing Values Count] ---")
print(df.isnull().sum())
