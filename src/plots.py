import matplotlib.pyplot as plt


def plot_category_spending(df):
    """Returns a matplotlib bar chart of spending by category."""
    fig, ax = plt.subplots()
    df.groupby('Category')['Amount'].sum().plot(kind='bar', ax=ax)
    return fig
