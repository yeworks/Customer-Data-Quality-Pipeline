# Customer Data Quality Pipeline (Part 1)

## Project Goal
This project aims to build an automated data quality inspection pipeline for e-commerce customer data using **Python (Pandas)** and **SQL**. As a Data Steward, the goal is to identify and resolve data integrity issues that negatively impact marketing campaigns (e.g., high email bounce rates, duplicate coupon distributions).

## Tech Stack
- **Language:** Python 3
- **Libraries:** Pandas, Faker
- **Database:** SQLite
- **Data Source:** Messy E-commerce Customer Data (CSV)

## Data Quality Dimensions Addressed (DAMA-DMBOK)
This script evaluates the dataset based on the core data quality dimensions:
1. **Completeness:** Identifying and imputing missing values (Nulls) in critical fields.
2. **Uniqueness:** Detecting and handling duplicate customer profiles.
3. **Validity:** Validating formats (Email, Postcode) and business rules.

---

## Data Quality Pipeline Execution

### Step 1: Data Profiling (Issues Identified)
- **Completeness:** The `email`, `phone`, `last_purchase_item`, and `signup_date` columns contain missing values.
- **Uniqueness:** Duplicated rows exist (e.g., multiple identical records for the same customer).
- **Validity:** The `phone` column is incorrectly parsed as `float64` instead of a string due to Null values, corrupting the format (losing leading zeros).

### Step 2: Data Cleansing & Missing Value Imputation
- **Raw Data Protection (SSOT):** The original dataset remains untouched. All cleaning tasks are performed on an isolated memory copy (`df.copy()`), guaranteeing zero risk of raw data corruption.
- **Targeted Imputation:** Applied specific strategies based on context (e.g., `1900-01-01` for dates, `no_email@provided.com` for text) to maintain completeness without distorting facts.
- **Data Type Correction:** Resolved the `float64` corruption in the `phone` column by casting to integers and converting to strings, successfully recovering the original structural integrity and restoring missing leading zeros (`0`).

### Step 3: Format Validation & Standardization
- **Regex-based Validation:** Implemented Regular Expressions to create a strict validation pattern for email addresses. Emails failing the structural test were replaced with `invalid_format@provided.com`.
- **Postcode Standardization:** Removed whitespaces and converted to uppercase to ensure formatting consistency.

### Step 4: Data Deduplication
- **Identity Resolution:** Removed duplicate customer records utilizing a composite key of `name` and `phone` columns. Retained the first occurrence to prevent false merges of shared contact details.

### Step 5: Data Type & Category Standardization
- **Date Formatting:** Converted date strings to the ISO 8601 standard (`YYYY-MM-DD`) using `pd.to_datetime()`.
- **Category Normalization:** Applied Title Case to status categories to ensure consistent grouping and aggregation.

### Step 6: Business Rule Validation
- **Numeric Outlier Handling:** Corrected logical anomalies violating business rules, such as converting negative age inputs to absolute values and resetting invalid negative spending amounts to zero.

### Step 7: Load to Database
- **SQL Integration:** Loaded the finalized, golden record dataset into an SQLite database (`customer_master.db`) using Pandas `.to_sql()` for downstream SQL querying and analytics.

--

## Part 2: Data Quality Diagnostic Dashboard (Tableau)

### Dashboard Overview
- **Tool:** Tableau Desktop (`.twbx`)
- **Purpose:** Visualizes data quality diagnosis results from the pipeline, translating raw data defects into clear operational insights.

### Key Visualizations & Metrics
1. **Total Ingestion Volume (KPI Card):** Establishes the baseline dataset scope (`1,050 records`).
2. **Status Standardization Analysis:** Bar chart exposing text fragmentation and formatting inconsistencies (mixed casing like `active` vs `ACTIVE` and `V.I.P` vs `vip`), proving the necessity of standardization.
3. **Column-Level Null Analysis:** Utilizes custom calculated fields (`IF ISNULL(...) THEN 1 ELSE 0 END`) to isolate missing values, demonstrating that data quality defects are heavily concentrated in contact channels (`Email`, `Phone`) rather than mandatory fields (`Postcode`).

---

## How to Run
1. Run the Python pipeline script to generate the cleaned SQLite database (`customer_master.db`).
2. Open `Customer_Data_Quality_Dashboard.twbx` in Tableau to explore the diagnostic dashboard.