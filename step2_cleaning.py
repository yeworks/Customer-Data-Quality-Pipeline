import pandas as pd

df = pd.read_csv("messy_customers.csv")

# - Step 2: Uniqueness & Missing Values -

# Remove exact duplicate rows
df_cleaned = df.drop_duplicates().copy()
print("--- [After Dropping Duplicates] ---")
print(f"Total rows after cleaning: {len(df_cleaned)}")

# Fill missing 'last_purchase_item' with 'Unknown'
df_cleaned['last_purchase_item'] = df_cleaned['last_purchase_item'].fillna('Unknown')

# Verify the changes
print("\n--- [Updated Missing Values Count] ---")
print(df_cleaned.isnull().sum())