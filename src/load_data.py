import pandas as pd
import os
from typing import Optional

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardizes column names for consistent downstream processing.
    - strips whitespace
    - lowercases
    - replaces spaces and special characters with underscores
    - removes duplicate column names
    """
    cleaned_cols = []
    seen = set()

    for col in df.columns:
        new_col = (
            col.strip()
               .lower()
               .replace(" ", "_")
               .replace("-", "_")
               .replace("/", "_")
        )

        # Ensure unique names
        while new_col in seen:
            new_col = new_col + "_dup"

        seen.add(new_col)
        cleaned_cols.append(new_col)

    df.columns = cleaned_cols
    return df


def load_data(file_path: str) -> Optional[pd.DataFrame]:
    """
    Loads financial transaction data from a CSV file.
    Cleans column names and handles errors gracefully.
    """
    if not os.path.exists(file_path):
        print(f"ERROR: File not found at path: {file_path}")
        return None
    
    try:
        df = pd.read_csv(file_path)

        # Handle empty CSV
        if df.empty:
            print("ERROR: CSV file is empty.")
            return None
        
        # Normalize column names
        df = clean_column_names(df)

        print(f"Successfully loaded {len(df)} records from {file_path}")
        return df
    
    except Exception as e:
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