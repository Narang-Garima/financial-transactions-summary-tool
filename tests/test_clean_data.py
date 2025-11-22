import pandas as pd
from src.clean_data import clean_data

def test_clean_data_basic():
    df = pd.DataFrame({
        'date': ['2020-01-01', '2020-01-01', None],
        'amount': ['100', '100', '50'],
        'category': ['food', 'food', None]
    })
    cleaned = clean_data(df)
    
    # Expect duplicates removed and empty row dropped
    assert cleaned.shape[0] == 2
    
    # Check types
    assert pd.api.types.is_numeric_dtype(cleaned['amount'])
    assert pd.api.types.is_datetime64_any_dtype(cleaned['date'])
