# Customer Data Quality Pipeline (Part 1)

## Project Goal
This project aims to build an automated data quality inspection pipeline for e-commerce customer data using **Python (Pandas)** and **SQL**. As a Data Steward, the goal is to identify and resolve data integrity issues that negatively impact marketing campaigns (e.g., high email bounce rates, duplicate coupon distributions) while strictly adhering to **DAMA-DMBOK** data governance standards.

## Tech Stack
- **Language:** Python 3
- **Libraries:** Pandas, Faker
- **Database:** SQLite
- **Data Source:** Messy E-commerce Customer Data (CSV - Synthetic Data)

---

## Data Quality Dimensions Addressed (DAMA-DMBOK)
This pipeline evaluates and processes the dataset based on core data quality dimensions:
1. **Completeness:** Preserving raw NULL values and introducing boolean tracking flags instead of arbitrary data imputation.
2. **Uniqueness:** Detecting and resolving duplicate customer profiles using composite keys.
3. **Validity:** Implementing regex format checks and isolating business rule violations into a quarantine audit table.

---

## Data Quality Pipeline Execution

### Step 1: Data Profiling (Issues Identified)
- **Completeness:** The `email`, `phone`, `last_purchase_item`, and `signup_date` columns contain missing values.
- **Uniqueness:** Duplicated rows exist (multiple identical records for the same customer profile).
- **Validity:** The `phone` column is incorrectly parsed as `float64` due to Null values, corrupting the format (losing leading zeros). Negative age and spending anomalies exist.

### Step 2: Completeness & Tracking Flags (Avoiding Data Distortion)
- **Raw Data Protection (SSOT):** The original dataset remains untouched (`df.copy()`). 
- **Flag Column Generation:** Instead of imputing arbitrary placeholder values (which causes data distortion), we preserve NULLs and introduce explicit tracking flags (`is_missing_email`, `is_missing_signup_date`) to maintain complete auditability.
- **Data Type Correction:** Resolved `float64` corruption in the `phone` column by casting and string-formatting to successfully restore missing leading zeros (`0`).

### Step 3: Format Standardization
- **Postcode Standardization:** Removed whitespaces and converted text to uppercase to ensure formatting consistency across regional entries.

### Step 4: Data Deduplication (Uniqueness)
- **Identity Resolution:** Removed duplicate customer records utilizing a composite key of `name` and `phone` columns, retaining the first occurrence.

### Step 5: Category & Date Standardization
- **Date Formatting:** Converted date strings to the ISO 8601 standard (`YYYY-MM-DD`) using `pd.to_datetime()`.
- **Category Normalization:** Applied Title Case to status categories to ensure consistent grouping and aggregation.

### Step 6: Business Rule Validation & Quarantine Isolation
- **Quarantine Mechanism:** Rather than arbitrarily modifying or distorting invalid records (e.g., converting negative ages to absolute values), rows violating critical business rules (`Age < 0` or `Total Spent < 0`) are safely isolated into a **Quarantine Table** for auditing. Only clean records pass through to the main pipeline.

### Step 7: Load to SQLite Database
- **Dual-Table SQL Integration:** Loaded the finalized, clean dataset into the **`golden_customers`** table, and isolated invalid records into the **`quarantine_customers`** table within an SQLite database (`customer_master.db`) using Pandas `.to_sql()`.

---

## Data Quality Performance (Before vs. After)

| DQ Dimension | Issue Identified (Before) | Resolution Action (DAMA-DMBOK Compliant) | Impact / Metric |
| **Completeness** | Missing emails & signup dates | Preserved NULLs + Added tracking flags | 100% factual integrity (Zero data distortion) |
| **Validity** | Negative age & spending anomalies | Isolated invalid rows into Quarantine Table | 0 corrupt records in Golden Master |
| **Uniqueness** | Duplicate customer profiles | Composite key (`Name`, `Phone`) deduplication | Eliminated redundant profile records |

---

## Part 2: Data Quality Diagnostic Dashboard (Tableau)

### Dashboard Overview
- **Tool:** Tableau Desktop (`.twbx`)
- **Purpose:** Visualizes data quality diagnosis results, translating raw data defects into clear operational insights.

### Key Visualizations & Metrics
1. **Total Ingestion Volume (KPI Card):** Establishes the baseline dataset scope (`1,050 records`).
2. **Status Standardization Analysis:** Bar chart exposing text fragmentation and formatting inconsistencies (`active` vs `ACTIVE`), proving the necessity of standardization.
3. **Column-Level Null Analysis:** Utilizes custom calculated fields (`IF ISNULL(...) THEN 1 ELSE 0 END`) to isolate missing values, demonstrating that data quality defects are concentrated in contact channels (`Email`, `Phone`).

---

## How to Run
1. Run the Python pipeline script to generate the SQLite database (`customer_master.db`) containing both `golden_customers` and `quarantine_customers`.
2. Open `Customer_Data_Quality_Dashboard.twbx` in Tableau to explore the diagnostic dashboard.