# Customer-Data-Quality-Pipeline

# Automated Data Quality Assessment Pipeline

## Project Goal
This project aims to build an automated data quality inspection pipeline for e-commerce customer data using **Python (Pandas)** and **SQL**. As a Data Steward, the goal is to identify and resolve data integrity issues that negatively impact marketing campaigns (e.g., high email bounce rates, duplicate coupon distributions).

## Tech Stack
- **Language:** Python 3
- **Libraries:** Pandas
- **Data Source:** Messy E-commerce Customer Data (CSV)

## Data Quality Dimensions Addressed
This script evaluates the dataset based on the DAMA-DMBOK data quality dimensions:
1. **Completeness:** Identifying missing values (Nulls) in critical fields like Email and Phone.
2. **Uniqueness:** Detecting and handling duplicate customer profiles.
3. **Validity:** Validating email formats and Regional Postcode structures.

## Progress & Results
- [x] Initial Repository & Project Setup
- [x] Step 1: Data Profiling & Missing Value Detection (In Progress)
- [ ] Step 2: Uniqueness & Duplicate Handling
- [ ] Step 3: Format Validation (Email & Postcode)
- [ ] Step 4: Final Data Quality Report Generation


## Data Quality Issues Identified (Step 1 Profiling)

During the initial data profiling phase, the following issues were discovered:
- **Completeness:** The `email`, `phone`, `last_purchase_item`, and `signup_date` columns contain missing values (Nulls).
- **Uniqueness:** Duplicated rows exist (e.g., multiple identical records for 'Sophie Turner').
- **Validity:** The `phone` column is incorrectly parsed as `float64` instead of a string due to the presence of Null values, corrupting the phone number format (e.g., losing the leading zero).

## Data Stewardship Principles Applied (Step 2 Cleaning)

During the Step 2 cleaning process, the following technical strategies were implemented to resolve data quality issues:
- **Raw Data Protection (SSOT):** The original dataset (`messy_customers.csv`) remains completely untouched to preserve the Single Source of Truth (SSOT). All cleaning tasks are performed on an isolated memory copy (`df_cleaned` via `.copy()`), guaranteeing zero risk of raw data corruption.
- **Targeted Missing Value Imputation:** Applied specific imputation strategies based on the context of each column, such as placeholder dates (`1900-01-01`) for `signup_date` and generic strings (`no_email@provided.com`, `Unknown`) to maintain data completeness without distorting facts.
- **Data Type Correction:** Resolved the `float64` corruption in the `phone` column. By temporarily filling Nulls with zeros, casting the column to integers (to remove decimal artifacts), and subsequently converting it to strings, the original structural integrity was recovered.
- **Conditional Formatting Recovery:** Utilized Pandas `.apply()` combined with `lambda` functions to dynamically evaluate and restore missing leading zeros (`0`) for valid phone numbers, while preserving the structural tags for missing data.