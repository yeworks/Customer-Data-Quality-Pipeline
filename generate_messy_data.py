import pandas as pd
import numpy as np
from faker import Faker
import random

print("--- [Generating 1000 Rows of Messy Customer Data] ---")

# Initialize Faker for generating synthetic data
fake = Faker('en_US')

data = []

# Generate 1000 rows of clean, raw data one by one
for i in range(1000):
    name = fake.name()
    email = fake.email()
    phone = f"0{fake.random_number(digits=10, fix_len=True)}"
    postcode = fake.postcode()
    signup_date = fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d')
    status = random.choice(['active', 'ACTIVE', 'vip', 'V.I.P', 'inactive'])
    age = random.randint(18, 80)
    total_spent = round(random.uniform(10.0, 1500.0), 2)
    last_purchase_item = fake.word()

    data.append([name, email, phone, postcode, signup_date, status, age, total_spent, last_purchase_item])

df = pd.DataFrame(data, columns=['name', 'email', 'phone', 'postcode', 'signup_date', 'status', 'age', 'total_spent', 'last_purchase_item'])

# ---------------------------------------------------------
# 3. Injecting Messy Data 
# ---------------------------------------------------------

# Issue 1: Completeness - Inject Nulls randomly into 10% of the rows
for col in ['email', 'phone', 'signup_date', 'last_purchase_item']:
    df.loc[df.sample(frac=0.1).index, col] = np.nan

# Issue 2: Validity - Simulate the Pandas float64 corruption issue for phone numbers
df['phone'] = pd.to_numeric(df['phone'], errors='coerce')

# Issue 3: Validity (Business Rules) - Inject negative values for age and spending (5% each)
df.loc[df.sample(frac=0.05).index, 'age'] *= -1
df.loc[df.sample(frac=0.05).index, 'total_spent'] *= -1

# Issue 4: Validity (Format) - Break email formats (5%)
df.loc[df.sample(frac=0.05).index, 'email'] = "invalid_email_format.com"

# Issue 5: Standardization - Add trailing/leading whitespaces to postcodes
df['postcode'] = df['postcode'].apply(lambda x: f" {x} " if pd.notnull(x) else x)

# Issue 6: Uniqueness - Duplicate 50 random records and append them to the bottom
duplicates = df.sample(n=50)
df = pd.concat([df, duplicates], ignore_index=True)

# ---------------------------------------------------------

# 4. Export the generated dataset
df.to_csv("messy_customers.csv", index=False)
print("'messy_customers.csv' (1050 rows) successfully generated!")