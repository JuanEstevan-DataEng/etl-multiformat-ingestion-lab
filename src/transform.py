import pandas as pd

def transform(data):
    """
    Transforms the extracted data.
    1. Concatenates the list of DataFrames into a single DataFrame.
    2. Selects only relevant columns.
    3. Converts the 'price' column to numeric, handling errors.
    4. Rounds the 'price' to 2 decimal places.
    """
    # Check if data is a list (from the new extract logic) and concatenate
    if isinstance(data, list):
        if not data:
            return pd.DataFrame()
        data = pd.concat(data, ignore_index=True)

    # Select specific columns to ensure schema consistency
    data = data[['car_model', 'year_of_manufacture', 'price', 'fuel']]

    # Convert 'price' column to numeric to handle any strings from XML or CSV sources
    # 'errors=coerce' turns unparseable values (like 'N/A' or empty strings) into NaN (Not a Number)
    # This prevents the script from crashing due to dirty data.
    data['price'] = pd.to_numeric(data['price'], errors='coerce')
    
    # Round the price to 2 decimal places as per requirements
    data['price'] = data['price'].round(2)
    
    return data