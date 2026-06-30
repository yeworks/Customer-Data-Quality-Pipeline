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
3. **Validity:** Validating email formats and UK Postcode structures.

## Progress & Results
- [x] Initial Repository & Project Setup
- [ ] Step 1: Data Profiling & Missing Value Detection (In Progress)
- [ ] Step 2: Uniqueness & Duplicate Handling
- [ ] Step 3: Format Validation (Email & Postcode)
- [ ] Step 4: Final Data Quality Report Generation
