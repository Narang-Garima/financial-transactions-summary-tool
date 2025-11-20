import pandas as pd
import os
from typing import Optional

def load_data(file_path: str) -> Optional[pd.DataFrame]:
    """
    Loads financial transaction data from a CSV file into a pandas DataFrame.

    The function handles potential FileNotFoundError exceptions as required by
    the Acceptance Criteria.

    Args:
        file_path: The full path to the CSV file.

    Returns:
        A pandas DataFrame containing the loaded data, or None if the file 
        cannot be loaded.
    """
    # Check if the file exists first, addressing the "Handles missing or 
    # invalid file paths gracefully" acceptance criteria.
    if not os.path.exists(file_path):
        print(f"ERROR: File not found at path: {file_path}")
        return None
    
    try:
        # Load the CSV file. pandas automatically handles common CSV structures.
        df = pd.read_csv(file_path)
        print(f"Successfully loaded {len(df)} records from {file_path}")
        return df
    except Exception as e:
        # Catch other potential errors (e.g., file corruption, wrong format)
        print(f"ERROR loading data: {e}")
        return None

# Example usage for testing purposes (not run when imported)
if __name__ == '__main__':
    
    sample_path = "data/financial_transactions.csv"
    
    # Check if the sample file exists before trying to load it
    if os.path.exists(sample_path):
        df_transactions = load_data(sample_path)
        if df_transactions is not None:
            print("\nDataFrame Head:")
            print(df_transactions.head())
    else:
        print(f"Placeholder file '{sample_path}' missing. Cannot run internal test.")