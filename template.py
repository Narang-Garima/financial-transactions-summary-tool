import os

# Folder structure
folders = [
    "src",
    "data",
    "docs",
    "test"
]

# Files to create (empty)
files = [
    "README.md",
    ".gitignore",
    "main.py",
    "src/load_data.py",
    "src/clean_data.py",
    "src/summary.py",
    "src/plots.py",
    "test/test_load_data.py",
    "docs/team_liftoff.md"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")

# Create empty files
for file_path in files:
    folder = os.path.dirname(file_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

    # Create empty file
    with open(file_path, "w") as f:
        pass
    print(f"Created empty file: {file_path}")

print("\nEmpty project template setup complete!")
