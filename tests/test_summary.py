import pandas as pd
from src.summary import summarize_transactions, category_summary

# ----------------------------
# Tests for summarize_transactions (US3)
# ----------------------------
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


# ----------------------------
# Tests for category_summary (US4)
# ----------------------------
def test_category_summary_basic():
    data = {
        "date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04"],
        "amount": [-20, -50, -30, 100],
        "category": ["food", "rent", "food", "salary"]
    }
    df = pd.DataFrame(data)
    result = category_summary(df)

    assert result.shape[0] == 2  # only food and rent categories with expenses
    assert result.loc[result['category'] == 'food', 'total_spent'].values[0] == 50  # 20+30
    assert result.loc[result['category'] == 'rent', 'total_spent'].values[0] == 50


def test_category_summary_empty():
    df = pd.DataFrame({
        "date": ["2024-01-01"],
        "amount": [100],
        "category": ["salary"]
    })
    result = category_summary(df)
    assert result.shape[0] == 0  # no expenses
