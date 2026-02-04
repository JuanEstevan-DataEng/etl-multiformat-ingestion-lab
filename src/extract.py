import pandas as pd
import glob
import os

def extract_from_csv(file_to_process):
    """
    Extracts data from a CSV file.
    Includes error handling to skip corrupted files.
    """
    try:
        dataframe = pd.read_csv(file_to_process)
        return dataframe
    except Exception as e:
        print(f"Error reading CSV file {file_to_process}: {e}")
        return pd.DataFrame()

def extract_from_json(file_to_process):
    """
    Extracts data from a JSON file.
    Attempts to read as JSON Lines (lines=True) first, 
    then falls back to standard JSON.
    """
    try:
        # Try reading as JSON Lines (common in Big Data)
        dataframe = pd.read_json(file_to_process, lines=True)
        return dataframe
    except ValueError:
        try:
            # Fallback: Try reading as a standard JSON array
            dataframe = pd.read_json(file_to_process)
            return dataframe
        except Exception as e:
            print(f"Error reading JSON file {file_to_process}: {e}")
            return pd.DataFrame()
    except Exception as e:
        print(f"Error processing JSON file {file_to_process}: {e}")
        return pd.DataFrame()

def extract_from_xml(file_to_process):
    """
    Extracts data from an XML file using pandas read_xml.
    """
    try:
        dataframe = pd.read_xml(file_to_process)
        return dataframe
    except Exception as e:
        print(f"Error reading XML file {file_to_process}: {e}")
        return pd.DataFrame()

def extract(path):
    """
    Main extraction function.
    Iterates through all CSV, JSON, and XML files in the specified path,
    extracts data, and concatenates it into a single DataFrame.
    """
    dataframes = []
    
    # Process all CSV files
    for csv_file in glob.glob(os.path.join(path, "*.csv")):
        dataframes.append(extract_from_csv(csv_file))
        
    # Process all JSON files
    for json_file in glob.glob(os.path.join(path, "*.json")):
        dataframes.append(extract_from_json(json_file))
        
    # Process all XML files
    for xml_file in glob.glob(os.path.join(path, "*.xml")):
        dataframes.append(extract_from_xml(xml_file))
        
    if not dataframes:
        return []
        
    return dataframes
