import pandas as pd

# 1. Load the standardized data from Step 5
df = pd.read_csv("step5_standardized.csv")

print("--- [Step 6: Business Rule Validation Started] ---")

# 2. Check for logical errors in numeric columns (e.g., age)
if 'age' in df.columns:
    # Filtering abnormal data where age is less than 0
    invalid_age = df[df['age'] < 0]
    print(f" Negative age records found: {len(invalid_age)}")
    
    # Assume a typing error (entering -25 instead of 25) and force conversion to the absolute value.
    df['age'] = df['age'].abs()
    print(" Negative ages successfully converted to positive (Absolute value).")

# 3. Check for invalid prices or spending (e.g., total_spent)
if 'total_spent' in df.columns:
    invalid_spend = df[df['total_spent'] < 0]
    print(f" Negative spending records found: {len(invalid_spend)}")
    
    # Negative purchase amounts may indicate issues such as refunds, 
    # but for the sake of analysis, they are uniformly reset to 0 (or can be treated as missing values).
    df.loc[df['total_spent'] < 0, 'total_spent'] = 0
    print(" Negative spending successfully reset to 0.")

# 4. Export the finalized validated data
df.to_csv("step6_validated.csv", index=False)
print("\n step6_validated.csv successfully saved.")