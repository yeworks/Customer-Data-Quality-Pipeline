import pandas as pd

# 1. Load the standardized data from Step 5
df = pd.read_csv("step5_standardized.csv")

print("--- [Step 6: Business Rule Validation & Quarantine Started] ---")

# 2. Define business rule violation conditions (Avoid Data Distortion)
# Instead of distorting data with .abs() or resetting values to 0, 
# we isolate rows violating critical business rules (negative age or negative spending).
quarantine_mask = (df['age'] < 0) | (df['total_spent'] < 0)

# 3. Isolate invalid records into a quarantine dataframe for auditing
df_quarantine = df[quarantine_mask].copy()
df_quarantine['quarantine_reason'] = 'Invalid Business Rule (Negative Age or Total Spent)'
print(f" Quarantined records isolated: {len(df_quarantine)}")

# 4. Keep only clean records for the main pipeline (Golden Records)
df_clean = df[~quarantine_mask].copy()
print(f" Clean records retained: {len(df_clean)}")

# 5. Export both finalized datasets (Validated main data & Quarantine data)
df_clean.to_csv("step6_validated.csv", index=False)
df_quarantine.to_csv("step6_quarantine.csv", index=False)

print("\n step6_validated.csv and step6_quarantine.csv successfully saved.")