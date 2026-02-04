# Lab 1: ETL Pipeline for Used Car Data

## Overview
This project implements a basic **ETL (Extract, Transform, Load)** pipeline using Python. It processes used car sales data from multiple formats (**CSV, JSON, and XML**), standardizes the information, and loads it into a **SQLite database** and a **CSV file** for analysis.

## Project Structure
```text
ETL_Lab_1/
│
├── data/
│   ├── raw/                  # Source files (.csv, .json, .xml)
│   └── transformed/          # Output file (transformed_data.csv)
│
├── logs/                     # Execution logs (log_file.txt)
│
├── src/                      # Source code
│   ├── extract.py            # Data extraction logic
│   ├── transform.py          # Data cleaning and standardization
│   ├── load.py               # Saving to CSV and SQLite
│   ├── log.py                # Logging utility
│   ├── db.py                 # Database query utility
│   └── main.py               # Main execution script
│
├── etl_database.db           # SQLite database
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Setup & Execution

1. **Install Dependencies:**
   Make sure your virtual environment is active and run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the ETL Pipeline:**
   Execute the main script:
   ```bash
   python src/main.py
   ```
   This will run the ETL process stages (Extract -> Transform -> Load) and then open an interactive query menu.

## Features
- **Extraction:** Robust handling of CSV, JSON (both Line-delimited and Arrays), and XML files.
- **Transformation:** Standardizes vehicle prices (numeric conversion) and rounds them to 2 decimal places.
- **Loading:** Persists data to `data/transformed/transformed_data.csv` and the `vehicles` table in `etl_database.db`.
- **Querying:** Interactive CLI menu to inspect and filter the loaded data.

## Reflection Questions (Deliverable 11)

**1. What is the role of each ETL stage in this laboratory?**
*   **Extraction:** Unifies data from heterogeneous sources (CSV, JSON, and XML) into a single tabular format.
*   **Transformation:** Standardizes the data quality by ensuring prices are numeric and rounded to 2 decimal places.
*   **Loading:** Saves the final result into persistent storage (CSV and SQLite) for future querying and reporting.

**2. What problems could arise if the transformation step is skipped?**
If skipped, the dataset would be inconsistent. Prices might have varying decimal precision or incorrect data types (like strings from the XML file), which would prevent accurate mathematical calculations or data aggregations.

**3. Why is it useful to load data into a database instead of keeping multiple raw files?**
A database provides structured storage that allows for fast SQL queries, efficient data filtering, and the ability for multiple users or applications to access the data simultaneously without manual file parsing.

**4. How does this ETL pipeline support future analytics or AI tasks?**
This pipeline provides clean, structured, and reliable data. This "clean state" is the critical first step for training Machine Learning models or performing advanced predictive analytics, as AI models require high-quality numerical input.