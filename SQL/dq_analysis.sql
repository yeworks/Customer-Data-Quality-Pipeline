-- =========================================================
-- Data Quality Diagnostic Queries (DAMA-DMBOK Compliant)
-- Target Database: SQLite (customer_master.db)
-- =========================================================

-- 1. Completeness Check: Verify null distribution and tracking flags
SELECT 
    COUNT(*) AS total_golden_records,
    SUM(CASE WHEN email IS NULL THEN 1 ELSE 0 END) AS null_email_count,
    SUM(CASE WHEN phone IS NULL THEN 1 ELSE 0 END) AS null_phone_count,
    SUM(CASE WHEN is_missing_email = 1 THEN 1 ELSE 0 END) AS flagged_missing_email
FROM golden_customers;

-- 2. Uniqueness Check: Detect duplicate profiles using composite keys
SELECT 
    name, 
    phone, 
    COUNT(*) AS duplicate_count
FROM golden_customers
GROUP BY name, phone
HAVING COUNT(*) > 1;

-- 3. Quarantine Audit: Analyze business rule violations
SELECT 
    quarantine_reason, 
    COUNT(*) AS quarantined_record_count,
    ROUND(CAST(COUNT(*) AS REAL) / (SELECT COUNT(*) FROM quarantine_customers) * 100, 2) AS percentage
FROM quarantine_customers
GROUP BY quarantine_reason;

-- 4. Status Analysis: Customer distribution and total spent by status
SELECT 
    status,
    COUNT(*) AS customer_count,
    ROUND(AVG(total_spent), 2) AS avg_spent,
    SUM(total_spent) AS total_revenue
FROM golden_customers
GROUP BY status
ORDER BY total_revenue DESC;