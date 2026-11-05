import pandas as pd
import sqlite3

# 1. Load both validated data and quarantine data
df_golden = pd.read_csv("step6_validated.csv")
df_quarantine = pd.read_csv("step6_quarantine.csv")

print("--- [Step 7: Load to SQL Database Started] ---")

# Connect to SQLite database
db_name = "customer_master.db"
conn = sqlite3.connect(db_name)

# 2. Load golden records into 'golden_customers' table
df_golden.to_sql("golden_customers", conn, if_exists="replace", index=False)

# 3. Load quarantined records into 'quarantine_customers' table
df_quarantine.to_sql("quarantine_customers", conn, if_exists="replace", index=False)

print(f"Data successfully loaded into 'golden_customers' and 'quarantine_customers' tables in {db_name}.")

# Run a quick SQL query to verify the load
query_result = pd.read_sql("SELECT count(*) AS total_clean_customers FROM golden_customers", conn)
print("\n[SQL Verification Query Result]")
print(query_result)

# Close the database connection
conn.close()
print("\n Data Pipeline completed successfully!")