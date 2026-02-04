import pandas as pd
import sqlite3

def run_query(query_statement, sql_connection):
    """
    Executes a SQL query against the database and prints the results.
    
    Args:
        query_statement (str): The SQL query string to execute.
        sql_connection (sqlite3.Connection): The active SQLite database connection object.
    """
    print(query_statement)
    # Use pandas to read the SQL query results directly into a DataFrame
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)
