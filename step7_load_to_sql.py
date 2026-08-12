import pandas as pd
import sqlite3

# Load the final validated data from Step 6
df = pd.read_csv("step6_validated.csv")

print("--- [Step 7: Load to SQL Database Started] ---")

# Connect to SQLite database
db_name = "customer_master.db"
conn = sqlite3.connect(db_name)

# Load DataFrame into a SQL table named 'customers'
# if_exists='replace' will overwrite the table if we run this script again
df.to_sql("customers", conn, if_exists="replace", index=False)

print(f"Data successfully loaded into the 'customers' table in {db_name}.")

# Run a quick SQL query to verify the load (Optional)
query_result = pd.read_sql("SELECT count(*) AS total_clean_customers FROM customers", conn)
print("\n[SQL Verification Query Result]")
print(query_result)

# Close the database connection
conn.close()
print("\n Data Pipeline completed successfully!")