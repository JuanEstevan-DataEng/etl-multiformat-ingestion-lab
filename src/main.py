import sqlite3
import os
from log import log_progress
from extract import extract
from transform import transform
from load import load_to_csv, load_to_db
from db import run_query

def main():
    # 1. Path Configuration
    
    # Get the absolute path of the directory where this script (main.py) is located
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the project root (ETL_Lab_1/)
    project_root = os.path.dirname(base_path)

    # Define paths relative to the project root to ensure portability
    log_file = os.path.join(project_root, "logs", "log_file.txt")
    target_file = os.path.join(project_root, "data", "transformed", "transformed_data.csv")
    data_path = os.path.join(project_root, "data", "raw")
    db_name = 'etl_database.db'
    db_path = os.path.join(project_root, db_name)
    table_name = 'vehicles'

    # Create necessary directories if they do not exist
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    os.makedirs(os.path.dirname(target_file), exist_ok=True)

    # Log the initialization of the ETL process 
    log_progress("ETL Job Started", log_file) 
    
    # 2. Extraction Phase
    log_progress("Extract phase Started", log_file) 
    extracted_data = extract(data_path)
    log_progress("Data extraction complete.", log_file)
    
    # 3. Transformation Phase
    log_progress("Transform phase Started", log_file) 
    transformed_data = transform(extracted_data)
    log_progress("Data transformation complete.", log_file)

    # 4. Loading Phase
    
    # Load to CSV
    log_progress("Load phase Started", log_file)
    load_to_csv(transformed_data, target_file)
    log_progress("Data loaded to CSV.", log_file)

    # Load to Database
    # Connect to the SQLite database using the absolute path
    sql_connection = sqlite3.connect(db_path)
    load_to_db(transformed_data, sql_connection, table_name)
    log_progress('Data loaded to Database as table. Running the query', log_file)

    # 5. Query Menu
    while True:
        print("\n--- Query Menu ---")
        print("1. Display all cars")
        print("2. Display brand, model, year, and price of vehicles manufactured after 2015")
        print("3. Count vehicles by fuel type")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Run query to select all records
            run_query(f"SELECT * FROM {table_name}", sql_connection)
        elif choice == '2':
            # Run query with a WHERE clause
            run_query(f"SELECT car_model, year_of_manufacture, price FROM {table_name} WHERE year_of_manufacture > 2015", sql_connection)
        elif choice == '3':
            # Run aggregation query
            run_query(f"SELECT fuel, COUNT(*) as count FROM {table_name} GROUP BY fuel", sql_connection)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    # Close the database connection
    sql_connection.close()

if __name__ == "__main__":
    main()
