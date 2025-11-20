import os

# Folder structure
folders = [
    "src",
    "data",
    "docs"
]

# Files to create with starter content
files = {
    "README.md": "# Financial Transactions Summary Tool\n\nThis project loads, cleans, and summarizes financial transaction data.\n\n",
    ".gitignore": "__pycache__/\n*.pyc\n.ipynb_checkpoints/\n",
    "main.py": "from src.load_data import load_data\nfrom src.clean_data import clean_data\nfrom src.summary import summarize_transactions\n\n\ndef run():\n    # Example workflow\n    df = load_data('data/financial_transactions.csv')\n    df = clean_data(df)\n    print(summarize_transactions(df))\n\n\nif __name__ == '__main__':\n    run()\n",
    "src/load_data.py": "import pandas as pd\n\n\ndef load_data(path):\n    \"\"\"Loads the CSV file and returns a DataFrame.\"\"\"\n    return pd.read_csv(path)\n",
    "src/clean_data.py": "def clean_data(df):\n    \"\"\"Cleans the dataset: handle missing values, fix dates, etc.\"\"\"\n    # Placeholder: modify later\n    df = df.dropna()\n    return df\n",
    "src/summary.py": "def summarize_transactions(df):\n    \"\"\"Returns summary of total income and expenses.\"\"\"\n    # Placeholder: modify later\n    summary = df.describe(include='all')\n    return summary\n",
    "src/plots.py": "import matplotlib.pyplot as plt\n\n\ndef plot_category_spending(df):\n    \"\"\"Returns a matplotlib bar chart of spending by category.\"\"\"\n    fig, ax = plt.subplots()\n    df.groupby('Category')['Amount'].sum().plot(kind='bar', ax=ax)\n    return fig\n",
    "docs/team_liftoff.md": "# Team Liftoff Summary\n\n(Add your mission, vision, working agreements, DoD here.)\n"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")

# Create files
for file_path, content in files.items():
    folder = os.path.dirname(file_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

    with open(file_path, "w") as f:
        f.write(content)
    print(f"Created file: {file_path}")

print("\nProject template setup complete!")
