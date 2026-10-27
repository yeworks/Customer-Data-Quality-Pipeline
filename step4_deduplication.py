import pandas as pd

# 1. Load the latest cleaned data from Step 2
df = pd.read_csv("step2_cleaned.csv")

print("--- [Step 4: Deduplication Started] ---")
print(f"Total initial records: {len(df)}")

# Identify duplicate records based on 'name' and 'phone' combination
# The 'subset' parameter restricts the duplicate check to specific columns.
exact_duplicates = df[df.duplicated(subset=['name', 'phone'])]
print(f"\nExact duplicates found (Name + Phone): {len(exact_duplicates)}")
print("\n[List of Duplicate Records]")
print(exact_duplicates)

# Remove duplicates, keeping only the first occurrence
df_deduped = df.drop_duplicates(subset=['name', 'phone'], keep='first').copy()

print(f"\nRecords remaining after deduplication: {len(df_deduped)}")

# Export the deduplicated data to a new CSV file
df_deduped.to_csv("step4_deduped.csv", index=False)
print("\n step4_deduped.csv successfully saved.")