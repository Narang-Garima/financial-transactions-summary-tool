import pandas as pd
import matplotlib.pyplot as plt

def plot_category_spending(df: pd.DataFrame) -> plt.Figure:
    """
    Returns a matplotlib Figure object showing spending per category.
    
    Args:
        df: DataFrame with 'category' and 'amount' columns.

    Returns:
        matplotlib.figure.Figure
    """
    if "category" not in df.columns or "amount" not in df.columns:
        raise ValueError("DataFrame must have 'category' and 'amount' columns")
    
    # Filter for expenses
    expenses = df[df["amount"] < 0].copy()
    
    # Aggregate total spent per category
    summary = expenses.groupby("category")["amount"].sum().abs()
    
    # Create figure
    fig, ax = plt.subplots(figsize=(6, 4))
    summary.plot(kind="bar", ax=ax)
    ax.set_title("Spending per Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Amount Spent")
    
    plt.tight_layout()
    return fig
