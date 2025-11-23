import pandas as pd

def summarize_transactions(df: pd.DataFrame) -> dict:
    """
    Returns total income and total expenses from a cleaned DataFrame.

    Args:
        df: DataFrame with 'amount' column.

    Returns:
        dict with keys:
            - 'total_income': sum of positive amounts
            - 'total_expenses': sum of negative amounts
    """
    total_income = df[df["amount"] > 0]["amount"].sum()
    total_expenses = df[df["amount"] < 0]["amount"].sum()

    return {
        "total_income": float(total_income),
        "total_expenses": float(total_expenses)
    }

def category_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarizes spending per category.

    Args:
        df: DataFrame with 'amount' and 'category' columns.

    Returns:
        DataFrame with columns:
            - 'category'
            - 'total_spent' (sum of negative amounts per category)
    """
    if "category" not in df.columns or "amount" not in df.columns:
        raise ValueError("DataFrame must have 'category' and 'amount' columns")

    # Only consider expenses (negative amounts)
    expenses = df[df["amount"] < 0].copy()

    summary = (
        expenses
        .groupby("category")["amount"]
        .sum()
        .abs()
        .reset_index()
        .rename(columns={"amount": "total_spent"})
        .sort_values(by="total_spent", ascending=False)
        .reset_index(drop=True)
    )

    return summary
