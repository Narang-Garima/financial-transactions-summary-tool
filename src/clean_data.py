import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the financial transactions dataset.

    Steps:
    - Handle missing values
    - Convert 'date' column to datetime
    - Convert 'amount' column to numeric
    - Remove duplicates
    """
    df = df.copy()

    # 1. Handle missing values
    df = df.dropna(how='all')

    # 2. Convert 'date' column
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # 3. Convert 'amount' column
    if 'amount' in df.columns:
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    # 4. Remove duplicates
    df = df.drop_duplicates()

    return df
