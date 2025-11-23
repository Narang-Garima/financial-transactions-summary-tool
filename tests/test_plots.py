import pandas as pd
import matplotlib.pyplot as plt
from src.plots import plot_category_spending

def test_plot_category_spending():
    df = pd.DataFrame({
        "category": ["food", "rent", "food", "salary"],
        "amount": [-20, -50, -30, 100]
    })
    
    fig = plot_category_spending(df)
    
    # Check that a Figure object is returned
    assert isinstance(fig, plt.Figure)
