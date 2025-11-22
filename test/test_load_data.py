import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import os
import pandas as pd
import pytest
from src.load_data import load_data, clean_column_names


# -----------------------------------------------------------
# Test — Column name cleaning
# -----------------------------------------------------------
def test_clean_column_names():
    df = pd.DataFrame({
        " Transaction ID ": [1],
        "Date": ["2024-01-10"],
        "AMOUNT ($)": [100],
        "category/type": ["Food"],
        "Category Type": ["Duplicate"],
    })

    df_clean = clean_column_names(df)

    assert df_clean.columns.tolist() == [
        "transaction_id",
        "date",
        "amount_($)",
        "category_type",
        "category_type_dup"
    ]


# -----------------------------------------------------------
# Test — Load CSV with messy columns → cleaned correctly
# -----------------------------------------------------------
def test_load_data_cleans_columns(tmp_path):
    csv_content = (
        " Transaction ID ,Date , AMOUNT ($) ,category/type\n"
        "1,2024-01-10,-45.90,Food\n"
    )

    file = tmp_path / "messy.csv"
    file.write_text(csv_content)

    df = load_data(str(file))

    assert df is not None
    assert df.columns.tolist() == [
        "transaction_id",
        "date",
        "amount_($)",
        "category_type"
    ]


# -----------------------------------------------------------
# Test — Missing file
# -----------------------------------------------------------
def test_load_data_missing_file(tmp_path):
    missing_file = tmp_path / "no.csv"
    df = load_data(str(missing_file))
    assert df is None


# -----------------------------------------------------------
# Test — Empty CSV
# -----------------------------------------------------------
def test_load_data_empty_csv(tmp_path):
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("")  # write empty file

    df = load_data(str(empty_file))
    assert df is None


# -----------------------------------------------------------
# Test — Corrupted CSV
# -----------------------------------------------------------
def test_load_data_corrupted_csv(tmp_path):
    bad_file = tmp_path / "bad.csv"
    bad_file.write_text(";;;;;;THIS_IS_NOT_VALID_CSV;;;;;;")

    df = load_data(str(bad_file))
    assert df is None


# -----------------------------------------------------------
# Test — Realistic financial CSV
# -----------------------------------------------------------
def test_load_data_financial(tmp_path):
    csv_content = (
        "transaction id , date , amount , category , account , description\n"
        "1,2024-02-01,-89.50,Food,Credit Card,Lunch and snacks\n"
        "2,2024-02-02,3200.00,Income,Checking,Salary deposit\n"
    )

    file = tmp_path / "finance.csv"
    file.write_text(csv_content)

    df = load_data(str(file))

    assert df is not None
    assert len(df) == 2
    assert df.columns.tolist() == [
        "transaction_id",
        "date",
        "amount",
        "category",
        "account",
        "description"
    ]
