import pandas as pd


def load_data(path):
    """Loads the CSV file and returns a DataFrame."""
    return pd.read_csv(path)
