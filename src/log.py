from datetime import datetime

def log_progress(message, log_file='logs/log_file.txt'): 
    """
    Logs a message with a timestamp to a specified log file.
    
    Args:
        message (str): The message describing the current stage or event.
        log_file (str): The path to the file where logs are appended.
    """
    timestamp_format = '%Y-%m-%d %H:%M:%S' # Year-Month-Day Hour-Minute-Second 
    now = datetime.now() # Get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    
    # Open the log file in append mode to keep history
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 
 