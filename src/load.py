import sqlite3

def load_to_csv(data, target_file):
    """
    Saves the transformed DataFrame to a CSV file.
    
    Args:
        data (pd.DataFrame): The transformed data to be saved.
        target_file (str): The destination file path for the CSV.
    """
    data.to_csv(target_file, index=False)

def load_to_db(data, sql_connection, table_name):
    """
    Loads the transformed DataFrame into a specified SQLite table.
    If the table already exists, it will be replaced.
    
    Args:
        data (pd.DataFrame): The transformed data to be loaded.
        sql_connection (sqlite3.Connection): The active SQLite database connection object.
        table_name (str): The name of the table where data will be stored.
    """
    data.to_sql(table_name, sql_connection, if_exists='replace', index=False)
