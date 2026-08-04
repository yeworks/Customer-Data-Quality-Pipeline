import pandas as pd
import re

# Load the data from Step 2
df = pd.read_csv("step2_cleaned.csv")

print("--- [Step 3: Format Validation] ---")

# Email Validation using Regex (Regular Expression)
# Pattern: something @ something . something
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

def validate_email(email):
    # If it's our placeholder, leave it alone
    if email == 'no_email@provided.com':
        return email
    # If it matches the email pattern, keep it
    if re.match(email_pattern, str(email)):
        return email
    # If it fails the test, mark as invalid
    else:
        return 'invalid_format@provided.com'

# Apply the validation rule to the email column
df['email'] = df['email'].apply(validate_email)