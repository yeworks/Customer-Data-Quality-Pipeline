import pandas as pd

# Load the deduplicated data from Step 4
df = pd.read_csv("step4_deduped.csv")

print("--- [Step 5: Data Standardization Started] ---")

# Date Standardization (Check if 'join_date' or similar column exists)
# pd.to_datetime() parses various date string formats into real Datetime objects.
# errors='coerce' handles completely broken text by turning it into NaT (Not a Time) / missing value.
if 'join_date' in df.columns:
    df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')
    
    # Convert back to a clean string format (YYYY-MM-DD) for uniform CSV export
    df['join_date'] = df['join_date'].dt.strftime('%Y-%m-%d')
    print("✅ 'join_date' successfully converted to YYYY-MM-DD format.")

# Categorical Standardization (Check if 'status' or 'membership' column exists)
# .str.title() capitalizes the first letter and lowercases the rest (e.g., 'ACTIVE', 'active' -> 'Active')
if 'status' in df.columns:
    df['status'] = df['status'].str.title()
    print("✅ 'status' categories successfully standardized (Title Case).")

# Export the finalized standardized data
df.to_csv("step5_standardized.csv", index=False)
print("\n✅ step5_standardized.csv successfully saved.")