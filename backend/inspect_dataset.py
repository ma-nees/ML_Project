# inspect_dataset.py
import pandas as pd

dataset_path = 'data/student-por.csv'

print("="*60)
print("Dataset Inspection")
print("="*60)

# Read the first few lines as raw text
print("\nFirst 3 lines of raw file:")
with open(dataset_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i < 3:
            print(f"Line {i+1}: {line[:200]}...")
        else:
            break

print("\n" + "="*60)
print("Trying different reading methods:")
print("="*60)

# Method 1: Using semicolon with engine='python'
try:
    print("\nMethod 1: sep=';', engine='python'")
    df1 = pd.read_csv(dataset_path, sep=';', engine='python', nrows=5)
    print(f"  Shape: {df1.shape}")
    print(f"  Columns: {df1.columns.tolist()[:5]}...")
    if 'G3' in df1.columns:
        print(f"  ✅ Found G3! Values: {df1['G3'].tolist()}")
except Exception as e:
    print(f"  Error: {e}")

# Method 2: Using semicolon with quoting
try:
    print("\nMethod 2: sep=';', quotechar='\"'")
    df2 = pd.read_csv(dataset_path, sep=';', quotechar='"', nrows=5)
    print(f"  Shape: {df2.shape}")
    print(f"  Columns: {df2.columns.tolist()[:5]}...")
    if 'G3' in df2.columns:
        print(f"  ✅ Found G3! Values: {df2['G3'].tolist()}")
except Exception as e:
    print(f"  Error: {e}")

# Method 3: Using pandas with on_bad_lines
try:
    print("\nMethod 3: sep=';', on_bad_lines='skip'")
    df3 = pd.read_csv(dataset_path, sep=';', on_bad_lines='skip', nrows=5)
    print(f"  Shape: {df3.shape}")
    print(f"  Columns: {df3.columns.tolist()[:5]}...")
    if 'G3' in df3.columns:
        print(f"  ✅ Found G3! Values: {df3['G3'].tolist()}")
except Exception as e:
    print(f"  Error: {e}")