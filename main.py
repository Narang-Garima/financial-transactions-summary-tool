from src.load_data import load_data
from src.clean_data import clean_data
from src.summary import summarize_transactions


def run():
    # Example workflow
    df = load_data('data/financial_transactions.csv')
    df = clean_data(df)
    print(summarize_transactions(df))


if __name__ == '__main__':
    run()
