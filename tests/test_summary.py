import pandas as pd
from src.summary import summarize_transactions

def test_summarize_transactions_basic():
    data = {
        "date": ["2024-01-01", "2024-01-02", "2024-01-03"],
        "amount": [200, -50, 100],
    }
    
    df = pd.DataFrame(data)
    result = summarize_transactions(df)
    
    assert result["total_income"] == 300.0
    assert result["total_expenses"] == -50.0


def test_summarize_transactions_all_negative():
    data = {
        "date": ["2024-01-01", "2024-01-02"],
        "amount": [-10, -20],
    }

    df = pd.DataFrame(data)
    result = summarize_transactions(df)

    assert result["total_income"] == 0.0
    assert result["total_expenses"] == -30.0
