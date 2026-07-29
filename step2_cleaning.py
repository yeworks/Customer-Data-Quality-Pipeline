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

# Handle remaining missing values (email, signup_date)
df_cleaned['email'] = df_cleaned['email'].fillna('no_email@provided.com')
df_cleaned['signup_date'] = df_cleaned['signup_date'].fillna('1900-01-01') # Default placeholder date

# Fix 'phone' data type and format
# Fill NaN with 0, convert to int (to drop the float '.0'), then to string
df_cleaned['phone'] = df_cleaned['phone'].fillna(0).astype(int).astype(str)

# Restore the dropped leading zero for phone numbers (except for the missing ones we filled with '0')
df_cleaned['phone'] = df_cleaned['phone'].apply(lambda x: '0' + x if x != '0' else 'Unknown')

# Final verification for Step 2
print("\n--- [Final Missing Values Count for Step 2] ---")
print(df_cleaned.isnull().sum())

print("\n--- [Cleaned Data Preview] ---")
print(df_cleaned[['name', 'phone', 'email', 'signup_date']])