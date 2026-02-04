import pandas as pd

def transform(data):
    """
    Transforms the extracted data.
    1. Converts the 'price' column to numeric, handling errors.
    2. Rounds the 'price' to 2 decimal places.
    """
    
    # Convert 'price' column to numeric to handle any strings from XML or CSV sources
    # 'errors=coerce' turns unparseable values (like 'N/A' or empty strings) into NaN (Not a Number)
    # This prevents the script from crashing due to dirty data.
    data['price'] = pd.to_numeric(data['price'], errors='coerce')
    
    # Round the price to 2 decimal places as per requirements
    data['price'] = data['price'].round(2)
    
    return data