import sqlite3

def load_to_csv(data, target_file):
    data.to_csv(target_file, index=False)

def load_to_db(data, sql_connection, table_name):
    data.to_sql(table_name, sql_connection, if_exists='replace', index=False)
